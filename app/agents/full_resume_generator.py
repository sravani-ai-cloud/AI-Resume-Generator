import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel("gemini-2.5-flash")


def generate_full_resume(
    name,
    experience,
    skills,
    domain
):

    prompt = f"""
Create a professional resume.

Candidate Name: {name}
Experience: {experience} years
Domain: {domain}
Skills: {', '.join(skills)}

Generate:

1. Professional Headline
2. Professional Summary
3. Technical Skills Section
4. Project Section
5. Experience Section

Return in professional resume format.
"""

    response = model.generate_content(prompt)

    return response.text