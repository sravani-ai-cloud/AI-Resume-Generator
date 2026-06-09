from app.agents.reviewer import review_resume

sample_resume = """
DevOps Engineer

Experienced in AWS and Python.
"""

result = review_resume(sample_resume)

print(result)