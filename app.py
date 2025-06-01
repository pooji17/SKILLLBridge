import streamlit as st
from resume_parser import extract_text_from_pdf, extract_skills
from job_recommender import recommend_jobs

st.set_page_config(page_title="SkillBridge AI", layout="wide")
st.title("🔍 SkillBridge AI")
st.write("Upload your resume to discover better-fitting or higher-paying career paths.")

uploaded_file = st.file_uploader("Upload your resume (PDF only)", type=["pdf"])

if uploaded_file:
    with st.spinner("Extracting skills..."):
        text = extract_text_from_pdf(uploaded_file)
        skills = extract_skills(text)

    st.subheader("✅ Extracted Skills:")
    st.write(skills)

    if st.button("🔎 Find Matching Careers"):
        with st.spinner("Asking AI for recommendations..."):
            output = recommend_jobs(skills)
        st.subheader("💡 Career Suggestions:")
        st.markdown(output)