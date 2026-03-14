''' modern, super-easy way to format and build strings
    "f" stands for "formatted"
    lets you easily put variables and expressions
    directly inside string value using curly braces {}
'''

name = "Harry Potter"
age = 22
is_student = False
print("My name is " + name + ", I am " + str(age) + " years old, and student status is " + str(is_student) + ".")  
# old way of formatting strings
print(f"My name is {name}, I am {age} years old and student status is {is_student}.")

print(f"In 5 years, {name} will be {age + 5} years old.")

# you can also put expressions inside the curly braces

name = input("Enter your name: ")
age = int(input("Enter your age: "))
is_student = input("Are you a student? (yes/no): ").lower() == "yes"
print(f"Hello {name}, you are {age} years old and your student status is {is_student}.")