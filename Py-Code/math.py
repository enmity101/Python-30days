# Length of a String
password = '912yefge23eh'
print(len(password))  # Output: 12

if len(password) < 8:
    print("Your Password is too short.")
else:    print("Your Password is strong enough.")

# Counting
text = """
Python is easy to learn
python is powerful
python is popular
many people use python
"""

print(text.count("python"))

# Transformations

price = "12132,99"
price = price.replace(',' , '.')
print(price)  


phone = "123-456-7890"
phone = phone.replace('-' , '')
print(phone)


price = '$1,243.99'
price = price.replace('$', '')
print(price)

phone = "+49 (176) 123-4567"
phone = phone.replace('+' , '00')
phone = phone.replace('(' , '')
phone = phone.replace(')' , '')
phone = phone.replace('-' , '')
phone = phone.replace(' ' , '')
print(phone) 

# String Transformations
first_name = "Harsh"
last_name = "Singh"
last_name = first_name + " " + last_name
print(last_name)  # Output: Harsh Singh


folder = "C:/Users/Harsh"
file = "data.txt"
full_file_path = folder + "/" + file
print(full_file_path)  # Output: C:/Users/Harsh/data.txt












