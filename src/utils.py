SEGMENTS = ["Standard", "Premium", "Enterprise"]

FREE_DELIVERY_THRESHOLD = 5000


def get_positive_number(message):
    while True:
        try:
            user_input = input(message).strip()

            if not user_input:
                print("Input cannot be empty.")
                continue

            value = float(user_input)

            if value == 0:
                print("Value cannot be zero.")
                continue

            if value < 0:
                print("Value cannot be negative.")
                continue

            return value

        except ValueError:
            print("Enter valid number.")


def get_non_negative_number(message):
    while True:
        try:
            user_input = input(message).strip()

            if not user_input:
                print("Input cannot be empty.")
                continue

            value = float(user_input)

            if value < 0:
                print("Value cannot be negative.")
                continue

            return value

        except ValueError:
            print("Enter valid number.")


def get_percentage(message):
    while True:
        try:
            user_input = input(message).strip()

            if not user_input:
                print("Input cannot be empty.")
                continue

            value = float(user_input)

            if value < 0:
                print("Percentage must be greater than 0.")
                continue

            if value > 100:
                print("Percentage cannot be greater than 100.")
                continue

            return value

        except ValueError:
            print("Enter valid number.")


def get_age():
    while True:
        try:
            user_input = input("Age: ").strip()

            if not user_input:
                print("Age cannot be empty.")
                continue

            age = float(user_input)

            if age <= 0:
                print("Age must be greater than zero.")
                continue

            if age != int(age):
                print("Age must be a whole number, not a decimal.")
                continue

            return int(age)

        except ValueError:
            print("Enter valid number.")


def get_credit_score():
    while True:
        try:
            user_input = input("Credit Score (300-900): ").strip()

            if not user_input:
                print("Credit score cannot be empty.")
                continue

            score = int(user_input)

            if 300 <= score <= 900:
                return score

            print("Credit score must be between 300 and 900.")

        except ValueError:
            print("Enter valid number.")


def get_segment():
    while True:
        segment = input("Segment: ").strip().title()

        if not segment:
            print("Segment cannot be empty.")
            continue

        if segment in SEGMENTS:
            return segment

        print("Allowed values:", SEGMENTS)