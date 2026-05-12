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


def extract_designation(annotation):

    for item in annotation:

        if "Designation" in item["label"]:

            points = item.get("points", [])

            if len(points) > 0:

                return points[0]["text"].strip()

    return "Unknown"


def load_json_lines(filepath):

    data = []

    with open(filepath, "r", encoding="utf-8") as f:

        for line in f:

            line = line.strip()

            if line:

                try:
                    data.append(json.loads(line))

                except Exception as e:

                    print("Error reading line:")
                    print(e)

    return data


def load_and_process_data():

    data = load_json_lines(
        "data/raw/resumes.json"
    )

    rows = []

    for item in data:

        content = item.get("content", "")

        annotation = item.get("annotation", [])

        cleaned = clean_text(content)

        designation = extract_designation(annotation)

        rows.append({
            "resume": content,
            "cleaned_resume": cleaned,
            "designation": designation
        })

    df = pd.DataFrame(rows)

    return df


if __name__ == "__main__":

    df = load_and_process_data()

    print("\nFIRST 5 ROWS:")
    print(df.head())

    print("\nCATEGORY COUNTS:")
    print(df["designation"].value_counts())

    df.to_csv(
        "data/processed/cleaned_resumes.csv",
        index=False
    )

    print("\nSaved cleaned dataset.")