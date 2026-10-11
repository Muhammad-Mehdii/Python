name=input("Enter your name: ")
name2="Mir"
# Center method add bothside by '*'
# name length is 3 and we want to make it 7 so we need to add 4 '*' in total, 2 on each side.
print(name2.center(7, "*"))
#OR
print(name.center(len(name) + 4, "*"))
#output: **Mir**