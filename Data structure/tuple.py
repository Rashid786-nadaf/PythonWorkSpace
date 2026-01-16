# # Defining the Tuple
# myTuple = ("Apple", 10, "Orange", "Grapes", 20.0, 10)

# # 1. Accessing by index (index 3 is the 4th item)
# print(myTuple[3])        # Output: Grapes

# # 2. Accessing the last item using negative indexing
# print(myTuple[-1])       # Output: 10

# # 3. Slicing from index 2 up to (but not including) index 4
# print(myTuple[2:4])      # Output: ('Orange', 'Grapes')

# # 4. Slicing from the beginning up to index 4
# print(myTuple[:4])       # Output: ('Apple', 10, 'Orange', 'Grapes')

# # 5. Slicing from index 2 to the end
# print(myTuple[2:])       # Output: ('Orange', 'Grapes', 20.0, 10)

sensor_readings = (
    "2026-01-16", 22.5, "Sunny", 1013.2, 45, "North", "Active"
)

weather = sensor_readings[2]
print(weather)

last_item = sensor_readings[-1]
print(last_item)

first_four = sensor_readings[:4]
print(first_four)

slice_1_to_4 = sensor_readings[1:4]
print(slice_1_to_4)
