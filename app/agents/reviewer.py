import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel("gemini-2.5-flash")


def review_resume(resume_text):

    model = genai.GenerativeModel("gemini-2.5-flash")

    prompt = f"""
    Review this resume:
    {resume_text}
    """

    try:
        response = model.generate_content(prompt)

        return {
            "review": response.text
        }

    except Exception as e:
        return {
            "review": "Gemini quota exceeded",
            "error": str(e)
        }