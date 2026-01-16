"""
Scoops & Scripts - Ice Cream Shop Management System

Data structures used (as per requirements):
- Fixed Offerings (immutable): tuple
- Pricing Lookup (fast search): dict
- Serving Rules (immutable): tuple
- Toppings (unique, order doesn't matter): set
- Transaction History (running record): list
"""

from datetime import datetime


# 1) Fixed Offerings (signature flavors) - IMMUTABLE
SIGNATURE_FLAVORS = ("Vanilla", "Chocolate", "Strawberry")
# 2) Pricing Lookup - DICTIONARY for fast access
FLAVOR_PRICES = {
    "vanilla": 80,
    "chocolate": 90,
    "strawberry": 85,
}

# 3) Strict Serving Rules - IMMUTABLE
SERVING_TYPES = ("Cone", "Cup")

# Optional: Available toppings list (for display only)
AVAILABLE_TOPPINGS = {"nuts", "sprinkles", "choco chips", "caramel", "oreo", "honey"}


# 5) Transaction Tracking - LIST of completed orders
transactions = []


# -------- Utilities --------
def read_int(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.\n")


def read_float(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.\n")


def normalize(text: str) -> str:
    return text.strip().lower()


def choose_flavor() -> str:
    print("\nSignature Flavors:")
    for f in SIGNATURE_FLAVORS:
        print(f"- {f} (Rs {FLAVOR_PRICES[normalize(f)]}/scoop)")

    while True:
        flavor = input("Enter flavor: ").strip()
        key = normalize(flavor)

        if key in FLAVOR_PRICES:
            return key

        print("Invalid flavor. Please choose from the available signature flavors.\n")


def choose_serving() -> str:
    print("\nServing Types (fixed):", ", ".join(SERVING_TYPES))

    while True:
        serving = input("Enter serving type (Cone/Cup): ").strip()
        # normalize but keep original standard capitalization
        serving_norm = serving.strip().lower()

        if serving_norm == "cone":
            return "Cone"
        if serving_norm == "cup":
            return "Cup"

        print("Invalid serving type. Only Cone or Cup allowed.\n")


def choose_toppings() -> set:
    """
    Customers can choose multiple toppings.
    Must be unique, order doesn't matter -> use set.
    """
    print("\nAvailable toppings:", ", ".join(sorted(AVAILABLE_TOPPINGS)))
    print("Enter toppings separated by comma (or press Enter for none).")

    raw = input("Toppings: ").strip()
    if not raw:
        return set()

    toppings = {normalize(t) for t in raw.split(",") if t.strip()}

    # Optional validation (reject unknown toppings)
    unknown = toppings - AVAILABLE_TOPPINGS
    if unknown:
        print(f"These toppings are not available and will be ignored: {', '.join(sorted(unknown))}")
        toppings = toppings & AVAILABLE_TOPPINGS

    return toppings


def calculate_bill(flavor_key: str, scoops: int, toppings: set) -> float:
    """
    Pricing model:
    - Flavor price is per scoop
    - Each topping costs Rs 10 (example rule)
    """
    price_per_scoop = FLAVOR_PRICES[flavor_key]
    topping_price = 10

    base_cost = price_per_scoop * scoops
    toppings_cost = topping_price * len(toppings)

    return base_cost + toppings_cost


def place_order():
    flavor_key = choose_flavor()

    scoops = read_int("Enter number of scoops (1-5): ")
    while scoops < 1 or scoops > 5:
        print("Scoops must be between 1 and 5.\n")
        scoops = read_int("Enter number of scoops (1-5): ")

    serving = choose_serving()
    toppings = choose_toppings()

    total = calculate_bill(flavor_key, scoops, toppings)

    order = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "flavor": flavor_key.capitalize(),
        "scoops": scoops,
        "serving": serving,
        "toppings": sorted(toppings),  # store sorted list for readability
        "total_rs": total,
    }

    transactions.append(order)
    print("\nOrder successful!")
    print_receipt(order)


def print_receipt(order: dict):
    print("\n----- Receipt -----")
    print("Time     :", order["timestamp"])
    print("Flavor   :", order["flavor"])
    print("Scoops   :", order["scoops"])
    print("Serving  :", order["serving"])
    print("Toppings :", ", ".join(order["toppings"]) if order["toppings"] else "None")
    print(f"Total    : Rs {order['total_rs']:.2f}")
    print("-------------------\n")


def show_transactions():
    if not transactions:
        print("\nNo sales yet.\n")
        return

    print("\n----- Day Sales History -----")
    grand_total = 0.0
    for idx, t in enumerate(transactions, start=1):
        grand_total += t["total_rs"]
        toppings_text = ", ".join(t["toppings"]) if t["toppings"] else "None"
        print(
            f"{idx}. {t['timestamp']} | {t['flavor']} | {t['scoops']} scoop(s) | "
            f"{t['serving']} | Toppings: {toppings_text} | Rs {t['total_rs']:.2f}"
        )
    print(f"\nGrand Total Sales: Rs {grand_total:.2f}")
    print("----------------------------\n")


def price_lookup():
    print("\nPrice Lookup")
    flavor = input("Enter flavor name: ").strip()
    key = normalize(flavor)

    if key in FLAVOR_PRICES:
        print(f"{key.capitalize()} price is Rs {FLAVOR_PRICES[key]} per scoop.\n")
    else:
        print("Flavor not found. Available signature flavors are:",
              ", ".join(SIGNATURE_FLAVORS), "\n")


def main():
    print("Welcome to Scoops & Scripts - Management System")

    while True:
        print("Menu")
        print("1. Place Order")
        print("2. Price Lookup")
        print("3. View Transaction History")
        print("4. Exit\n")

        choice = input("Enter choice (1-4): ").strip()

        if choice == "1":
            place_order()
        elif choice == "2":
            price_lookup()
        elif choice == "3":
            show_transactions()
        elif choice == "4":
            print("Closing system. Goodbye.")
            break
        else:
            print("Invalid choice. Please select 1 to 4.\n")


if __name__ == "__main__":
    main()
