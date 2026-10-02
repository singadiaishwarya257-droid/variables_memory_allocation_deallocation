def calculate_discount(purchase_amount: float) -> tuple[float, float]:
    """Return the discount amount and final payable amount."""
    if purchase_amount < 0:
        raise ValueError("Purchase amount cannot be negative.")

    if purchase_amount >= 5000:
        discount_rate = 0.20
    elif purchase_amount >= 3000:
        discount_rate = 0.10
    else:
        discount_rate = 0.05

    discount_amount = round(purchase_amount * discount_rate, 2)
    payable_amount = round(purchase_amount - discount_amount, 2)
    return discount_amount, payable_amount


def main() -> None:
    try:
        purchase_amount = float(input("Enter the purchase amount in rupees: "))
        discount_amount, payable_amount = calculate_discount(purchase_amount)
    except ValueError as error:
        print(error)
        return

    print(f"Discount amount: Rs. {discount_amount:.2f}")
    print(f"Final payable amount: Rs. {payable_amount:.2f}")


if __name__ == "__main__":
    main()
