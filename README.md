# context_aware_retrieval_inference
Multi Document context aware retrieval system inference pipeline for question answering over research papers with strict token and retrieval constraints.

I built this project as **inference-first** With focus on how context is retrieved, assembled, and passed to an LLM at runtime.


## Design Goals & Constraints

### Design Goals
- Enable question answering across **multiple research papers**
- Ensure **context-specific retrieval**
- Explicitly control **token usage and latency**
- Minimize hallucinations through **retrieval grounding and citations**
- Keep the system **simple, inspectable, and reproducible**

### Constraints
- Fixed **maximum context window** per query
- Hard cap on **number of retrieved chunks**
- Answers must rely **only on retrieved context**
- Metrics must be collected at **inference time**


## Non-Goals (V1)
- Agent-based workflows
- Long-term memory or conversation history
- Multi-model ensembling
- Automatic context window expansion
- Benchmarking against proprietary systems


## Project Status
This is the first version  
Focus: Retrieval → Context Assembly → Inference → Metrics
