name =input("Enter Your name : ")
temp_var= ""
i=0
while i < len(name):
    if name[i] not in temp_var:
        temp_var += name[i]
        print(name[i] , ":" , name.count(name[i]))
    i += 1
print("loop end")