from src.utils import get_positive_number, get_percentage

FREE_DELIVERY_THRESHOLD = 5000


def billing_calculator():

    while True:
        product = input("Product Name: ").strip()
        if product:
            break
        print("Product name cannot be empty.")

    while True:
        category = input("Category: ").strip()
        if category:
            break
        print("Category cannot be empty.")

    quantity = get_positive_number("Quantity: ")
    unit_price = get_positive_number("Unit Price: ")

    discount = get_percentage("Discount %: ")
    gst = get_percentage("GST %: ")

    delivery = get_positive_number("Delivery Charge: ")

    gross = quantity * unit_price

    discount_amount = gross * discount / 100

    after_discount = gross - discount_amount

    gst_amount = after_discount * gst / 100

    subtotal = after_discount + gst_amount

    if subtotal > FREE_DELIVERY_THRESHOLD:
        delivery_applied = 0
    else:
        delivery_applied = delivery

    final_amount = subtotal + delivery_applied

    print("\nBilling Summary")
    print("-" * 30)

    print(f"Gross Amount: {round(gross, 2):g}")
    print(f"Discount Amount: {round(discount_amount, 2):g}")
    print(f"Amount after Discount: {round(after_discount, 2):g}")
    print(f"GST Amount: {round(gst_amount, 2):g}")
    print(f"Delivery charge applied: {round(delivery_applied, 2):g}")
    print(f"Final payable amount: {round(final_amount, 2):g}")