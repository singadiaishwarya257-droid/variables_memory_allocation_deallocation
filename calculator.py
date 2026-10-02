import operator as arithmetic


OPERATIONS = {
    "+": arithmetic.add,
    "-": arithmetic.sub,
    "*": arithmetic.mul,
    "/": arithmetic.truediv,
    "//": arithmetic.floordiv,
    "%": arithmetic.mod,
    "**": arithmetic.pow,
}


def calculate(a: float, operator: str, b: float) -> float:
    """Calculate a supported arithmetic operation on two numbers."""
    if operator not in OPERATIONS:
        raise ValueError(f"Invalid operator: {operator}")

    if operator in {"/", "//", "%"} and b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")

    return OPERATIONS[operator](a, b)


def main() -> None:
    try:
        a = float(input("Enter the first number: "))
        selected_operator = input("Enter an operator (+, -, *, /, //, %, **): ").strip()
        b = float(input("Enter the second number: "))
        result = calculate(a, selected_operator, b)
    except ZeroDivisionError as error:
        print(error)
        return
    except ValueError as error:
        print(error)
        return

    print(f"Result: {result}")


if __name__ == "__main__":
    main()
