import pandas as pd
import joblib

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

df = pd.read_csv("data/processed/cleaned_resumes.csv")

# Fake labels demo
# Sau này bạn có thể thay bằng category thật

df["category"] = [
    "Software"
    if "python" in str(text).lower()
    else "Other"
    for text in df["skills"]
]

X = df["cleaned_resume"]

y = df["category"]

vectorizer = TfidfVectorizer(max_features=3000)

X_vectorized = vectorizer.fit_transform(X)

encoder = LabelEncoder()

y_encoded = encoder.fit_transform(y)

X_train, X_test, y_train, y_test = train_test_split(
    X_vectorized,
    y_encoded,
    test_size=0.2,
    random_state=42
)

model = RandomForestClassifier()

model.fit(X_train, y_train)

predictions = model.predict(X_test)

accuracy = accuracy_score(y_test, predictions)

print(f"Accuracy: {accuracy}")

joblib.dump(model, "models/random_forest_model.pkl")

joblib.dump(vectorizer, "models/tfidf_vectorizer.pkl")

joblib.dump(encoder, "models/label_encoder.pkl")

print("Model saved.")