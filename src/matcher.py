from sklearn.metrics.pairwise import cosine_similarity
import joblib


vectorizer = joblib.load("models/tfidf_vectorizer.pkl")


def calculate_match_score(cv_text, jd_text):

    cv_vector = vectorizer.transform([cv_text])

    jd_vector = vectorizer.transform([jd_text])

    similarity = cosine_similarity(
        cv_vector,
        jd_vector
    )[0][0]

    return round(similarity * 100, 2)