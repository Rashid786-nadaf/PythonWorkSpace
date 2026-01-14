# employee_utility.py

TOTAL_PAID_LEAVES = 32  # total leaves = paid leaves


def validate_leaves(total_leaves):
    """
    Employee cannot apply more than 32 leaves in a year.
    """
    if not (0 <= total_leaves <= TOTAL_PAID_LEAVES):
        raise ValueError(
            f"Invalid leave count. Allowed range: 0–{TOTAL_PAID_LEAVES} days."
        )


def calculate_bonus(basic_salary, designation):
    """
    Calculates bonus based on designation.
    """
    designation = designation.lower()

    bonus_percentage = {
        "coder": 0.10,
        "designer": 0.15,
        "manager": 0.05
    }

    return basic_salary * bonus_percentage.get(designation, 0.0)


def calculate_final_salary(basic_salary, designation, total_leaves):
    """
    Final salary = Basic + Bonus
    Leaves are validated but do not affect salary (all leaves are paid).
    """
    validate_leaves(total_leaves)

    bonus = calculate_bonus(basic_salary, designation)
    final_salary = basic_salary + bonus

    return bonus, final_salary
