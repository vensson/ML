import json
import pandas as pd
import re
import nltk

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

nltk.download('stopwords')
nltk.download('wordnet')

stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()


def clean_text(text):
    text = text.lower()

    text = re.sub(r'http\S+', '', text)

    text = re.sub(r'[^a-zA-Z\s]', ' ', text)

    text = re.sub(r'\s+', ' ', text)

    words = text.split()

    words = [
        lemmatizer.lemmatize(word)
        for word in words
        if word not in stop_words
    ]

    return " ".join(words)


def extract_skills(annotation):
    skills = []

    for item in annotation:
        if "Skills" in item["label"]:
            for point in item["points"]:
                skills.append(point["text"])

    return " ".join(skills)


def load_and_process_data():
  with open("data/raw/resumes.json", "r", encoding="utf-8") as f:

    data = []

    for line in f:

        line = line.strip()

        if line:
            data.append(json.loads(line))

    rows = []

    for item in data:
        content = item.get("content", "")
        annotation = item.get("annotation", [])

        cleaned = clean_text(content)

        skills = extract_skills(annotation)

        rows.append({
            "resume": content,
            "cleaned_resume": cleaned,
            "skills": skills
        })

    df = pd.DataFrame(rows)

    return df


if __name__ == "__main__":
    df = load_and_process_data()

    print(df.head())

    df.to_csv(
        "data/processed/cleaned_resumes.csv",
        index=False
    )

    print("Saved cleaned dataset.")