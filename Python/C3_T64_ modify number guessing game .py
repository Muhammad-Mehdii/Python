import random
win_num= random.randint(1,100)
atemps = 1
game_over = False
while not game_over:
    ges_num=int(input("gess a number between 1 - 100 : "))
    
    if ges_num==win_num:
        print(f"you won in {atemps} atemps")    
        print("you won !")
        break
    elif ges_num<win_num:
        print("num is too loo")
        atemps+=1
    else:
        print("num is too high")
        atemps+=1