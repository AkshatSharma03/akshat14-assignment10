import numpy as np
from sklearn.decomposition import PCA

def perform_search(text_query, image_query, weight, use_pca, pca_components):
    # Placeholder: Replace with actual search functionality
    results = [{"image": f"Image_{i}.jpg", "score": 1.0 - 0.1 * i} for i in range(5)]
    return {"results": results}

def apply_pca(embeddings, k):
    pca = PCA(n_components=k)
    return pca.fit_transform(embeddings)
