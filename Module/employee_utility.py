# """
# employee_utility.py

# Utility module for employee salary calculations.
# Includes leave validation and designation-based bonus.
# """

# import logging

# logger = logging.getLogger(__name__)

# TOTAL_PAID_LEAVES = 32  # total leaves = paid leaves (no salary deduction)


# def validate_leaves(total_leaves: int) -> None:
#     """Validate leave count (0–32)."""
#     logger.debug("Validating leaves: total_leaves=%d", total_leaves)

#     if not 0 <= total_leaves <= TOTAL_PAID_LEAVES:
#         logger.warning("Leave validation failed: total_leaves=%d", total_leaves)
#         raise ValueError(f"Leaves must be between 0 and {TOTAL_PAID_LEAVES} days.")

#     logger.info("Leave validation passed: total_leaves=%d", total_leaves)


# def calculate_bonus(basic_salary: float, designation: str) -> float:
#     """Calculate bonus based on designation."""
#     designation_key = designation.strip().lower()
#     logger.debug(
#         "Calculating bonus: basic_salary=%.2f designation=%s",
#         basic_salary,
#         designation_key,
#     )

#     bonus_percentage = {
#         "coder": 0.10,
#         "designer": 0.15,
#         "manager": 0.05,
#     }.get(designation_key, 0.0)

#     if bonus_percentage == 0.0:
#         logger.warning("Unknown designation, bonus set to 0: designation=%s", designation)

#     bonus = basic_salary * bonus_percentage
#     logger.info(
#         "Bonus calculated: designation=%s bonus_percentage=%.2f bonus=%.2f",
#         designation_key,
#         bonus_percentage,
#         bonus,
#     )
#     return bonus


# def calculate_final_salary(basic_salary: float, designation: str, total_leaves: int):
#     """
#     Final salary = Basic + Bonus
#     Leaves are validated but do not affect salary (all 32 leaves are paid).
#     """
#     logger.info("Starting salary calculation")

#     validate_leaves(total_leaves)
#     bonus = calculate_bonus(basic_salary, designation)
#     final_salary = basic_salary + bonus

#     logger.info(
#         "Salary calculation completed: basic=%.2f bonus=%.2f final=%.2f",
#         basic_salary,
#         bonus,
#         final_salary,
#     )
#     return bonus, final_salary

"""
employee_utility.py

Business logic for employee salary calculation.
Rules:
- Total leaves allowed: 0 to 32
- Total leaves are paid leaves (no salary deduction for leaves)
- Bonus depends on designation:
  - coder: 10%
  - designer: 15%
  - manager: 5%
"""

import logging

logger = logging.getLogger(__name__)

TOTAL_PAID_LEAVES = 32
BONUS_RATES = {
    "coder": 0.10,
    "designer": 0.15,
    "manager": 0.05,
}


# ----- Custom Exceptions -----
class EmployeeUtilityError(Exception):
    """Base exception for employee utility errors."""


class InvalidLeavesError(EmployeeUtilityError):
    """Raised when leaves are outside allowed range."""


class InvalidSalaryError(EmployeeUtilityError):
    """Raised when salary is invalid."""


class InvalidDesignationError(EmployeeUtilityError):
    """Raised when designation is not supported."""


# ----- Validations -----
def validate_salary(basic_salary: float) -> None:
    """Validate salary input."""
    logger.debug("Validating salary: basic_salary=%.2f", basic_salary)

    if basic_salary <= 0:
        logger.warning("Invalid salary: basic_salary=%.2f", basic_salary)
        raise InvalidSalaryError("Basic salary must be greater than 0.")


def validate_leaves(total_leaves: int) -> None:
    """Validate leave input."""
    logger.debug("Validating leaves: total_leaves=%d", total_leaves)

    if not 0 <= total_leaves <= TOTAL_PAID_LEAVES:
        logger.warning("Invalid leaves: total_leaves=%d", total_leaves)
        raise InvalidLeavesError(
            f"Leaves must be between 0 and {TOTAL_PAID_LEAVES} days."
        )


def validate_designation(designation: str) -> str:
    """Validate designation and return normalized key."""
    if designation is None:
        raise InvalidDesignationError("Designation cannot be empty.")

    designation_key = designation.strip().lower()
    logger.debug("Validating designation: designation=%s", designation_key)

    if designation_key not in BONUS_RATES:
        logger.warning("Invalid designation: %s", designation)
        raise InvalidDesignationError(
            "Designation must be one of: Coder, Designer, Manager."
        )

    return designation_key


# ----- Calculations -----
def calculate_bonus(basic_salary: float, designation: str) -> float:
    """Calculate bonus amount."""
    designation_key = validate_designation(designation)
    bonus = basic_salary * BONUS_RATES[designation_key]

    logger.info(
        "Bonus calculated: designation=%s bonus=%.2f",
        designation_key,
        bonus,
    )
    return bonus


def calculate_final_salary(basic_salary: float, designation: str, total_leaves: int):
    """
    Final salary = Basic + Bonus
    Leaves are validated but do not affect salary (all leaves are paid).
    Returns (bonus, final_salary).
    """
    validate_salary(basic_salary)
    validate_leaves(total_leaves)

    bonus = calculate_bonus(basic_salary, designation)
    final_salary = basic_salary + bonus

    logger.info(
        "Final salary calculated: basic=%.2f bonus=%.2f final=%.2f leaves=%d",
        basic_salary,
        bonus,
        final_salary,
        total_leaves,
    )
    return bonus, final_salary
