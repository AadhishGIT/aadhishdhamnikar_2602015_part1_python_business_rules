from src.utils import (
    get_non_negative_number,
    get_positive_number,
    get_age,
    get_credit_score,
    get_segment
)


def customer_summary():

    while True:
        name = input("Customer Name: ").strip()
        if name:
            break
        print("Customer name cannot be empty.")

    age = get_age()

    while True:
        city = input("City: ").strip()
        if not city:
            print("City cannot be empty.")
            continue

        if not city.isalpha():
            print("City must contain only alphabets.")
            continue

        break

    income = get_positive_number("Monthly Income: ")
    expenses = get_positive_number("Monthly Expenses: ")
    emi = get_non_negative_number("Existing EMI: ")

    credit_score = get_credit_score()
    segment = get_segment()

    savings = income - expenses

    savings_percentage = (savings / income) * 100

    emi_ratio = (emi / income) * 100

    # Risk Rules
    if credit_score >= 750 and emi_ratio < 30:
        risk = "Low Risk"
    elif credit_score >= 650 and emi_ratio < 50:
        risk = "Medium Risk"
    else:
        risk = "High Risk"

    # Value Rules
    if income >= 100000:
        value = "High Value"
    elif income >= 50000:
        value = "Medium Value"
    else:
        value = "Low Value"

    result = {
        "name": name,
        "age": age,
        "city": city,
        "income": income,
        "expenses": expenses,
        "emi": emi,
        "credit_score": credit_score,
        "segment": segment,
        "savings": savings,
        "savings_percentage": round(savings_percentage, 2),
        "emi_ratio": round(emi_ratio, 2),
        "risk": risk,
        "value": value
    }

    printValues = {"savings": "Monthly Savings", "savings_percentage": "Savings Percentage", "emi_ratio": "EMI-to-income ratio", "risk": "Risk Category", "value": "Customer value category"}
    print("\nCustomer Summary")
    print("-" * 30)

    for k, v in result.items():
        if k in printValues:
            if isinstance(v, (int, float)):
                print(f"{printValues[k]}: {v:g}")
            else:
                print(f"{printValues[k]}: {v}")

    return result