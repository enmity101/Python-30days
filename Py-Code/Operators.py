# ============================================
#           PYTHON OPERATORS
#           Author: Harsh Singh
# ============================================

name = "Harsh Singh"
print(f"Author: {name}")
print("=" * 45)


# ──────────────────────────────────────────
# 1.  ARITHMETIC OPERATORS
# ──────────────────────────────────────────
print("\n--- Arithmetic Operators ---")

a = 20
b = 6

print(f"a = {a}, b = {b}")
print(f"Addition       (a + b)  = {a + b}")
print(f"Subtraction    (a - b)  = {a - b}")
print(f"Multiplication (a * b)  = {a * b}")
print(f"Division       (a / b)  = {a / b}")
print(f"Floor Division (a // b) = {a // b}")
print(f"Modulus        (a % b)  = {a % b}")
print(f"Exponentiation (a ** b) = {a ** b}")


# ──────────────────────────────────────────
# 2.  ASSIGNMENT OPERATORS
# ──────────────────────────────────────────
print("\n--- Assignment Operators ---")

x = 10
print(f"x = {x}")

x += 5
print(f"x += 5  ->  x = {x}")

x -= 3
print(f"x -= 3  ->  x = {x}")

x *= 2
print(f"x *= 2  ->  x = {x}")

x /= 4
print(f"x /= 4  ->  x = {x}")

x //= 2
print(f"x //= 2 ->  x = {x}")

x **= 3
print(f"x **= 3 ->  x = {x}")

x %= 5
print(f"x %= 5  ->  x = {x}")
 
# ──────────────────────────────────────────
# 3.  COMPARISON OPERATORS
# ──────────────────────────────────────────
print("\n--- Comparison Operators ---")

harsh_age   = 22
friend_age  = 25

print(f"Harsh Singh's age  = {harsh_age}")
print(f"Friend's age       = {friend_age}")
print(f"Equal              (==) : {harsh_age == friend_age}")
print(f"Not Equal          (!=) : {harsh_age != friend_age}")
print(f"Greater Than       (>)  : {harsh_age > friend_age}")
print(f"Less Than          (<)  : {harsh_age < friend_age}")
print(f"Greater or Equal   (>=) : {harsh_age >= friend_age}")
print(f"Less or Equal      (<=) : {harsh_age <= friend_age}")


# ──────────────────────────────────────────
# 4.  LOGICAL OPERATORS
# ──────────────────────────────────────────
print("\n--- Logical Operators ---")

is_student   = True
has_id_card  = True
is_graduated = False

print(f"is_student   = {is_student}")
print(f"has_id_card  = {has_id_card}")
print(f"is_graduated = {is_graduated}")

print(f"AND  (is_student and has_id_card)  = {is_student and has_id_card}")
print(f"OR   (is_student or is_graduated)  = {is_student or is_graduated}")
print(f"NOT  (not is_graduated)            = {not is_graduated}")


# ──────────────────────────────────────────
# 5.  BITWISE OPERATORS
# ──────────────────────────────────────────
print("\n--- Bitwise Operators ---")

p = 12   # binary: 1100
q = 10   # binary: 1010

print(f"p = {p} (binary: {bin(p)})")
print(f"q = {q} (binary: {bin(q)})")
print(f"AND   (p & q)  = {p & q}   -> {bin(p & q)}")
print(f"OR    (p | q)  = {p | q}  -> {bin(p | q)}")
print(f"XOR   (p ^ q)  = {p ^ q}   -> {bin(p ^ q)}")
print(f"NOT   (~p)     = {~p}")
print(f"Left  Shift (p << 1) = {p << 1}  -> {bin(p << 1)}")
print(f"Right Shift (p >> 1) = {p >> 1}   -> {bin(p >> 1)}")


# ──────────────────────────────────────────
# 6.  IDENTITY OPERATORS
# ──────────────────────────────────────────
print("\n--- Identity Operators ---")

name1 = "Harsh Singh"
name2 = "Harsh Singh"
name3 = name1

print(f"name1 = '{name1}'")
print(f"name2 = '{name2}'")
print(f"name3 = name1")
print(f"name1 is name3     = {name1 is name3}")
print(f"name1 is name2     = {name1 is name2}")
print(f"name1 is not name2 = {name1 is not name2}")


# ──────────────────────────────────────────
# 7.  MEMBERSHIP OPERATORS
# ──────────────────────────────────────────
print("\n--- Membership Operators ---")

members = ["Harsh Singh", "Ravi Yadav", "Priya Sharma", "Arjun Mehta"]

print(f"Members list: {members}")
print(f"'Harsh Singh' in members     = {'Harsh Singh' in members}")
print(f"'John Doe' in members        = {'John Doe' in members}")
print(f"'John Doe' not in members    = {'John Doe' not in members}")


# ──────────────────────────────────────────
# --  SUMMARY
# ──────────────────────────────────────────
print("\n" + "=" * 45)

print(f"  Done by: {name}")
print("=" * 45)
