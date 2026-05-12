import streamlit as st

from src.matcher import calculate_match_score
from src.keyword_extractor import extract_missing_keywords
from src.predictor import predict_job_category

st.set_page_config(
    page_title="AI Resume Analyzer",
    layout="wide"
)

st.title("AI Resume Analyzer")

st.subheader("Job Description")

jd = st.text_area(
    "Paste Job Description",
    height=200
)

st.subheader("Resume")

cv = st.text_area(
    "Paste Resume",
    height=300
)

if st.button("Analyze Resume"):

    if jd.strip() == "" or cv.strip() == "":

        st.warning("Please fill both fields.")

    else:

        score = calculate_match_score(
            cv,
            jd
        )

        category = predict_job_category(cv)

        missing = extract_missing_keywords(
            cv,
            jd
        )

        st.success("Analysis Completed")

        col1, col2 = st.columns(2)

        with col1:

            st.metric(
                "Match Score",
                f"{score}%"
            )

        with col2:

            st.metric(
                "Predicted Category",
                category
            )

        st.subheader("Missing Keywords")

        if len(missing) == 0:

            st.write("No missing keywords.")

        else:

            for word in missing:

                st.write(f"- {word}")