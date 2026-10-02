REQUIRED_SKILLS = ["python", "sql", "git", "HTML"]


def check_skill(skill_name: str) -> str:
    """Check whether a skill is in the required skills list."""
    available_skills = {skill.casefold() for skill in REQUIRED_SKILLS}
    if skill_name.strip().casefold() in available_skills:
        return "Skill available"
    return "Skill not available"


def main() -> None:
    skill_name = input("Enter a skill name: ")
    print(check_skill(skill_name))


if __name__ == "__main__":
    main()
