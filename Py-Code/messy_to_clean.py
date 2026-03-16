# Clean and format the raw string into: name | role | age
details = "968-Maria, ( D@t@ Engineer ) ;; 27y  ".lower().strip()\
    .replace(" ", "")\
    .replace(";;", "age:")\
    .replace(",", "|")\
    .replace("(", "role:")\
    .replace(")", "|")\
    .replace("@", "a")\
    .replace("y", "")\
    .replace("968-", "name:")\
    .replace(" ", "")\
    .replace("|", " | ")

print(details)

