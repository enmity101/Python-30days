# String Search Methods
phone = "+91-89546-74545"
print(phone.startswith("+91"))
print(phone.endswith("74545"))
print(phone.find("+")) 

# Search for a substring in a string
email = "harshsingh@gmail.com"
email1 = "harshsingh@outlook.com"

# Check if the email starts with "harsh" and ends with "gmail.com"
print(email.startswith("harsh") and email.endswith("gmail.com"))
print(email1.startswith("harsh"))
print(email1.endswith("gmail.com"))

# Check if the email contains "@" symbol
print("@" in email)
print("@" in email1)

# Search for a substring and get its index
url = "https://www.api.company.com/v2/users/products"

print(url.startswith("https://"))
print(url.endswith("/products"))

# Find the index of "api" in the URL
print(url.find("api"))
print("api" in url)

phone1 = "+91-89546-74545"
phone2 = "58598-53532"
phone3 = "0091-42355-98789"

# old way to extract the phone number without country code
print(phone1[4:])
print(phone2[:])
print(phone3[5:])

# new way to extract the phone number without country code using find() method
print(phone1[phone1.find("-") +1:])
print(phone2[:])
print(phone3[phone3.find("-") +1:])













