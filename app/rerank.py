from functools import lru_cache

from sentence_transformers import CrossEncoder

# A fast, standard cross-encoder model for reranking search results
DEFAULT_RERANK_MODEL = "cross-encoder/ms-marco-MiniLM-L-6-v2"

@lru_cache(maxsize=1)
def _cross_encoder():
    """Load the cross-encoder model once and cache it."""
    return CrossEncoder(DEFAULT_RERANK_MODEL)

def rerank(query: str, candidates: list[dict], n_results: int = 5) -> list[dict]:
    """Rescore candidates using a cross-encoder and return the top n."""
    if not candidates:
        return []

    model = _cross_encoder()
    
    # Create pairs of (query, chunk_text) to score
    pairs = [(query, c["text"]) for c in candidates]
    
    # Predict relevance scores
    scores = model.predict(pairs)

    # Attach scores to the candidate dictionaries
    for candidate, score in zip(candidates, scores):
        candidate["rerank_score"] = float(score)

    # Sort by the new score in descending order and return the top results
    ranked = sorted(candidates, key=lambda x: x["rerank_score"], reverse=True)
    
    return ranked[:n_results]