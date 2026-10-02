def check_integer(number: int) -> dict[str, bool]:
    """Return whether number is even, odd, or divisible by 3 and 5."""
    if isinstance(number, bool) or not isinstance(number, int):
        raise TypeError("number must be an integer")

    return {
        "even": number % 2 == 0,
        "odd": number % 2 != 0,
        "divisible_by_3": number % 3 == 0,
        "divisible_by_5": number % 5 == 0,
    }


def main() -> None:
    try:
        number = int(input("Enter an integer: "))
    except ValueError:
        print("Please enter a valid integer.")
        return

    results = check_integer(number)
    for check, passed in results.items():
        print(f"{check.replace('_', ' ')}: {'Yes' if passed else 'No'}")


if __name__ == "__main__":
    main()
    
