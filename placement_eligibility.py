def assess_candidate(
    age: int,
    marks: float,
    attendance: float,
    experience: int,
    has_backlog: bool,
) -> tuple[bool, str]:
    """Return placement eligibility and the candidate's experience category."""
    if age < 0 or experience < 0:
        raise ValueError("Age and experience cannot be negative.")

    is_eligible = marks >= 60 and attendance >= 75 and has_backlog is False

    if experience == 0:
        category = "Fresher"
    elif 1 <= experience <= 2:
        category = "Junior"
    else:
        category = "Experienced"

    return is_eligible, category


def main() -> None:
    try:
        age = int(input("Enter age: "))
        marks = float(input("Enter marks: "))
        attendance = float(input("Enter attendance percentage: "))
        experience = int(input("Enter years of experience: "))
    except ValueError:
        print("Please enter valid numeric values.")
        return

    backlog_answer = input("Does the candidate have a backlog? (yes/no): ").strip().lower()
    if backlog_answer not in {"yes", "no"}:
        print("Please answer yes or no for backlog status.")
        return

    has_backlog = backlog_answer == "yes"

    try:
        is_eligible, category = assess_candidate(
            age,
            marks,
            attendance,
            experience,
            has_backlog,
        )
    except ValueError as error:
        print(error)
        return

    eligibility = "Yes" if is_eligible else "No"
    print(f"1) Placement eligible: {eligibility}")
    print(f"2) Candidate category: {category}")


if __name__ == "__main__":
    main()
