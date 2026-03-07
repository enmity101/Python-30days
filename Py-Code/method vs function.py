# ============================================================
#        DIFFERENCE BETWEEN FUNCTIONS AND METHODS IN PYTHON
# ============================================================

# ---------------------------------------------------------------
# 1. FUNCTION
# ---------------------------------------------------------------
# - A function is a STANDALONE block of reusable code.
# - It is defined using the 'def' keyword OUTSIDE of a class.
# - It is called independently by its name.
# - It does NOT belong to any object or class.
# - It does NOT take 'self' as its first parameter.

# Example of a Function:
def greet(name):
    return f"Hello, {name}!"

print(greet("Harsh Singh"))   # Output: Hello, Harsh Singh!


# ---------------------------------------------------------------
# 2. METHOD
# ---------------------------------------------------------------
# - A method is a function that is DEFINED INSIDE a class.
# - It is associated with an OBJECT or CLASS.
# - It is called on an object using the dot (.) operator.
# - It automatically takes 'self' as its first parameter,
#   which refers to the instance of the class.

# Example of a Method:
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):               # This is a METHOD
        return f"Hello, {self.name}!"

p = Person("Harsh Singh")
print(p.greet())        # Output: Hello, Harsh Singh!


# ---------------------------------------------------------------
# 3. KEY DIFFERENCES AT A GLANCE
# ---------------------------------------------------------------

# | Feature              | Function                        | Method                          |
# |----------------------|---------------------------------|---------------------------------|
# | Definition           | Defined outside a class         | Defined inside a class          |
# | Association          | Independent / standalone        | Belongs to an object or class   |
# | First Parameter      | No 'self' required              | Takes 'self' (or 'cls') param   |
# | How to Call          | function_name(args)             | object.method_name(args)        |
# | Access to Object     | Cannot access object data       | Can access object attributes    |
# | Example              | len(), print(), greet()         | list.append(), str.upper()      |


# ---------------------------------------------------------------
# 4. BUILT-IN EXAMPLES
# ---------------------------------------------------------------

# Built-in FUNCTION (standalone):
my_list = [3, 1, 2]
print(len(my_list))         # len() is a built-in FUNCTION → Output: 3

# Built-in METHOD (called on an object):
my_list.sort()              # sort() is a METHOD of the list object
print(my_list)              # Output: [1, 2, 3]

my_string = "hello harsh singh"
print(my_string.upper())    # upper() is a METHOD of the str object → Output: HELLO HARSH SINGH


# ---------------------------------------------------------------
# 5. SUMMARY
# ---------------------------------------------------------------
# ✅ FUNCTION  → Lives outside a class, called by name directly.
# ✅ METHOD    → Lives inside a class, called on an object using dot notation.
# Both are defined with 'def', but a method always belongs to a class/object.
