from dataclasses import dataclass
from typing import Dict, List, Optional


# ----------------------------
# Data Models
# ----------------------------

@dataclass(frozen=True)
class Food:
    id: int
    name: str
    category: str
    price: float


@dataclass
class CartItem:
    food: Food
    qty: int

    @property
    def line_total(self) -> float:
        return self.food.price * self.qty


class Cart:
    def __init__(self) -> None:
        # key = food_id, value = CartItem
        self._items: Dict[int, CartItem] = {}

    def add(self, food: Food, qty: int = 1) -> None:
        if qty <= 0:
            raise ValueError("Quantity must be greater than 0.")
        if food.id in self._items:
            self._items[food.id].qty += qty
        else:
            self._items[food.id] = CartItem(food=food, qty=qty)

    def update_qty(self, food_id: int, qty: int) -> None:
        if food_id not in self._items:
            raise KeyError("Item not found in cart.")
        if qty <= 0:
            # remove if qty is 0 or negative
            del self._items[food_id]
        else:
            self._items[food_id].qty = qty

    def remove(self, food_id: int) -> None:
        if food_id in self._items:
            del self._items[food_id]

    def clear(self) -> None:
        self._items.clear()

    @property
    def items(self) -> List[CartItem]:
        return list(self._items.values())

    @property
    def total_bill(self) -> float:
        return sum(item.line_total for item in self._items.values())

    def is_empty(self) -> bool:
        return len(self._items) == 0


class Menu:
    def __init__(self, outlet_name: str, outlet_id: str, foods: List[Food]) -> None:
        self.outlet_name = outlet_name
        self.outlet_id = outlet_id
        self._foods_by_id: Dict[int, Food] = {f.id: f for f in foods}

    @property
    def foods(self) -> List[Food]:
        return list(self._foods_by_id.values())

    def get_food(self, food_id: int) -> Optional[Food]:
        return self._foods_by_id.get(food_id)

    def print_menu(self) -> None:
        print("\n" + "=" * 60)
        print(f"Pizza Hut Menu | Outlet: {self.outlet_name} (ID: {self.outlet_id})")
        print("=" * 60)
        print(f"{'ID':<5} {'Item':<28} {'Category':<15} {'Price (₹)':>10}")
        print("-" * 60)
        for f in sorted(self.foods, key=lambda x: x.id):
            print(f"{f.id:<5} {f.name:<28} {f.category:<15} {f.price:>10.2f}")
        print("=" * 60)


# ----------------------------
# Helper Input Functions
# ----------------------------

def read_int(prompt: str, min_value: int = None, max_value: int = None) -> int:
    while True:
        raw = input(prompt).strip()
        try:
            val = int(raw)
            if min_value is not None and val < min_value:
                print(f"Please enter a number >= {min_value}.")
                continue
            if max_value is not None and val > max_value:
                print(f"Please enter a number <= {max_value}.")
                continue
            return val
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def read_yes_no(prompt: str) -> bool:
    while True:
        ans = input(prompt).strip().lower()
        if ans in ("y", "yes"):
            return True
        if ans in ("n", "no"):
            return False
        print("Please type Y/Yes or N/No.")


# ----------------------------
# UI / Printing
# ----------------------------

def print_cart(cart: Cart) -> None:
    print("\n" + "=" * 60)
    print("CART")
    print("=" * 60)

    if cart.is_empty():
        print("Your cart is empty.")
        print("=" * 60)
        return

    print(f"{'ID':<5} {'Item':<28} {'Qty':>5} {'Price (₹)':>10} {'Total (₹)':>10}")
    print("-" * 60)
    for item in sorted(cart.items, key=lambda x: x.food.id):
        print(
            f"{item.food.id:<5} "
            f"{item.food.name:<28} "
            f"{item.qty:>5} "
            f"{item.food.price:>10.2f} "
            f"{item.line_total:>10.2f}"
        )
    print("-" * 60)
    print(f"{'TOTAL BILL (₹)':>49} {cart.total_bill:>10.2f}")
    print("=" * 60)


