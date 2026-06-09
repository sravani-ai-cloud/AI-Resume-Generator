import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel("gemini-2.5-flash")


def generate_ai_resume_summary(
    name,
    experience,
    skills,
    domain
):

    prompt = f"""
    Create a professional resume summary.

    Candidate Name: {name}
    Experience: {experience} years
    Domain: {domain}
    Skills: {', '.join(skills)}

    Generate a concise professional summary suitable for a resume.
    """

    response = model.generate_content(prompt)

    return response.text