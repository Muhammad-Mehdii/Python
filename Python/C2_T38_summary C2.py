#string
name="Mir"
name2="Muhammad"
#string indexing
print(name[0])  # Output: M
print(name[1])  # Output: i
print(name[2])  # Output: r
#string slicing
print(name[-1:0:-1])  # Output: riM
#take input from user
age=input("Enter your age: ")
print("Your age is:", age)
#two inputs
name3, age2 = input("Enter your name and age: ").split(",")
print("Your name is:", name3)
print("Your age is:", age2)
#length of string
print(len(name))  # Output: 3
#lowercase, uppercase amd titlecase
print(name.lower())  # Output: mir
print(name.upper())  # Output: MIR
print(name.title())  # Output: Mir
#find , replace and count
print(name.find("i"))  # Output: 1
print(name.replace("i", "I"))  # Output: mIr
print(name.count("r"))  # Output: 1

