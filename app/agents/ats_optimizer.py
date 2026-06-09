def optimize_ats(skills):

    required_keywords = [
        "AWS",
        "Terraform",
        "Docker",
        "Kubernetes",
        "CI/CD"
    ]

    missing_keywords = []

    for keyword in required_keywords:

        if keyword.lower() not in [
            skill.lower() for skill in skills
        ]:
            missing_keywords.append(keyword)

    ats_score = int(
        ((len(required_keywords) -
          len(missing_keywords))
         / len(required_keywords))
        * 100
    )

    return {
        "ats_score": ats_score,
        "missing_keywords": missing_keywords
    }