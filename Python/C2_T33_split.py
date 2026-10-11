name="          MIR MuHaMmAD meHdi          "
dot=".................."
print(name+dot)
# 1. lstrip() function removes the leading whitespaces from the string
print("The string after removing left side whitespaces is:",name.lstrip()+dot)
# 2. rstrip() function removes the Right side whitespaces from the string
print("The string after removing right side whitespaces is:",name.rstrip()+dot)
# 3. strip() function removes both left and right side whitespaces from the string
print("The string after removing both left and right side whitespaces is:",name.strip()+dot)
print("OR")
print(name.replace(" ","")+dot) # replace all the whitespaces to none from the string

