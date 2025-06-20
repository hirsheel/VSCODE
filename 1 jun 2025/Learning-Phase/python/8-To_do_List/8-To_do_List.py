# This function prints all the tasks and returns them as a list of lines
def open_print(task_):
    print("\n----------Here is a List of Tasks:---------------")
    with open(task_, "r", encoding="utf-8") as file:
        lines = file.readlines()
    for i, item in enumerate(lines):
        print(f'{i+1}.{item}', end="")
    print("\n-------------------------------------------------")
    return lines

# Start the main menu loop
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

            # Option 1: Add task
            if ask == 1:
                task = input("State Your Task: ").strip()
                with open("Task.txt", "a", encoding="utf-8") as a:
                    a.write(task + "\n")
                print("\n-----------Added-------------\n")

            # Option 2: Update a task
            elif ask == 2:
                lines = open_print("Task.txt")
                line_number = input("Enter Your Line to Change: ")
                if not line_number.isdigit():
                    print("\n-----PLease Choose A valid Line------\n")
                    continue

                line_number = int(line_number)
                if 1 <= line_number <= len(lines):
                    new_text = input("Enter Your Text: ")
                    lines[line_number - 1] = new_text + "\n"
                    with open("Task.txt", "w", encoding="utf-8") as file:
                        file.writelines(lines)
                    print(f"\n------------Line {line_number} updated.---------------\n")
                else:
                    print("\n---Invalid line number---\n")

            # Option 3: Delete task
            elif ask == 3:
                print("\nHere is a List of Tasks:")
                with open("Task.txt", "r", encoding="utf-8") as file:
                    lines = file.readlines()
                    for i, item in enumerate(lines):
                        print(f'{i+1}.{item}', end="")
                        print("\n----------------------------------------------\n")
                line_number = input("\nEnter Your Line to Delete: ")
                if not line_number.isdigit():
                    print("\n-----PLease Choose A valid Line------\n")
                    continue

                line_number = int(line_number)
                if 1 <= line_number <= len(lines):
                    del lines[line_number - 1]
                    with open("Task.txt", "w", encoding="utf-8") as file:
                        file.writelines(lines)
                    print(f"\n------------Line {line_number} deleted---------------\n")
                else:
                    print("\n---Invalid line number---\n")

            # Option 4: Mark task as complete
            elif ask == 4:
                lines = open_print("Task.txt")
                complete = input("Choose the line number: ")
                if not complete.isdigit():
                    print("\n--------Please Provide a valid line number--------------\n")
                    continue

                complete = int(complete)
                if 1 <= complete <= len(lines):
                    if lines[complete - 1].startswith("✅"):
                        print("\n------Already Completed-----\n")
                    else:
                        line_text = lines[complete - 1].rstrip("\n")
                        lines[complete - 1] = "✅" + line_text + "\n"
                        with open("Task.txt", "w", encoding="utf-8") as b:
                            b.writelines(lines)
                        print(f"\n---Task {complete} marked as completed---\n")
                else:
                    print("\n--------Please Provideh a valid line number--------------\n")

            # Option 5: Unmark a completed task
            elif ask == 5:
                lines = open_print("Task.txt")
                incomplete = input("Enter the number of line: ")
                if not incomplete.isdigit():
                    print("Give a Valid line number")
                    continue

                incomplete = int(incomplete)
                if 1 <= incomplete <= len(lines):
                    if "✅" in lines[incomplete - 1]:
                        lines[incomplete - 1] = lines[incomplete - 1].replace("✅", "", 1)
                        with open("Task.txt", "w", encoding="utf-8") as c:
                            c.writelines(lines)
                        print(f"\n---Task {incomplete} marked as incomplete again---\n")
                    else:
                        print("\n--------It's already Incomplete lol--------\n")
                else:
                    print("\n-------------Give a Valid Input!-------------------\n ")

            # Option 6: Show tasks
            elif ask == 6:
                lines = open_print("Task.txt")

            # Invalid number input
            else:
                print("\n---------Please Give A Valid Input (1-6) Or q to Quit---------\n")

        except:
            print("\n--------Please Give A Valid Input (1-6) Or q to Quit---------\n")     
