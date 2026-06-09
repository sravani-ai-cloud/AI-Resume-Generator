def analyze_profile(experience, skills):

    # Candidate Level

    if experience <= 2:
        level = "Entry Level"

    elif experience <= 6:
        level = "Mid Level"

    else:
        level = "Senior Level"

    # Domain Detection

    skills_lower = [skill.lower() for skill in skills]

    if any(skill in skills_lower for skill in
           ["aws", "terraform", "docker", "kubernetes"]):
        domain = "DevOps"

    elif any(skill in skills_lower for skill in
             ["sql", "power bi", "tableau"]):
        domain = "Data Analytics"

    elif any(skill in skills_lower for skill in
             ["java", "spring", "c#"]):
        domain = "Software Development"

    else:
        domain = "General IT"

    return {
        "candidate_level": level,
        "primary_domain": domain,
        "years_experience": experience
    }