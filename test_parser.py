# from resume_parser import extract_text_from_pdf

# text = extract_text_from_pdf("PRARABDHA NAMDEO.pdf")

# print(text[:500])

# from resume_parser import extract_text_from_pdf
# from skill_extractor import extract_skills


# text = extract_text_from_pdf("PRARABDHA NAMDEO.pdf")

# skills = extract_skills(text)

# print(skills)

# from resume_parser import extract_text_from_pdf
# from similarity import compute_similarity


# resume = extract_text_from_pdf("PRARABDHA NAMDEO.pdf")

# job_description = """
# Looking for a data scientist with python,
# machine learning, statistics and SQL experience
# """


# score = compute_similarity(resume, job_description)

# print("Match Score:", score)

from skill_extractor import extract_skills, missing_skills

resume_text = "I know python and sql"

job_description = """
Looking for python, sql, machine learning, statistics
"""

resume_skills = extract_skills(resume_text)

job_skills = extract_skills(job_description)

missing = missing_skills(resume_skills, job_skills)

print("Missing Skills:", missing)