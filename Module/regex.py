import re

INDIAN_MOBILE_REGEX = r'^(?:\+91|91)?[6-9]\d{9}$'

def is_valid_indian_mobile(number: str) -> bool:
    return bool(re.fullmatch(INDIAN_MOBILE_REGEX, number))

while True:
    mobile = input("Enter Indian mobile number: ").strip()

    if is_valid_indian_mobile(mobile):
        print("Valid Indian mobile number")
        break
    else:
        print("Invalid number. Please enter a valid Indian mobile number.")
