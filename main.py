from fastapi import FastAPI, Header
from app.auth.auth_handler import verify_token
from app.models.login_request import LoginRequest
from app.auth.auth_handler import create_access_token
from app.models.resume_request import ResumeRequest
from app.agents.profile_analyzer import analyze_profile
from app.agents.ats_optimizer import optimize_ats
from app.agents.resume_writer import generate_resume_content
from app.agents.full_resume_generator import generate_full_resume
from app.agents.reviewer import review_resume

app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "Enterprise AI Resume Generator API Running"
    }

@app.post("/login")
def login(request: LoginRequest):

    if (
        request.username == "admin"
        and request.password == "password123"
    ):

        token = create_access_token(
            {"sub": request.username}
        )

        return {
            "access_token": token,
            "token_type": "bearer"
        }

    return {
        "message": "Invalid Credentials"
    }

@app.post("/generate-resume")
def generate_resume(
    request: ResumeRequest,
    authorization: str = Header(None)
):
    
    if not authorization:
        return {
            "message": "Authorization token missing"
        }

    token = authorization.replace(
        "Bearer ",
        ""
    )

    username = verify_token(token)

    if not username:
        return {
            "message": "Invalid token"
        }
    

    profile_data = analyze_profile(
        request.experience,
        request.skills
    )

    ats_data = optimize_ats(
        request.skills
    )

    ai_resume = generate_full_resume(
        request.name,
        request.experience,
        request.skills,
        profile_data["primary_domain"]
    )
    review_data = review_resume(
        ai_resume
    )

    resume_content = generate_resume_content(
        request.name,
        profile_data["primary_domain"],
        request.experience,
        request.skills
    )

    return {
        "candidate_name": request.name,
        "profile_analysis": profile_data,
        "ats_analysis": ats_data,
        "resume_content": resume_content,
        "ai_resume": ai_resume,
        "review_report": review_data,
        "skills": request.skills
}