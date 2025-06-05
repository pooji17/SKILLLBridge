import fitz  # PyMuPDF
import spacy
from spacy.cli import download

# Safe loading of spaCy model with fallback
try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    download("en_core_web_sm")
    nlp = spacy.load("en_core_web_sm")

# You can expand this list as needed
KNOWN_SKILLS = [
    "Python", "Excel", "Java", "JavaScript", "SQL", "Data Analysis",
    "Project Management", "Customer Service", "C++", "Communication",
    "AWS", "Machine Learning"
]

def extract_text_from_pdf(file):
    doc = fitz.open(stream=file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def extract_skills(text):
    doc = nlp(text)
    found = set()
    for token in doc:
        if token.text in KNOWN_SKILLS_
