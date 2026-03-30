import numpy as np
from sklearn.preprocessing import normalize

class MultiTenantEmbeddingPipeline:
    def __init__(self, embedding_model):
        self.embedding_model = embedding_model
        self.embeddings = {}

    def add_tenant(self, tenant_id):
        self.embeddings[tenant_id] = []

    def remove_tenant(self, tenant_id):
        if tenant_id in self.embeddings:
            del self.embeddings[tenant_id]

    def embed(self, tenant_id, texts):
        if tenant_id not in self.embeddings:
            raise ValueError(f"Tenant {tenant_id} is not registered.")
        tenant_embeddings = self.embedding_model.encode(texts)
        # Optionally normalize embeddings
        tenant_embeddings = normalize(tenant_embeddings)
        self.embeddings[tenant_id].extend(tenant_embeddings)
        return tenant_embeddings

    def get_embeddings(self, tenant_id):
        if tenant_id not in self.embeddings:
            raise ValueError(f"Tenant {tenant_id} is not registered.")
        return self.embeddings[tenant_id]