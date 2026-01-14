# import math_utils
# from math_utils import square
# print(square(6))          
# print(math_utils.cube(7))
# import calculate_result
# calculate_result.calculate_result()
import logging
from employee_utility import calculate_final_salary

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s"
)

def main():
    name = input("Enter employee name: ")
    designation = input("Enter designation (Coder / Designer / Manager): ")
    basic_salary = float(input("Enter basic salary: "))
    total_leaves = int(input("Enter total leaves taken (0 to 32): "))

    bonus, final_salary = calculate_final_salary(basic_salary, designation, total_leaves)

    print("\n----- Employee Salary Report -----")
    print(f"Employee Name : {name}")
    print(f"Designation   : {designation}")
    print(f"Basic Salary  : {basic_salary:.2f}")
    print(f"Leaves Taken  : {total_leaves}/32 (All Paid)")
    print(f"Bonus         : {bonus:.2f}")
    print(f"Final Salary  : {final_salary:.2f}")

if __name__ == "__main__":
    main()
