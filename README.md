# aadhishdhamnikar_2602015_part1_python_business_rules

# Python Business Rules Engine

## Student Information

- Student Name: Aadhish Dhamnikar
- Student ID: 2602015

---

## Assignment Title

Business Rules Engine - Part 1

---

## Problem Summary

This project is a menu-driven Python command-line application developed to help a business team:

1. Evaluate customer financial profiles
2. Calculate product billing amounts
3. Check loan eligibility
4. Determine campaign eligibility
5. Handle invalid inputs through proper validation

The application is implemented using multiple Python modules and follows the required folder structure.

---

## Features Implemented

### Feature 1: Customer Profile and Financial Summary

Accepts:

- Customer Name
- Age
- City
- Monthly Income
- Monthly Expenses
- Existing EMI Amount
- Credit Score
- Customer Segment

Calculates:

- Monthly Savings
- Savings Percentage
- EMI-to-Income Ratio
- Risk Category
- Customer Value Category

---

### Feature 2: Product Billing Calculator

Accepts:

- Product Name
- Product Category
- Quantity
- Unit Price
- Discount Percentage
- GST Percentage
- Delivery Charge

Calculates:

- Gross Amount
- Discount Amount
- Amount After Discount
- GST Amount
- Delivery Charge Applied
- Final Payable Amount

Additional Rule:

- Delivery charge is waived when the payable amount exceeds the predefined threshold.

---

### Feature 3: Loan Eligibility Decision

Checks loan eligibility using:

- Age
- Monthly Income
- Existing EMI
- Credit Score
- Savings Percentage
- Requested Loan Amount

Possible Results:

- Approved
- Rejected
- Manual Review Required

The reason for the decision is also displayed.

---

### Feature 4: Campaign Eligibility

Assigns customers to one of the following campaigns:

- Premium Upsell Campaign
- Loan Offer Campaign
- Cashback Campaign
- No Campaign

Campaign assignment is based on:

- Customer Segment
- Savings Percentage
- Customer Value Category

---

### Feature 5: Input Validation and Error Handling

The application validates:

- Age
- Income
- Expenses
- EMI
- Credit Score
- Quantity
- Discount Percentage
- GST Percentage
- Customer Segment

The application does not crash when invalid input is entered and asks the user to re-enter valid values.

---

# Business Rules Used

## Risk Category Rules

### Low Risk

- Credit Score >= 750
- EMI Ratio < 30%

### Medium Risk

- Credit Score >= 650
- EMI Ratio < 50%

### High Risk

- All remaining cases

---

## Customer Value Rules

### High Value

Monthly Income >= 100000

### Medium Value

Monthly Income >= 50000 and < 100000

### Low Value

Monthly Income < 50000

---

## Loan Eligibility Rules

### Approved

- Credit Score >= 750
- EMI Ratio < 30%
- Savings Percentage > 25%

### Rejected

- Credit Score < 600

### Manual Review Required

- All other cases

---

## Campaign Eligibility Rules

### Premium Upsell Campaign

- Customer Segment = Premium
- Customer Value Category = High Value

### Loan Offer Campaign

- Savings Percentage > 20%

### Cashback Campaign

- Customer Value Category = Medium Value

### No Campaign

- All remaining customers

---

## Project Structure

```text
studentname_studentid_part1_python_business_rules/

├── README.md
├── main.py
├── src/
│   ├── __init__.py
│   ├── customer.py
│   ├── billing.py
│   ├── eligibility.py
│   └── utils.py
├── outputs/
│   ├── sample_output.txt
│   └── screenshots/
└── tests/
    └── test_cases.md
```

---

## File Description

### main.py

Controls the application menu and calls functions from the src modules.

### customer.py

Contains customer profile and financial summary logic.

### billing.py

Contains product billing calculation logic.

### eligibility.py

Contains loan eligibility and campaign eligibility logic.

### utils.py

Contains reusable validation functions and constants.

---

## How To Run The Program

### Step 1

Open Terminal or Command Prompt.

### Step 2

Navigate to the project directory.

```bash
cd studentname_studentid_part1_python_business_rules
```

### Step 3

Run the application.

```bash
python main.py
```

or

```bash
python3 main.py
```

---

## Sample Input

```text
Customer Name: John Smith
Age: 32
City: Mumbai
Monthly Income: 100000
Monthly Expenses: 50000
Existing EMI: 15000
Credit Score: 780
Segment: Premium
```

---

## Sample Output

```text
Customer Summary

Monthly Savings: 50000
Savings Percentage: 50%

EMI Ratio: 15%

Risk Category: Low Risk

Customer Value Category: High Value
```

---

## Screenshots

Add screenshots of:

1. Customer Profile Summary
2. Billing Calculator Output
3. Loan Eligibility Output
4. Campaign Eligibility Output
5. Input Validation Example

Store screenshots inside:

```text
outputs/screenshots/
```

---

## Assumptions Made

1. Monthly income is greater than zero.
2. Monthly expenses cannot be negative.
3. Existing EMI cannot be negative.
4. Credit score must be between 300 and 900.
5. Quantity must be greater than zero.
6. Discount percentage must be between 0 and 100.
7. GST percentage cannot be negative.
8. Delivery charge cannot be negative.
9. Customer segment must be one of:
   - Standard
   - Premium
   - Enterprise
10. Free delivery threshold is fixed at 5000.

---

## Technologies Used

- Python 3
- Functions
- Loops
- Conditional Statements
- Constants
- Input Validation
- Modular Programming

---

## Conclusion

This project demonstrates the implementation of business rules using Python through a modular, menu-driven application. It provides customer analysis, billing calculations, loan eligibility checks, campaign assignment, and robust input validation while following software engineering best practices.
