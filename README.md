# SkillBridge AI

An AI-powered app that helps users discover better career paths by analyzing their resume and suggesting adjacent jobs with learning paths.

## Setup

1. Install dependencies:
```
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

2. Add your OpenAI API key to `job_recommender.py`.

3. Run the app:
```
streamlit run app.py
```