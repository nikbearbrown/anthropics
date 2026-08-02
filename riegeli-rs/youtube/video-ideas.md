# riegeli-rs Video Ideas

## Candidate 1 — Why decode by prepending bytes, then reverse the whole buffer?
- Source: `TRANSPOSE.md` (Backward-writing and finalization), `riegeli/TRANSPOSE.md`
- Topic: Record assembly order in columnar decode
- Hook: Fields arrive in decode order but protobufs need them in wire order. Appending bytes means shifting N times per field. What if you wrote backward?
- Key case: A 3-field record (tag + field 1, tag + field 2, tag + field 3) decoded field-by-field. Appending forces 50 bytes left on each field add. Prepending and reversing once costs the same total work but keeps the buffer static during decode.
- The Question: Prepending (backward writing) forces a final reversal. Why is this faster than forward appending?
- Core idea: Appending requires shifting existing data on each write. Prepending is O(1) per write (just a cursor decrement). A single O(n) reversal at the end costs less than N shifts during construction.
- Visual object: A buffer growing leftward with a moving cursor, then flipping to rightward orientation.
- Manim move: transform
- Example seed: Decode 100 records with 5 fields each. Show 3 records: bytes prepended during decode (cursor moves left), then the full buffer reverses in one step. Contrast the shift cost (500 operations) vs. prepend+reverse (100 ops).
- Length band: 2–3 min
- Still lanes: c2v (cursor position diagram), raster (buffer memory state)
- Prerequisites: protobuf wire format, vector memory layout
- Exclusions: submessage stack, record boundary markers, varint restoration
- Score: 8/10

## Candidate 2 — How does a state machine encode thousands of field transitions in bytes?
- Source: `TRANSPOSE.md` (Optimized state machine), `riegeli/TRANSPOSE.md`
- Topic: Efficient transition encoding in state machines
- Hook: A protobuf state machine may have 50 states and 50+ possible destinations. A naive transition table is huge. But actual messages use only a fraction of them. How do you compress the graph without slowing decode?
- Key case: 1M-record event log where 99% follow the pattern (user_id → timestamp → action → metadata), but 1% skip metadata. The decoder needs to distinguish: after action, is metadata next (implicit) or end (explicit)?
- The Question: The transition stream could encode all reachable paths, but that's expensive. How does the encoder collapse frequent transitions into implicit next_node values and rare transitions into indexed public lists?
- Core idea: Collect transition statistics during encode. Destinations hit ≥10 times from a source become "private" (no byte consumed). The most frequent becomes implicit (encoded in next_node_index). Others enter a shared public list. When the public list exceeds 63 slots, NoOp states bridge the gap, allowing multi-byte transitions via implicit hops.
- Visual object: A state graph with private destinations (solid arrows), public destinations (dashed arrows), and NoOp bridges (chain links).
- Manim move: accumulate, split
- Example seed: 5 states (fields 1–5), 1000 records. State 1→2 occurs 950 times, 1→3 occurs 50 times. Apply the ≥10 threshold: 1→2 becomes implicit, 1→3 goes to the public list. Show the byte stream compacting: 1 byte per 50 transitions instead of a 5×5 table.
- Length band: 3–5 min
- Still lanes: c2v (state diagram, transition table), raster (byte encoding layout)
- Prerequisites: state machines, protobuf field structure
- Exclusions: NoOp insertion algorithm, per-node base_index calculation
- Score: 8/10

## Candidate 3 — How does stripping high bits compress a column of varints?
- Source: `TRANSPOSE.md` (Varint encoding), `riegeli/TRANSPOSE.md`
- Topic: Columnar compression of varint fields
- Hook: A million-record log has a million varint timestamps (8 bytes each). Every byte carries a continuation bit that tells you "more bytes follow." In a column, that information is redundant — you already know the byte count from the decoder's subtype. Can you drop those bits?
- Key case: A column of 1000 varints, each 8 bytes. Naively stored: each byte carries a continuation bit (128 bytes of overhead). Stripped: 1000 bytes, or 12.5% smaller.
- The Question: Every varint byte has a high continuation bit. In row-oriented storage, you need them to know where to stop. In a column, the decoder already knows the byte count. Why keep the bits?
- Core idea: Before storage, strip the high bit from every varint byte. At decode, when reading a varint of known length, restore the high bit to all but the last byte. The subtype encodes length, so the decoder knows exactly where to restore.
- Visual object: A byte string with high bits highlighted, then dimmed, then restored.
- Manim move: transform
- Example seed: Varint 300 encodes as `[0xAC, 0x02]` in standard protobuf (high bits: 1,0). In the column: store `[0x2C, 0x02]` (high bits stripped). At decode with subtype=2, restore to `[0xAC, 0x02]`.
- Length band: ~1–2 min
- Still lanes: raster (bit strings, highlighting)
- Prerequisites: varint encoding (protobuf format)
- Exclusions: inline varint optimization, other compression techniques
- Score: 9/10

