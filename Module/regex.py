# import re

# INDIAN_MOBILE_REGEX = r'^(?:\+91|91)?[6-9]\d{9}$'

# def is_valid_indian_mobile(number: str) -> bool:
#     return bool(re.fullmatch(INDIAN_MOBILE_REGEX, number))

# while True:
#     mobile = input("Enter Indian mobile number: ").strip()

#     if is_valid_indian_mobile(mobile):
#         print("Valid Indian mobile number")
#         break
#     else:
#         print("Invalid number. Please enter a valid Indian mobile number.")

import re

def validate_user_details(email, mobile, password):

    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    mobile_pattern = r'^[6-9]\d{9}$'
    password_pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'

    if not re.match(email_pattern, email):
        raise ValueError("Invalid email address")

    if not re.match(mobile_pattern, mobile):
        raise ValueError("Invalid Indian mobile number")

    if not re.match(password_pattern, password):
        raise ValueError("Password must be strong")

    return "All details are valid"

Result = validate_user_details(
    "rashidnadaf85@gmail.com",
    "7899001015", 
    "Rashid@786"
    )

print(Result)