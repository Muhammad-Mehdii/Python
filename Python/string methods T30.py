name="MiR MuHaMmAD meHdi"
print("name : ",name)

# 1.Length Functions shows how many characters are in the string
length=len(name)
print("The length of the string is:",length)

# 2.lower() function converts all the characters in the string to lower case
lower=name.lower()
print("The string in lower case is:",lower)

# 3.upper() function converts all the characters in the string to upper case
upper=name.upper()
print("The string in upper case is:",upper)

# 4.title() function converts the first character of each word to upper case
title=name.title()
print("The string in title case is:",title)

# 5.strip() function removes the leading and trailing whitespaces from the string
strip=name.strip()
print("The string after removing leading and trailing whitespaces is:",strip)

# 6.replace() function replaces a specified substring with another substring in the string
replace=name.replace("MiR","Mr")
print("The string after replacing 'MiR' with 'Mr' is:",replace)

# 7.count() function counts the number of occurrences of a specified substring in the string
count=name.count("M")
print("The number of occurrences of 'M' in the string is:",count)