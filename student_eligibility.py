def check_eligibility(
    marks: float,
    attendance_percentage: float,
    backlog: bool,
) -> str:
    """Return whether a student meets all eligibility requirements."""
    if marks >= 60 and attendance_percentage >= 75 and backlog is False:
        return "Eligible"
    return "Not eligible"


def main() -> None:
    try:
        marks = float(input("Enter marks: "))
        attendance_percentage = float(input("Enter attendance percentage: "))
    except ValueError:
        print("Marks and attendance must be valid numbers.")
        return

    backlog_input = input("Does the student have any backlogs? (yes/no): ").strip().lower()
    if backlog_input not in {"yes", "no"}:
        print("Please enter yes or no for backlog status.")
        return

    backlog = backlog_input == "yes"
    print(check_eligibility(marks, attendance_percentage, backlog))


if __name__ == "__main__":
    main()
