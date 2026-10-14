#pass statment 
 
age=int("input age :")
if age>= 14:
    pass


#tutorial no 42

win=12
inputnum=int(input("gues a num b/n 1-100 :"))
if inputnum == win:
    print("you win")
else:
    if inputnum>win :
        print("too high")
    else:
        print("too low")