from app.agents.full_resume_generator import generate_full_resume

result = generate_full_resume(
    "Sravani Koriginja",
    5,
    ["Python", "AWS", "FastAPI"],
    "DevOps"
)

print(result)