import spacy

nlp = spacy.load("en_core_web_sm")

SKILLS = [

    # programming
    "python", "java", "c++", "javascript",

    # web
    "html", "css", "tailwind",

    # databases
    "sql", "mysql",

    # data science
    "machine learning", "deep learning",
    "statistics", "data analysis",

    # libraries
    "pandas", "numpy", "matplotlib", "seaborn",
    "scikit-learn", "tensorflow", "pytorch",

    # tools
    "git", "streamlit", "jupyter notebook",
    "power bi", "tableau"
]
def extract_skills(text):

    doc = nlp(text.lower())

    extracted_skills = []

    for skill in SKILLS:
        if skill in doc.text:
            extracted_skills.append(skill)

    return list(set(extracted_skills))

def missing_skills(resume_skills, job_skills):
    
    return list(set(job_skills) - set(resume_skills))