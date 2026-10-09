name=input("enter your name :")
physics=int(input("emter Marks of physics :"))
math=int(input("emter Marks of Math :"))
computer=int(input("emter Marks of computer :"))
isl=int(input("emter Marks of islamiyat :"))
english=int(input("emter Marks of english :"))
urdu=int(input("emter Marks of urdu :"))
Total_marks=int(input("Enter Total Marks :"))
obtain_marks=physics+math+computer+isl+english+urdu
persentage=(obtain_marks/Total_marks)*100
print("\n")
print("RESULT CARD")
print(f"your name is : {name}\nphysics {physics}\nmath : {math}\ncomputer : {computer} \nislamiyat : {isl}\nenglish : {english}\nurdu : {urdu}")
print(f"you got {persentage} % in exam")
if persentage>100:
    print("Invalid Marks")
elif persentage>90 and persentage<=100:
    print("you got A+ Grade")
    print("Status Pass")
elif persentage>80 and persentage<=90:
    print("you got A Grade")
    print("Status Pass")
elif persentage>70 and persentage<=80:
    print("you got B Grade")
    print("Status Pass")
elif persentage>60 and persentage<=70:
    print("you got C Grade")
    print("Status Pass")
elif persentage>50 and persentage<=60:
    print("you got D Grade")
    print("Status Pass")
else:
    print("your dot F Grade \nStatus failed")

