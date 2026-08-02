# Rclone Video Ideas

## Candidate 1 — When transferring between clouds, why avoid local bandwidth?
- Source: `README.md`
- Topic: Direct cloud-to-cloud transfer path selection
- Hook: Moving 100 GB between two S3-compatible services normally downloads your entire 100 GB locally
- Key case: Transferring data from AWS S3 to Cloudflare R2 without your client machine ever receiving the bytes
- The Question: When both backends speak the same underlying protocol, how does rclone detect and choose a direct path instead of routing through you?
- Core idea: Protocol negotiation; rclone detects protocol-compatible backends and routes through server-side operations instead of local buffering
- Visual object: Network diagram showing two paths—one through the local machine, one direct cloud-to-cloud—with the system choosing the direct route
- Manim move: split (revealing the two possible paths) then collapse (choosing direct routing)
- Example seed: User transfers 500 GB from a MinIO cluster to AWS S3 in 3 minutes instead of the 45 minutes a local download-then-upload would require
- Length band: 2–3 min
- Still lanes: geo, c2v
- Prerequisites: S3 API, network fundamentals
- Exclusions: Full protocol specifications, authentication details
- Score: 10/10

## Candidate 2 — How do you present a filesystem interface to an API?
- Source: `docs/content/_index.md`
- Topic: Bridging cloud APIs to filesystem semantics
- Hook: Cloud storage is an API; your programs expect `open()`, `read()`, `write()` on a real disk
- Key case: Mounting Google Drive at `/mnt/gdrive` and editing files directly with vim, with changes syncing back to the cloud
- The Question: How does rclone translate filesystem operations (open, read, write, delete) into cloud API calls that preserve semantics?
- Core idea: FUSE (Linux/macOS) and WinFSP (Windows) act as a bridge; rclone intercepts filesystem syscalls and routes them to backend operations
- Visual object: Filesystem tree accessible through a mount point, files from cloud storage indistinguishable from local files
- Manim move: transform (filesystem calls becoming API operations) or bridge (two worlds connecting at the mount point)
- Example seed: Developer mounts OneDrive at `/cloud`, runs `ls`, opens a document in their text editor, saves it; the change appears in the cloud within seconds
- Length band: 2–3 min
- Still lanes: geo, c2v
- Prerequisites: Filesystem mount concepts, FUSE (Linux) or WinFSP (Windows) existence
- Exclusions: Kernel-level implementation, platform-specific syscall translation, caching strategy
- Score: 8/10

## Candidate 3 — Can you add encryption and compression without rewriting every backend?
- Source: `README.md`, `docs/content/_index.md`
- Topic: Layered filesystem transformations via wrapper pattern
- Hook: You want to encrypt files on Google Drive AND compress them—do you code two features separately into every backend?
- Key case: Configuring a single "secure-cloud" remote that wraps Google Drive and applies both AES256 encryption and gzip, transparently
- The Question: If you want to apply a transformation (encrypt, compress, chunk) to any backend without duplicating code for each backend combination, how do you design this?
- Core idea: Wrapper pattern; each virtual backend wraps another and applies one transformation; data flows through the composition stack
- Visual object: Nested boxes showing data entering, passing through encryption, then compression, then exiting to storage
- Manim move: morph (data changing form as it passes through each layer) or scan (revealing each layer in the stack)
- Example seed: User creates "safe-s3" wrapping S3 with AES256 encryption and gzip compression; syncs 1000 files with both transformations applied automatically
- Length band: 2–3 min
- Still lanes: c2v, raster
- Prerequisites: Concept of wrapping/decoration pattern, basic encryption and compression ideas
- Exclusions: Cipher algorithm details, compression codec specifics, key management
- Score: 7/10

## Candidate 4 — When both sides change the same file, how does two-way sync decide?
- Source: `README.md`
- Topic: Bidirectional sync with conflicting changes
- Hook: Team member A edits `document.pdf` on her laptop, team member B edits it on his desktop, both trigger sync
- Key case: Bisync detects that both sides have modified the same file since the last sync and flags the conflict
- The Question: In two-way sync where both directories can change independently, how does rclone detect conflicts and decide what to preserve?
- Core idea: State tracking with conflict detection; rclone remembers what was synced last, detects changes on both sides, and marks conflicts explicitly for user resolution
- Visual object: Timeline showing two edits diverging from a common ancestor state, then colliding, then being marked/resolved
- Manim move: split (showing divergence from common ancestor) then collapse (conflict reconciliation)
- Example seed: Both users edit `shared.txt`; bisync detects the conflict and renames one version to `shared.txt.conflict`, leaving both versions visible
- Length band: 2–3 min
- Still lanes: c2v, raster
- Prerequisites: Concept of bidirectional sync, merge conflicts (e.g., git)
- Exclusions: Specific conflict resolution algorithms, post-conflict workflow
- Score: 7/10

