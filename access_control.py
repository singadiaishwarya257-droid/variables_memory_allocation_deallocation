def check_access(age: int, has_id: bool, is_employee: bool) -> str:
    """Return the access decision based on age, ID, and employee status."""
    if (age >= 18 and has_id) or is_employee:
        return "Access granted"
    return "Access denied"


def read_yes_no(prompt: str) -> bool:
    """Read a yes/no answer and return it as a Boolean."""
    while True:
        answer = input(prompt).strip().lower()
        if answer in {"yes", "y"}:
            return True
        if answer in {"no", "n"}:
            return False
        print("Please enter yes or no.")


def main() -> None:
    try:
        age = int(input("Enter age: "))
    except ValueError:
        print("Please enter a valid whole-number age.")
        return

    has_id = read_yes_no("Do you have an ID? (yes/no): ")
    is_employee = read_yes_no("Are you an employee? (yes/no): ")

    print(check_access(age, has_id, is_employee))


if __name__ == "__main__":
    main()
