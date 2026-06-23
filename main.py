from src.customer import customer_summary
from src.billing import billing_calculator
from src.eligibility import (
    loan_eligibility,
    campaign_eligibility
)

customer_data = None

while True:

    print("\n==== BUSINESS RULE ENGINE ====")
    print("1. Customer Profile")
    print("2. Billing Calculator")
    print("3. Loan Eligibility")
    print("4. Campaign Eligibility")
    print("5. Exit")

    choice = input("Choice: ").strip()

    if not choice:
        print("Choice cannot be empty.")
        continue

    if choice == "1":
        customer_data = customer_summary()

    elif choice == "2":
        billing_calculator()

    elif choice == "3":
        if customer_data:
            loan_eligibility(customer_data)
        else:
            print("Create customer first.")

    elif choice == "4":
        if customer_data:
            campaign_eligibility(customer_data)
        else:
            print("Create customer first.")

    elif choice == "5":
        print("Goodbye")
        break

    else:
        print("Invalid choice")