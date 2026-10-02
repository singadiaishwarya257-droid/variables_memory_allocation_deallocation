def get_result(marks: float) -> str:
    """Return the result category for a student's marks."""
    if marks >= 75:
        return "Distinction"
    if marks >= 35:
        return "Pass"
    return "Fail"


def main() -> None:
    try:
        marks = float(input("Enter the student's marks: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    print(get_result(marks))


if __name__ == "__main__":
    main()
