def open_and_print(task_):
    print("\nHere is a List of Tasks:")
    with open(task_, "r") as file:
        lines = file.readlines()
    for i, item in enumerate(lines):
            print(f'{i+1}.{item}', end = "")
while True:
    print("Choose from The Options Below:\n")
    print("1.Add tasks")
    print("2.Update tasks")
    print("3.Delete tasks")
    print("4.Mark tasks as complete")
    print("5.Remark Completed Tasks as Incomplete")
    print("6.Show all tasks\n")
    ask = input("Choose Your Option(1-6) or q to Quit: ").strip()
    if ask.lower() == "q":
        print("Have A Nice Day!")
        break
    else:
        try:
            ask = int(ask)
            if ask == 1:
                task = input("State Your Task: ").strip()
                with open("Task.txt", "a") as a:
                    a.write(task + "\n")
                print("\n-----------Added-------------\n")
            elif ask == 2:
                open_and_print("Task.txt")
                line_number = input("Enter Your Line to Change: ")
                try:
                    line_number = int(line_number)
                    if 1 <= line_number <= len(lines):
                        new_text = input("Enter Your Text: ")
                        lines[line_number - 1] = new_text + "\n"
                        with open("Task.txt", "w") as file:
                            file.writelines(lines)
                        print(f"\n------------Line {line_number} updated.---------------\n")
                    else:
                        print("\n---Invalid line number---\n")
                except:
                    print("\n-----PLease Choose A valid Line------\n")
            elif ask == 3:
                print("\nHere is a List of Tasks:")
                with open("Task.txt", "r") as file:
                    lines = file.readlines()
                    for i, item in enumerate(lines):
                        print(f'{i+1}.{item}', end = "")
                line_number = input("Enter Your Line to Delete: ")
                try:
                    line_number = int(line_number)
                    if 1 <= line_number <= len(lines):
                        with open("Task.txt", "w") as file:
                            del lines[line_number - 1]
                            file.writelines(lines)
                        print(f"\n------------Line {line_number} deleted---------------\n")
                    else:
                        print("\n---Invalid line number---\n")
                except:
                    print("\n-----PLease Choose A valid Line------\n")
            elif ask == 4:
                
            elif ask == 5:
            elif ask == 6:
            else:
                print("Please Give A Valid Input (1-6) Or q to Quit")   
        except:
            print("Please Give A Valid Input (1-6) Or q to Quit")