## Candidate 4 — Why split columns into independent buckets for compression?
- Source: `TRANSPOSE.md` (Buckets and buffers), `riegeli/TRANSPOSE.md`
- Topic: Columnar data grouping for compression trade-offs
- Hook: Compressing each column separately lets you skip decompressing unwanted columns. But compression ratio suffers — the compressor can't see cross-column patterns. Compressing all columns together is best for ratio but forces all-or-nothing decompression. Can you have both?
- Key case: A protobuf with 100 fields across 1M records. IDs (fields 1–10) are 4 bytes each, tags (fields 11–50) are varints, payloads (fields 51–100) are strings. If you compress each separately, skipping field 5 is fast but the compressor sees 100 separate streams. If all together, compression is great but you must decompress all 100 fields even if you only want field 5.
- The Question: Field projection lets you skip fields. If you group columns into buckets for compression, can you still identify and skip entire buckets?
- Core idea: Group columns greedily: start a new bucket when adding the next column would exceed bucket_size / 2. This trades cross-bucket entropy for intra-bucket skip granularity. Each bucket is compressed independently. The decoder scans the state machine to find which buffers (columns) are needed, then decompresses only buckets containing those buffers.
- Visual object: Columns stacked vertically, grouped into colored buckets, then each bucket compressed.
- Manim move: split, collapse
- Example seed: 10 columns (sizes [100 B, 150 B, 200 B, 80 B, 120 B, 110 B, 90 B, 130 B, 160 B, 100 B]), bucket limit 500 B. Greedy: bucket 1 = cols 1–3 (450 B, fits), bucket 2 = cols 4–7 (410 B), bucket 3 = cols 8–10. Show how field projection skips bucket 2 if those columns aren't needed.
- Length band: 2–3 min
- Still lanes: geo (column layout, bucket boundaries)
- Prerequisites: column storage, compression, protobuf field numbers
- Exclusions: compression algorithm details, exact bucket_size / 2 formula
- Score: 8/10

## Candidate 5 — How does the encoder detect field-order patterns and build an optimized state machine?
- Source: `TRANSPOSE.md` (State machine construction), `riegeli/TRANSPOSE.md`
- Topic: Statistical optimization of state machines
- Hook: Proto records follow regular field patterns — field 1 before 2, then 3, then 4. 99% of your records follow the same pattern; 1% diverge. The encoder sees this regularity in the data and builds a state machine where the common path is fast (implicit, no byte cost) and the rare paths are slower (explicit, one byte each).
- Key case: Transaction log, 1M records. 950K have fields (user_id → timestamp → amount → merchant). 50K are refunds, skip merchant. The encoder scans and counts: 1→2 (1M times), 2→3 (1M times), 3→4 (950K times), 3→end (50K times). The machine should make 1→2 and 2→3 implicit, and encode 3→{4 or end} with one transition byte.
- The Question: How does the encoder decide which transitions are "implicit" (no byte cost) and which are "explicit" (one transition byte)?
- Core idea: Collect transition statistics during encode. For each source state, count transitions to each destination. Destinations hit ≥10 times become candidates for implicit transitions (encoded in next_node_index). The highest-frequency destination becomes the implicit successor. All others enter a shared public list, indexed by transition byte.
- Visual object: A histogram of transition counts, then a state machine graph with implicit edges highlighted.
- Manim move: accumulate, morph
- Example seed: 5 states (fields 1–5), 1000 records. State 1 → state 2 in 950 records (implicit), state 1 → state 3 in 50 records (explicit, byte 0). State 2 → state 3 always (implicit). Show histograms, apply the ≥10 threshold, reveal implicit vs. explicit edges. Illustrate the byte savings: 50 transition bytes instead of 1000.
- Length band: 2–3 min
- Still lanes: c2v (histogram bar chart), c2v (state transition diagram)
- Prerequisites: protobuf field ordering, state machines
- Exclusions: NoOp bridging, private/public list assignment algorithm
- Score: 7/10

