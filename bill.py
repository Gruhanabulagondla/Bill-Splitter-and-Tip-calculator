def calculate_bill(bill, tip_percent, people):
    tip = bill * tip_percent / 100
    total = bill + tip
    per_person = total / people
    return tip, total, per_person


def main():
    print("========== BILL SPLITTER & TIP CALCULATOR ==========")

    while True:
        try:
            bill = float(input("\nEnter bill amount: ₹"))

            if bill <= 0:
                print("Bill amount must be greater than 0.")
                continue

            tip_percent = float(input("Enter tip percentage: "))

            if tip_percent < 0:
                print("Tip percentage cannot be negative.")
                continue

            people = int(input("Enter number of people: "))

            if people <= 0:
                print("Number of people must be greater than 0.")
                continue

            tip, total, per_person = calculate_bill(
                bill, tip_percent, people
            )

            print("\n========== BILL DETAILS ==========")
            print(f"Bill Amount: ₹{bill:.2f}")
            print(f"Tip Amount: ₹{tip:.2f}")
            print(f"Total Bill: ₹{total:.2f}")
            print(f"Number of People: {people}")
            print(f"Amount Per Person: ₹{per_person:.2f}")

            break

        except ValueError:
            print("Please enter valid numbers.")


if __name__ == "__main__":
    main()