"""
employee_utility.py

Utility module for employee salary calculations.
Includes leave validation and designation-based bonus.
"""

import logging

logger = logging.getLogger(__name__)

TOTAL_PAID_LEAVES = 32  # total leaves = paid leaves (no salary deduction)


def validate_leaves(total_leaves: int) -> None:
    """Validate leave count (0–32)."""
    logger.debug("Validating leaves: total_leaves=%d", total_leaves)

    if not 0 <= total_leaves <= TOTAL_PAID_LEAVES:
        logger.warning("Leave validation failed: total_leaves=%d", total_leaves)
        raise ValueError(f"Leaves must be between 0 and {TOTAL_PAID_LEAVES} days.")

    logger.info("Leave validation passed: total_leaves=%d", total_leaves)


def calculate_bonus(basic_salary: float, designation: str) -> float:
    """Calculate bonus based on designation."""
    designation_key = designation.strip().lower()
    logger.debug(
        "Calculating bonus: basic_salary=%.2f designation=%s",
        basic_salary,
        designation_key,
    )

    bonus_percentage = {
        "coder": 0.10,
        "designer": 0.15,
        "manager": 0.05,
    }.get(designation_key, 0.0)

    if bonus_percentage == 0.0:
        logger.warning("Unknown designation, bonus set to 0: designation=%s", designation)

    bonus = basic_salary * bonus_percentage
    logger.info(
        "Bonus calculated: designation=%s bonus_percentage=%.2f bonus=%.2f",
        designation_key,
        bonus_percentage,
        bonus,
    )
    return bonus


def calculate_final_salary(basic_salary: float, designation: str, total_leaves: int):
    """
    Final salary = Basic + Bonus
    Leaves are validated but do not affect salary (all 32 leaves are paid).
    """
    logger.info("Starting salary calculation")

    validate_leaves(total_leaves)
    bonus = calculate_bonus(basic_salary, designation)
    final_salary = basic_salary + bonus

    logger.info(
        "Salary calculation completed: basic=%.2f bonus=%.2f final=%.2f",
        basic_salary,
        bonus,
        final_salary,
    )
    return bonus, final_salary
