def generate_resume_content(name, domain, experience, skills):

    headline = f"{domain} Professional"

    summary = (
        f"{name} is a {experience}+ years experienced "
        f"{domain} professional with expertise in "
        f"{', '.join(skills)}."
    )

    return {
        "headline": headline,
        "professional_summary": summary,
        "skills_section": skills
    }