## Candidate 06 — A column of a million integers with zero bytes of data
- Source: `riegeli/TRANSPOSE.md` (Inline varint optimization), `TRANSPOSE.md` (Subtypes)
- Topic: Inline varint encoding — eliminating data buffers for small values
- Hook: Every field in transpose encoding gets a data buffer. But a column of status codes 0–100 can have zero bytes in its buffer. Where did the data go?
- Key case: 1M records, field `status` always in range 0–50. Standard column: 1M bytes in a varint buffer. With inline encoding: the buffer is empty. Each value is recovered entirely from the subtype byte sitting in the state machine node.
- The Question: The decoder must read a value for every field. If the column's data buffer is empty, what does it read?
- Core idea: Subtypes 10–137 (VARINT_INLINE_0 through VARINT_INLINE_MAX) encode values 0–127 directly in the subtype field. The state node carries the value; the decoder skips the buffer cursor entirely. Subtypes 0–9 (VARINT_1 through VARINT_10) indicate buffered values of known byte length. One byte serves as both type tag and value payload.
- Visual object: A state node forking into two paths — left path reads N bytes from buffer; right path reads nothing and extracts value = subtype − 10.
- Manim move: split
- Example seed: Five records with field `status` = [7, 42, 0, 15, 100]. Encoded subtypes: 17, 52, 10, 25, 110. Data buffer byte count: 0. At decode: read subtype 17 → emit value 7; read subtype 52 → emit value 42. No buffer cursor advances. Label illustrative at build time.
- Length band: ~1 min
- Still lanes: raster (subtype byte layout, value range mapping), c2v (decode path fork diagram)
- Prerequisites: varint encoding, columnar storage (Candidate 3)
- Exclusions: VARINT_1..VARINT_10 buffered path, interaction with state machine construction, compression ratio impact of reducing buffer sizes
- Score: 8/10

## Candidate 07 — How does the decoder write a header whose length it doesn't know yet?
- Source: `TRANSPOSE.md` (Backward writing and finalization, Decoding section), `riegeli/TRANSPOSE.md` (Backward-writing decode pattern)
- Hook: A protobuf submessage header must state the byte length of its content before that content appears. In forward decoding, that length is unknown until all nested fields have been decoded. The transpose decoder writes the content first, then fills in the header — with zero backtracking.
- Key case: A `User` record with a nested `Address` submessage containing two fields (15 bytes total). The state machine fires SubmessageEnd first (marks right boundary), then two field nodes write 15 bytes of content leftward, then SubmessageStart fires and writes tag + varint(15) at the new left edge. No re-scanning of completed content.
- The Question: Protobuf wire format requires submessage byte-length before its content. In the transpose decoder, content is written before the header. How is the length computed without a backward scan?
- Core idea: At SubmessageEnd, the decoder pushes `(current_write_pos)` as `end_pos` onto a stack. Field nodes then write content, moving write_pos leftward. At SubmessageStart, it pops `end_pos`; length = `end_pos − write_pos`. Because the buffer grows leftward, `end_pos` is always a fixed, already-placed right boundary; the gap to the current cursor is exactly the content byte count.
- Visual object: A backward-growing buffer with two position markers — `end_pos` pinned on the right, `write_pos` drifting left — and the labeled gap between them.
- Manim move: accumulate
- Example seed: Nested `Address { street: "Main St" }`. SubmessageEnd fires: push end_pos=100. Street field writes 9 bytes: write_pos moves 100→91. SubmessageStart fires: length = 100−91 = 9; write tag + varint(9) at position 89. Final slice [89..100] is the complete, length-correct submessage. Label illustrative at build time.
- Length band: 2–3 min
- Still lanes: raster (buffer with position markers), c2v (stack state diagram with push/pop annotations)
- Prerequisites: protobuf length-delimited wire format, backward-writing pattern (Candidate 1)
- Exclusions: multi-level nesting depth, SubmessageStart/End node construction in the encoder, interaction with record boundary tracking
- Score: 7/10
