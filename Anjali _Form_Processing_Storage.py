import re

data_store = []

def validate_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

def collect_data():
    name = input("Enter your full name: ")
    domain = input("Enter internship domain: ")
    email = input("Enter your email: ")
    date = input("Enter start date (e.g. 10 June 2025): ")

    if not validate_email(email):
        print("Invalid email format.")
        return

    entry = {
        "name": name,
        "domain": domain,
        "email": email,
        "date": date
    }

    data_store.append(entry)

    with open("form_data_saved.txt", "a") as file:
        file.write(f"{entry}\n")

    print("Data validated and saved (simulated Google Sheet)")

# Run the function
collect_data()