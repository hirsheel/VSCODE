import random
opt = [ "Snake", "Water", "Gun" ]
print("Let's Play The Game!")
inp = input("Select One: Snake/ Water/ Gun (or Q to quit):  ").strip().capitalize()
cc = random.choice(opt)
if inp in opt:
    print(f"The Computer chooses: {cc}")
    if inp == "Q":
         print("THANKs for playing!")
    elif inp == cc:
        print("Well, Looks like a draw")
    elif (inp == "Snake" and cc == "Water") or (inp == "Water" and cc == "Gun" ) or (inp == "Gun" and cc == "Snake"):
        print("You Won!")
    else:
        print("You Lost...")
else:
    print("enter a valid input!")