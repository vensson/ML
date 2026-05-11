from src.matcher import calculate_match_score
from src.keyword_extractor import extract_missing_keywords

jd = """
Looking for Python developer with machine learning,
SQL, and communication skills.
"""

cv = """
I am a Python developer with machine learning
and data analysis experience.
"""

score = calculate_match_score(cv, jd)

missing = extract_missing_keywords(cv, jd)

print("MATCH SCORE:")
print(score)

print("\nMISSING KEYWORDS:")
print(missing)