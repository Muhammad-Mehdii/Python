a=int(input("enter the value of a :"))
b=int(input("enter the value of b :"))
c=int(input("enter the value of b :"))
if a>b and a>c:
    print("a is greater than b and c")
elif b>a and b> c :
    print("b is greater than a and c")
    
elif c>a and c>b:
    print("c is greater than a and b")
elif a==b and a>c:
    print("a and b are equal and greater than c")
elif c==a and c==b:
    print("all three numbers are equal")
else:
    wrong = "all are equal"
    print("wrong number")











