import re

STOPWORDS = {
    "and",
    "or",
    "the",
    "a",
    "an",
    "for",
    "with",
    "to",
    "of",
    "in",
    "on",
    "at",
    "is",
    "are","looking",
"skill",
"skills",
"developer",
}


def clean_words(text):

    text = text.lower()

    text = re.sub(r'[^a-zA-Z\s]', ' ', text)

    words = text.split()

    words = [
        word
        for word in words
        if word not in STOPWORDS
    ]

    return set(words)


def extract_missing_keywords(cv_text, jd_text):

    cv_words = clean_words(cv_text)

    jd_words = clean_words(jd_text)

    missing = jd_words - cv_words

    return sorted(list(missing))