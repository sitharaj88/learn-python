# Control Flow Examples

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
