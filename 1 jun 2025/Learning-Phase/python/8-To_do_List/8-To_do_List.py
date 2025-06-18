print("Choose from The Options Below:")
print("1.Add tasks")
print("2.Delete tasks")
print("3.Mark tasks as complete")
print("4.Remark Completed Tasks as Incomplete")
print("5.View all incomplete tasks")
print("6.Show all completed tasks")
ask = input("Choose Your Option(1-6) or q to Quit: ").strip()
if ask.lower() == "q":
    print("Have A Nice Day!")
else:
    try:
        ask = int(ask)
        if ask == 1:
            task = input("State Your Task: ").strip()
            with open("Task.txt", "a") as a:
                a.write(task + "\n")
            
    except:
        print("Please Give A Valid Input (1-6) Or q to Quit")