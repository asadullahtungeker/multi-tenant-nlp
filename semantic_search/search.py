import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

class SemanticSearch:
    def __init__(self, document_embeddings):
        self.document_embeddings = document_embeddings

    def search(self, query_embedding, top_n=5):
        # Compute cosine similarity between the query and document embeddings
        similarities = cosine_similarity(query_embedding.reshape(1, -1), self.document_embeddings)
        
        # Get the indices of the top_n most similar documents
        top_indices = np.argsort(similarities[0])[-top_n:][::-1]
        return top_indices, similarities[0][top_indices]

# Example usage:
# document_embeddings = np.array([[...], [...], [...]])  # Your document embeddings here
# query_embedding = np.array([...])  # Your query embedding here
# semantic_search = SemanticSearch(document_embeddings)
# top_indices, scores = semantic_search.search(query_embedding)