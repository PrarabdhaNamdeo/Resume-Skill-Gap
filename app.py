import streamlit as st

from resume_parser import extract_text_from_pdf
from skill_extractor import extract_skills, missing_skills
from similarity import compute_similarity


st.title("Resume Skill Gap Analyzer")


uploaded_resume = st.file_uploader("Upload your resume (PDF)", type=["pdf"])

job_description = st.text_area("Paste Job Description Here")


if uploaded_resume and job_description:

    with open("temp_resume.pdf", "wb") as f:
        f.write(uploaded_resume.read())

    resume_text = extract_text_from_pdf("temp_resume.pdf")

    resume_skills = extract_skills(resume_text)
    job_skills = extract_skills(job_description)

    match_score = compute_similarity(resume_text, job_description)

    missing = missing_skills(resume_skills, job_skills)

    st.subheader("Match Score")
    st.write(match_score, "%")

    st.subheader("Resume Skills")
    st.write(resume_skills)

    st.subheader("Missing Skills")
    st.write(missing)