def print_invoice(menu: Menu, cart: Cart) -> None:
    print("\n" + "#" * 60)
    print("ORDER CONFIRMATION / INVOICE")
    print("#" * 60)
    print(f"Outlet: {menu.outlet_name} (ID: {menu.outlet_id})")
    print("-" * 60)

    print(f"{'Item':<30} {'Qty':>5} {'Unit (₹)':>10} {'Line (₹)':>12}")
    print("-" * 60)
    for item in sorted(cart.items, key=lambda x: x.food.id):
        print(
            f"{item.food.name:<30} "
            f"{item.qty:>5} "
            f"{item.food.price:>10.2f} "
            f"{item.line_total:>12.2f}"
        )
    print("-" * 60)
    print(f"{'TOTAL AMOUNT (₹)':>47} {cart.total_bill:>12.2f}")
    print("#" * 60)
    print("Thank you for ordering from Pizza Hut.\n")


# ----------------------------
# Main Application
# ----------------------------

def run_app() -> None:
    # You can customize these items as needed
    menu = Menu(
        outlet_name="Pizza Hut - MG Road",
        outlet_id="PH-MG-001",
        foods=[
            Food(1, "Margherita", "Pizza", 199.00),
            Food(2, "Farmhouse", "Pizza", 349.00),
            Food(3, "Peppy Paneer", "Pizza", 369.00),
            Food(4, "Chicken Tikka", "Pizza", 429.00),
            Food(5, "Garlic Bread", "Sides", 149.00),
            Food(6, "Cheesy Dip", "Sides", 59.00),
            Food(7, "Coke (500ml)", "Beverage", 75.00),
            Food(8, "Brownie", "Dessert", 129.00),
        ],
    )

    cart = Cart()

    while True:
        print("\n" + "=" * 60)
        print("PIZZA HUT FOOD ORDERING APP")
        print("=" * 60)
        print("1) View Menu")
        print("2) Add Item to Cart")
        print("3) View Cart")
        print("4) Update Cart Item Quantity")
        print("5) Remove Item from Cart")
        print("6) Place Order")
        print("7) Exit")
        print("=" * 60)

        choice = read_int("Choose an option (1-7): ", 1, 7)

        if choice == 1:
            menu.print_menu()

        elif choice == 2:
            menu.print_menu()
            food_id = read_int("Enter Food ID to add: ", 1)
            food = menu.get_food(food_id)
            if not food:
                print("Invalid Food ID. Please try again.")
                continue
            qty = read_int("Enter quantity: ", 1)
            cart.add(food, qty)
            print(f"Added: {food.name} x {qty}")

        elif choice == 3:
            print_cart(cart)

        elif choice == 4:
            if cart.is_empty():
                print("Cart is empty. Nothing to update.")
                continue
            print_cart(cart)
            food_id = read_int("Enter Food ID to update quantity: ", 1)
            qty = read_int("Enter new quantity (0 to remove): ", 0)
            try:
                cart.update_qty(food_id, qty)
                if qty == 0:
                    print("Item removed from cart.")
                else:
                    print("Quantity updated successfully.")
            except KeyError:
                print("That item is not in your cart.")

        elif choice == 5:
            if cart.is_empty():
                print("Cart is empty. Nothing to remove.")
                continue
            print_cart(cart)
            food_id = read_int("Enter Food ID to remove: ", 1)
            cart.remove(food_id)
            print("Item removed (if it existed).")

        elif choice == 6:
            if cart.is_empty():
                print("Cart is empty. Add items before placing an order.")
                continue
            print_cart(cart)
            if read_yes_no("Confirm place order? (Y/N): "):
                print_invoice(menu, cart)
                cart.clear()
            else:
                print("Order cancelled. You can continue shopping.")

        elif choice == 7:
            print("Exiting. Goodbye.")
            break


if __name__ == "__main__":
    run_app()
