import sys
from app.store import _collection

def delete_document_chunks(doc_id: str):
    """Deletes all chunks associated with a specific doc_id from ChromaDB."""
    collection = _collection()
    
    # ChromaDB metadata filtering to find chunks for this doc_id
    results = collection.get(where={"doc_id": doc_id})
    
    if not results["ids"]:
        print(f"No chunks found for document ID: {doc_id}")
        return False
        
    collection.delete(ids=results["ids"])
    print(f"Successfully deleted {len(results['ids'])} chunks for document ID: {doc_id}")
    return True

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python -m scripts.delete_document <doc_id>")
        sys.exit(1)
        
    doc_id_to_delete = sys.argv[1]
    delete_document_chunks(doc_id_to_delete)