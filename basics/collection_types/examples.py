# --- List Examples ---
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")  # Adding an item
fruits.extend(["grape", "mango"])  # Extending the list
print("Fruits List:", fruits)
print("First fruit:", fruits[0])  # Accessing an item
fruits.remove("banana")  # Removing an item
print("Fruits after removal:", fruits)
fruits.sort()  # Sorting the list
print("Sorted Fruits:", fruits)
fruits.reverse()  # Reversing the list
print("Reversed Fruits:", fruits)

# --- Tuple Examples ---
dimensions = (200, 50, 150)
print("Dimensions Tuple:", dimensions)
print("First dimension:", dimensions[0])  # Accessing an item

# --- Set Examples ---
unique_colors = {"red", "blue", "green"}
unique_colors.add("yellow")  # Adding an item
print("Colors Set:", unique_colors)
unique_colors.discard("blue")  # Removing an item
print("Colors after discard:", unique_colors)
other_colors = {"green", "orange"}
combined_colors = unique_colors.union(other_colors)  # Union of sets
print("Combined Colors:", combined_colors)
intersection_colors = unique_colors.intersection(other_colors)  # Intersection
print("Intersection Colors:", intersection_colors)

# --- Dictionary Examples ---
person = {"name": "Alice", "age": 25}
print("Person Dictionary:", person)
person["age"] = 26  # Updating an item
person["email"] = "alice@example.com"  # Adding a new key-value pair
print("Updated Person Dictionary:", person)
del person["age"]  # Deleting a key-value pair
print("Person Dictionary after deletion:", person)
print("All keys:", list(person.keys()))  # Listing all keys
print("All values:", list(person.values()))  # Listing all values
