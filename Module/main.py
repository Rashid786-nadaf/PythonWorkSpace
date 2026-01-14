# # import math_utils
# # from math_utils import square
# # print(square(6))          
# # print(math_utils.cube(7))
# # import calculate_result
# # calculate_result.calculate_result()
# import logging
# from employee_utility import calculate_final_salary

# logging.basicConfig(
#     level=logging.INFO,
#     format="%(asctime)s | %(levelname)s | %(name)s | %(message)s"
# )

# def main():
#     name = input("Enter employee name: ")
#     designation = input("Enter designation (Coder / Designer / Manager): ")
#     basic_salary = float(input("Enter basic salary: "))
#     total_leaves = int(input("Enter total leaves taken (0 to 32): "))

#     bonus, final_salary = calculate_final_salary(basic_salary, designation, total_leaves)

#     print("\n----- Employee Salary Report -----")
#     print(f"Employee Name : {name}")
#     print(f"Designation   : {designation}")
#     print(f"Basic Salary  : {basic_salary:.2f}")
#     print(f"Leaves Taken  : {total_leaves}/32 (All Paid)")
#     print(f"Bonus         : {bonus:.2f}")
#     print(f"Final Salary  : {final_salary:.2f}")

# if __name__ == "__main__":
#     main()

import logging
import re

from employee_utility import (
    calculate_final_salary,
    EmployeeUtilityError,
    InvalidLeavesError,
    InvalidSalaryError,
    InvalidDesignationError,
)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
)
logger = logging.getLogger(__name__)


def read_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")


def read_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter an integer.")


def main():
    name = input("Enter employee name: ").strip()
    if not re.fullmatch(r"[A-Za-z ]+", name):
        print("Invalid name. Only alphabets (A–Z, a–z) and spaces are allowed.")
    else:
        print("Valid name:", name)

    # Keep asking until we get valid salary/designation/leaves
    while True:
        try:
            designation = input("Enter designation (Coder/Designer/Manager): ")
            basic_salary = read_float("Enter basic salary: ")
            total_leaves = read_int("Enter total leaves taken (0 to 32): ")

            bonus, final_salary = calculate_final_salary(
                basic_salary, designation, total_leaves
            )
            break

        except (InvalidLeavesError, InvalidSalaryError, InvalidDesignationError) as err:
            logger.warning("Validation error for %s: %s", name, err)
            print(f"Error: {err}\nPlease try again.\n")

        except EmployeeUtilityError as err:
            # Any other known project errors
            logger.error("EmployeeUtilityError: %s", err)
            print(f"Error: {err}")
            return

        except Exception as err:
            # Unexpected errors (real bugs)
            logger.exception("Unexpected error")
            print("Unexpected error occurred:", err)
            return

    print("\n----- Employee Salary Report -----")
    print(f"Employee Name : {name}")
    print(f"Designation   : {designation}")
    print(f"Basic Salary  : {basic_salary:.2f}")
    print(f"Leaves Taken  : {total_leaves}/32 (All Paid)")
    print(f"Bonus         : {bonus:.2f}")
    print(f"Final Salary  : {final_salary:.2f}")


if __name__ == "__main__":
    main()
