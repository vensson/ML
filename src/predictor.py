import joblib

model = joblib.load(
    "models/random_forest_model.pkl"
)

vectorizer = joblib.load(
    "models/tfidf_vectorizer.pkl"
)

encoder = joblib.load(
    "models/label_encoder.pkl"
)


def predict_job_category(text):

    vector = vectorizer.transform([text])

    prediction = model.predict(vector)

    category = encoder.inverse_transform(
        prediction
    )[0]

    return category