## Candidate 5 — When a 10 GB sync fails at 8 GB, must you start over?
- Source: `docs/content/_index.md`
- Topic: Resumable transfers via checkpoint persistence
- Hook: Your backup sync to S3 fails mid-transfer due to network loss—rclone doesn't restart from file 1
- Key case: Network drops after 500 of 1000 files complete; you restart the sync and it continues from file 501
- The Question: How does rclone remember which files were successfully transferred when a sync is interrupted?
- Core idea: Checkpoint tracking; rclone stores state of completed file transfers and resumes from the last successful boundary, not the beginning
- Visual object: Progress bar filling incrementally, pausing on failure, resuming from the checkpoint
- Manim move: accumulate (progress building), pause (interruption), accumulate (resuming from checkpoint)
- Example seed: User syncs 1000 photos to cloud; transfer fails at photo 500, restarts next hour from photo 501 instead of 1
- Length band: 2–3 min
- Still lanes: c2v, raster
- Prerequisites: Understanding of file transfer and failure modes
- Exclusions: Exact state storage format, resume protocol negotiation with each backend
- Score: 7/10

## Candidate 06 — When two clouds share no common hash, integrity checking silently vanishes
- Source: `docs/content/overview.md`
- Topic: Cross-backend checksum negotiation and silent fallback
- Hook: You configure rclone to verify every byte during a cloud-to-cloud transfer, but the verification never actually runs
- Key case: Syncing from 1Fichier (Whirlpool hash only) to Mega (no hash support) — the intersection of their hash sets is empty, so rclone silently falls back to size comparison
- The Question: Common hash should enable integrity verification; this pair shares none; why does rclone not error or warn the user?
- Core idea: Rclone computes the intersection of source and destination hash sets before transfer; empty intersection triggers a silent fallback to size-only comparison — a corrupted file with the same byte count passes undetected
- Visual object: The backend hash compatibility matrix from the overview table, two rows highlighted, their hash columns scanned left-to-right, the intersection cell shown empty
- Manim move: scan (tracing hash columns for both backends) then collapse (to the empty intersection, revealing the fallback mode)
- Example seed: User syncs 200 files from Mega (no hash) to 1Fichier (Whirlpool); one file is silently corrupted during transit but matches size; rclone reports success — illustrative
- Length band: 2–3 min
- Still lanes: raster with hash matrix, c2v
- Prerequisites: Concept of checksums as integrity checks, hash function basics
- Exclusions: Specific hash algorithm internals, `--checksum` flag behavior when hashes do align, `rclone check` command details
- Score: 9/10

## Candidate 07 — Cloud storage lets two files share one name; sync assumes that's impossible
- Source: `docs/content/overview.md`
- Topic: Duplicate filenames breaking sync's uniqueness invariant
- Hook: Every sync algorithm assumes a filename uniquely identifies a file in a directory — Google Drive does not
- Key case: Google Drive folder contains two files both named "report.pdf" with different contents; rclone lists the directory and finds two entries occupying one name slot
- The Question: Sync maps source names to destination names one-to-one; this case has two source files sharing one name; which file does rclone write to the destination?
- Core idea: Rclone detects the invariant violation, logs a warning, and skips the ambiguous files rather than silently picking one; the dedicated `rclone dedupe` command then lets the user resolve each conflict explicitly
- Visual object: A directory listing showing two "report.pdf" icons, a sync arrow pointing to a destination folder with a single slot, the collision made concrete
- Manim move: split (one filename label, two diverging file objects) then collapse (both trying to occupy the single destination slot, triggering the conflict marker)
- Example seed: User has "budget.xlsx" appearing twice in a Google Drive folder with different sizes; `rclone copy` to local disk logs duplicate warnings and copies only one version; the other version is preserved only by running `rclone dedupe` — illustrative
- Length band: 2–3 min
- Still lanes: c2v, raster with directory tree
- Prerequisites: Basic sync semantics, understanding that filenames normally serve as unique keys
- Exclusions: Dedupe strategy details (largest, newest, rename), Google Drive API internals, how duplicates are created in the first place
- Score: 9/10

## Candidate 08 — How does a command-line tool become an embeddable library without a subprocess?
- Source: `librclone/README.md`
- Topic: Exposing a CLI as an in-process JSON-RPC library
- Hook: Spawning `rclone sync` as a subprocess for every operation is slow; librclone lets you call the same code as a function
- Key case: An Android app calling `Gomobile.rcloneRPC("sync/copy", jsonParams)` to trigger a cloud backup in-process, with no subprocess fork and no shell parsing
- The Question: A CLI tool's command dispatcher is built for human shell invocation; how does rclone surface the same dispatch table as callable in-process functions?
- Core idea: Rclone's internal command router — the same code path that handles `rclone sync` — is exposed behind a single `RcloneRPC(method, json)` entry point; only the input/output channel changes, not the operation logic
- Visual object: Two side-by-side diagrams: process tree with subprocess fork vs. in-process call stack sharing the same dispatcher node
- Manim move: transform (CLI process spawning tree morphing into a single in-process call graph)
- Example seed: Mobile backup app calls `RcloneRPC("sync/copy", `{"srcFs":"/photos","dstFs":"drive:backup"}`)` and receives a JSON result in 50 ms without OS-level process creation — illustrative
- Length band: ~1 min
- Still lanes: c2v, geo
- Prerequisites: Understanding of process spawning overhead, basic RPC concepts
- Exclusions: cgo build specifics, Windows DLL memory management rules, gomobile binding details
- Score: 6/10
