# we can not change the string because it is immutable.
# but we can create a new string with the changes we want.
string="MIR"
string.replace("I", "i")# not works because string is immutable
print(string)
#but we can create a new string with the changes we want.
new_string=string.replace("I", "i")
print(new_string)
