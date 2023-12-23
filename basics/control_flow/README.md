# Control Flow in Python

Control flow is essential for decision-making in programs. This section covers `if` statements, `for` and `while` loops, and the `match` statement.

## Examples
- **If statements**: Used for decision-making.
- **For loops**: Iterate over a sequence.
- **While loops**: Repeat as long as a condition is true.
- **Match statements**: New in Python 3.10, similar to switch/case in other languages, used for pattern matching.

See below for real-world applications.

```python
# If statement
temperature = 20
if temperature > 30:
    print("It's a hot day!")
else:
    print("It's not a hot day.")

# For loop
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print("Fruit:", fruit)

# While loop
count = 0
while count < 3:
    print("Count:", count)
    count += 1

# Match statement (Python 3.10+)
color = "red"
match color:
    case "red":
        print("The color is red.")
    case "blue":
        print("The color is blue.")
    case _:
        print("The color is unknown.")
