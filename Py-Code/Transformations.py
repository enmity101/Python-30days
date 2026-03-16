csv_file = "454,Harsh Singh,25,Data Analyst,India, 2000-02-02,Male,50000\n"
print(csv_file.split(","))

# String Transformations
print("ha" * 5)             # repeats the string "ha" 5 times

# Indexing and Slicing
text = "Python"

# Extract the first character
print(text[0])              # Output: 'P'
print(text[-6])             # Output: 'P'

# Extract the last character
print(text[-1])             # Output: 'n'
print(text[5])              # Output: 'n'

# Extract 'h'
print(text[3])              # Output: 'h'
print(text[-3])             # Output: 'h'

# Date
date = "2024-06-01"

# Extract the year
print(date[:4])             # Output: '2024' (year)
print(date[0:4])            # Output: '2024' (year)

# Extract the month
print(date[5:7])            # Output: '06' (month)
print(date[-5:-3])          # Output: '06' (month)


# Extract the Day
print(date[-2:])            # Output: '01' (day)
print(date[8:10])           # Output: '01' (day)

# Whitespace Removal
text = "  Engineering     "
print(text.lstrip())
print(text.rstrip())
print(text.strip())

text = "###ABC###".strip("#")
print(text)                 # Output: 'ABC'

# Whitespace Cleanup
text = "  Engineering"
print(len(text))            # Output: 14
print(len(text.strip()))    # Output: 11

nr_of_spaces = len(text) - len(text.strip())
is_clean = len(text) == len(text.strip())

print("Number of Spaces:", nr_of_spaces)    # Output: 3
print("Is the text clean?", is_clean)       # Output: False



# Case Conversion
text = "python PROGRAMMING"
print(text.upper())         # Output: 'PYTHON PROGRAMMING'
print(text.lower())         # Output: 'python programming'
print(text.title())         # Output: 'Python Programming'
print(text.capitalize())    # Output: 'Python programming'


search = "Email".lower().strip()
data = " emAil".lower().strip()

print(search == data)       # Output: True