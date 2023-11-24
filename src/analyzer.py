import numpy as np


def cosine_similarity(df1, df2):
    v1 = df1.values
    v2 = df2.values

    cos_sim = np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))
    return cos_sim
