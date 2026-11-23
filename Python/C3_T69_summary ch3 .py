#if , elif , else  statment
name="mir"
name2=input("enter your name : ")
if name=="mir" or name=="Mir":
    print("your name is mir")
elif name2=="Muhammad":
    print("your name is Muhammad")
else:
    print("your name is not mir or Muhammad")

print("\n\n")

#while loop
i=1
while i<=10:
    print(i)
    i+=1

print("\n\n")

#for loop
for i in range(1,11,2):
    print(i)

print("\n\n")

#break and continue statement
for i in range(1,11):
    if i==5:
        break
    print(i)

print("\n\n")

for i in range(1,11):
    if i==5:
        continue
    print(i)

print("\n\n")

#for loop in string
name = "Mir Muhammad"
for i in range(len(name)):
    print(name[i])
