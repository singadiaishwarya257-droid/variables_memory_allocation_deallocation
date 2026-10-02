def is_valid_user(username: str, password: str) -> bool:
    """Return True only for the specified username and password."""
    return username == "admin" and password == "python123"


def main() -> None:
    username = input("Enter username: ")
    password = input("Enter password: ")

    if is_valid_user(username, password):
        print("Valid user")
    else:
        print("Invalid user")


if __name__ == "__main__":
    main()
