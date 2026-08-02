## cookbooks-knowledge-graph-construction

- **Source path:** claude-cookbooks/capabilities/knowledge_graph/guide.ipynb
- **Teachable claim:** Claude extracts typed entities and relations from unstructured documents into a NetworkX graph — multi-hop questions that RAG can't answer ("who works with people who worked on project X") become graph traversal queries.
- **Suggested builder:** terminal-screencast
- **Suggested channel:** claude-liam
- **Runtime estimate:** medium (5–7 min)

### Visual beats
1. The RAG failure case: multi-hop question where no single document contains the answer; show the retrieval returning partial results and Claude guessing
2. Extraction prompt: structured output with typed entities (Person, Project, Organization) and relations (WORKS_WITH, MANAGED, CONTRIBUTED_TO) — the JSON schema drives consistent extraction
3. Graph build: `networkx.DiGraph` populated from extractions; `matplotlib` visualization of the entity network; nodes sized by degree
4. Multi-hop traversal: `nx.shortest_path` answers the cross-document question that stumped RAG; show the path through two intermediate nodes

### Score
- Teachability: 5/5 — "RAG retrieves, graphs traverse; use graphs for multi-hop" is the sharp design choice
- Visual: 5/5 — the NetworkX graph visualization is a natural payoff visual
- Pull: 4/5 — enterprise knowledge management is a common use case
- Freshness: 4/5 — knowledge graphs are established; using Claude for extraction with typed schemas is the fresh angle
- **Total: 18/20**
