# Test Cases - Business Rules Engine

## TC01 - Low Risk Customer

### Input

```text
Income = 100000
Expenses = 50000
EMI = 15000
Credit Score = 780
```

### Expected Result

```text
Risk Category = Low Risk
Customer Value = High Value
```

### Reason

Credit score is above 750 and EMI ratio is below 30%.

---

## TC02 - Medium Risk Customer

### Input

```text
Income = 70000
Expenses = 40000
EMI = 25000
Credit Score = 680
```

### Expected Result

```text
Risk Category = Medium Risk
Customer Value = Medium Value
```

### Reason

Credit score is above 650 and EMI ratio is below 50%.

---

## TC03 - High Risk Customer

### Input

```text
Income = 50000
Expenses = 30000
EMI = 30000
Credit Score = 550
```

### Expected Result

```text
Risk Category = High Risk
Customer Value = Medium Value
```

### Reason

Credit score is below 650.

---

## TC04 - Billing With Free Delivery

### Input

```text
Quantity = 2
Unit Price = 3000
Discount = 10%
GST = 18%
Delivery Charge = 200
```

### Expected Result

```text
Gross Amount = 6000
Discount Amount = 600
GST Amount = 972
Final Amount = 6372
Delivery Charge Applied = 0
```

### Reason

Subtotal exceeds free delivery threshold.

---

## TC05 - Billing With Delivery Charge

### Input

```text
Quantity = 2
Unit Price = 1000
Discount = 10%
GST = 18%
Delivery Charge = 100
```

### Expected Result

```text
Final Amount = 2224
Delivery Charge Applied = 100
```

### Reason

Subtotal is below free delivery threshold.

---

## TC06 - Loan Eligibility Approved

### Input

```text
Credit Score = 780
EMI Ratio = 15%
Savings Percentage = 50%
Requested Loan Amount = 500000
```

### Expected Result

```text
Decision = Approved
```

### Reason

Excellent credit score, low EMI ratio and high savings percentage.

---

## TC07 - Campaign Eligibility

### Input

```text
Segment = Premium
Income = 100000
```

### Expected Result

```text
Campaign = Premium Upsell Campaign
```

### Reason

Premium customer with High Value category.

---

## TC08 - Invalid Age

### Input

```text
Age = -5
```

### Expected Result

```text
Invalid age.
```

### Reason

Age cannot be negative or zero.

---

## TC09 - Invalid Credit Score

### Input

```text
Credit Score = 950
```

### Expected Result

```text
Credit score must be between 300 and 900.
```

### Reason

Credit score is outside valid range.

---

## TC10 - Invalid Quantity

### Input

```text
Quantity = -2
```

### Expected Result

```text
Value cannot be negative.
```

### Reason

Quantity must be a positive number.

---

## TC11 - Invalid Customer Segment

### Input

```text
Segment = Gold
```

### Expected Result

```text
Allowed values:
Standard
Premium
Enterprise
```

### Reason

Only predefined customer segments are accepted.

---

## TC12 - Loan Eligibility Rejected

### Input

```text
Credit Score = 550
EMI Ratio = 20%
Savings Percentage = 30%
```

### Expected Result

```text
Decision = Rejected
Reason = Poor credit score
```

### Reason

Credit score is below 600.
