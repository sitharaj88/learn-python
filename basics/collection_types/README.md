# Collection Types in Python

In Python, collection types are used to store collections of data. In this section, we'll explore some of the basic collection types: Lists, Tuples, Sets, and Dictionaries.

## Lists
- **Mutable**: Lists can be changed after creation.
- **Ordered**: The order of elements is maintained.
- **Example**: `fruits = ["apple", "banana", "cherry"]`

## Tuples
- **Immutable**: Tuples cannot be changed after creation.
- **Ordered**: The order of elements is maintained.
- **Example**: `dimensions = (200, 50)`

## Sets
- **Mutable**: Sets can be changed after creation.
- **Unordered and Unindexed**: Sets do not record element position.
- **Example**: `unique_colors = {"red", "blue", "green"}`

## Dictionaries
- **Mutable**: Dictionaries can be changed after creation.
- **Unordered (As of Python 3.7, ordered)**: Dictionaries are collections of key-value pairs.
- **Example**: `person = {"name": "Alice", "age": 25}`

## Usage and Applications
- **Lists**: Used for storing a collection of related items.
- **Tuples**: Suitable for storing a sequence of elements that shouldn't change.
- **Sets**: Ideal for membership testing, removing duplicates.
- **Dictionaries**: Perfect for storing data in key-value pairs for fast retrieval.

Understanding these collection types is crucial as they form the basis for data organization and manipulation in Python programming.

## Example usage of python collection:

```python
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


