##### user input
# name = input("Enter your name: ")
# print("Hello, " + name)

##### condition

x = 10
if x > 5:
    print("x is greater than 5")
else:
    print("x is not greater than 5")

##### loops
# Using a for loop
for i in range(5):
    print(i)

# Using a while loop
count = 0
while count < 5:
    print(count)
    count += 1

##### lists
fruits = ["apple", "banana", "cherry"]
print(fruits[0])  # Accessing elements
fruits.append("orange")  # Adding an element


##### functions
def greet(name):
    return "Hello, " + name

message = greet("Bob")
print(message)

###### directories
student = {"name": "Alice", "age": 20, "grade": "A"}
print(student["name"])  # Accessing values
student["age"] = 21  # Modifying values

####### errors
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Division by zero is not allowed")

###### files
# Writing to a file
with open("example.txt", "w") as file:
    file.write("This is a sample text.")

# Reading from a file
with open("example.txt", "r") as file:
    content = file.read()
    print(content)

