# numbers = [1, 2, 3, 4]
# numbers.append(5)
# print(numbers)

# myList=[10,"apple",12,13,14]
# print("--------")
# print(myList)
# print(myList[1:2])
# print(myList[1:3])
# print(myList[:2])
# print(myList[2:])

# items = []

# n = int(input("Enter number of elements: "))

# for i in range(n):
#     value = input(f"Enter element {i + 1}: ")

#     # Convert to int if possible
#     if value.isdigit():
#         items.append(int(value))
#     else:
#         items.append(value)

# print("\nList created:", items)

# search_value = input("Enter element to search: ")

# # Convert search value similarly
# if search_value.isdigit():
#     search_value = int(search_value)

# if search_value in items:
#     print("Item found in the list")
# else:
#     print("Item NOT found in the list")

# Dictionary to store fruit prices (Rs per Kg)

# Predefined fruit prices (Rs per Kg)
fruit_prices = {
    "apple": 100,
    "banana": 40,
    "mango": 120,
    "orange": 60,
    "grapes": 80
}

# Display available fruits
print("Available fruits:")
for fruit in fruit_prices:
    print("-", fruit.capitalize())

# Search fruit
search_fruit = input("\nEnter fruit name: ").strip().lower()

# Check price
if search_fruit in fruit_prices:
    print(f"{search_fruit.capitalize()} costs Rs {fruit_prices[search_fruit]} per Kg")
else:
    print("Sorry, this fruit is not available.")

