import openai
import streamlit as st

# Read API key securely from Streamlit secrets
openai.api_key = st.secrets["OPENAI_API_KEY"]

def recommend_jobs(skills):
    if not skills:
        return "❗️No skills were provided. Please upload a resume with recognizable skills."

    prompt = f"""
    I have these skills: {', '.join(skills)}.
    Suggest 3 adjacent or emerging career paths I could qualify for with minimal upskilling.
    For each job:
    - Explain why it's a match
    - List missing skills
    - Recommend specific online courses
    """

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7
        )
        return response['choices'][0]['message']['content']

    except Exception as e:
        return f"❌ An error occurred while fetching recommendations:\n\n{str(e)}"
