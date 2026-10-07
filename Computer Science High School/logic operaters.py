print("For creating accout please Fill the following")
username=input("enter username :")
password=int(input("enter Passwoard :"))
day,month,year=input("enter your Date of Birth eg (5-10-2007) :").split("-")
print("Account created succesfully! \nLogin Please")
username1=input("enter username :")
password1=int(input("enter Passwoard :"))

if (username==username1 and password==password1):
    print("Login Succesfully")
    print(f"your age is : {2026-(int(year))}")
elif (username=="mmehdi.x" and password==5678):
    print("Login Succesfully")
    print(f"your age is : {2026-(int(year))}")
else:
    print("Invalid Username or Password")



