from app.agents.llm_resume_writer import generate_ai_resume_summary

result = generate_ai_resume_summary(
    "Sravani Koriginja",
    5,
    ["Python", "AWS", "FastAPI"],
    "DevOps"
)

print(result)