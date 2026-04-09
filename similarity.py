from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def compute_similarity(resume_text, job_description):

    documents = [resume_text, job_description]
    tfidf = TfidfVectorizer()
    matrix = tfidf.fit_transform(documents)
    similarity_score = cosine_similarity(matrix[0], matrix[1])

    return round(similarity_score[0][0] * 100, 2)