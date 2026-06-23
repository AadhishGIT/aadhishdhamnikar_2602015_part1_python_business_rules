def loan_eligibility(customer):

    score = customer["credit_score"]
    emi_ratio = customer["emi_ratio"]
    savings_percentage = customer["savings_percentage"]

    requested_amount = float(
        input("Requested Loan Amount: ")
    )

    if score >= 750 and emi_ratio < 30 and savings_percentage > 25:
        decision = "Approved"
        reason = "Excellent credit and financial profile."

    elif score < 600:
        decision = "Rejected"
        reason = "Poor credit score."

    else:
        decision = "Manual Review Required"
        reason = "Credit score is acceptable, but EMI-to-income ratio is high."

    # Print decision and a clear explanation for why it was made
    print("\nDecision:", decision)
    print("Reason:", reason)


def campaign_eligibility(customer):

    segment = customer["segment"]
    value = customer["value"]
    savings = customer["savings_percentage"]
    # Determine campaign and provide an explanation for the assignment
    if segment == "Premium" and value == "High Value":
        campaign = "Premium Upsell Campaign"
        reason = "Customer belongs to the Premium segment and is High Value, so upsell offers are suitable."

    elif savings > 20:
        campaign = "Loan Offer Campaign"
        reason = "Customer has high savings (>20%), indicating capacity to service a loan."

    elif value == "Medium Value":
        campaign = "Cashback Campaign"
        reason = "Customer is Medium Value; cashback incentives may increase engagement."

    else:
        campaign = "No Campaign"
        reason = "No campaign rules matched the customer's profile."

    print("\nCampaign:", campaign)
    print("Explanation:", reason)