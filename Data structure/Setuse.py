unique = {1, 2, 2, 3}
unique.add(4)
print(unique)

# Force-assign the new values
mySet1 = {"Apple", 10, "Orange", "Grapes", 20.0}
mySet2 = {30.0, 10, "Orange", "Apple", 40}

# Print the results
print("Union:", mySet1 | mySet2)
print("Intersection:", mySet1 & mySet2)
print("Difference:", mySet1 - mySet2)
print("Symmetric Difference:", mySet1 ^ mySet2)