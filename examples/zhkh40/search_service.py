"""Sanitized portfolio example based on the project's TF-IDF search pattern."""

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def best_match(query: str, documents: list[str]) -> tuple[int, float] | None:
    if not query.strip() or not documents:
        return None

    vectorizer = TfidfVectorizer(lowercase=True)
    matrix = vectorizer.fit_transform([query, *documents])
    scores = cosine_similarity(matrix[0:1], matrix[1:]).ravel()
    index = int(scores.argmax())
    return index, float(scores[index])
