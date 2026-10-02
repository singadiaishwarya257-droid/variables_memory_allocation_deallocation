"""Python operator topics:
1. Arithmetic operators
2. Assignment operators
3. Comparison operators
4. Logical operators
5. Identity operators
6. Membership operators
7. Bitwise operators
8. Ternary operators

task1:
    write calculator program ,which should return addition, subtraction ,multiplication,division,floor division,reminder.
"""

def calculate(first_number, second_number):
    if second_number == 0:
        raise ValueError("The second number must not be zero for division operations.")

    return {
        "addition": first_number + second_number,
        "subtraction": first_number - second_number,
        "multiplication": first_number * second_number,
        "division": first_number / second_number,
        "floor_division": first_number // second_number,
        "remainder": first_number % second_number,
    }


if __name__ == "__main__":
    try:
        first_number = float(input("Enter the first number: "))
        second_number = float(input("Enter the second number: "))
        results = calculate(first_number, second_number)
    except ValueError as error:
        print(error)
    else:
        for operation, result in results.items():
            print(f"{operation}: {result}")



