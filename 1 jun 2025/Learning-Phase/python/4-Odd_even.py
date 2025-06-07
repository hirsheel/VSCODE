num = input("Enter Your Number: ")
try:
    num = int(num)  # Main purpose
    if num % 2 == 0:
        print("The Given Number is an Even Integer!")
    else:
        print("The Given Number is an Odd Integer!")
except:
    try:
        float(num)  # Just check if it's a float
        print("Wanna let you know that decimals \"Can't be Odd/Even!\"")
    except:  # for some great scholars (￣y▽,￣)╭ 
        print("You Sure are a Mathematician lol, Give a Number!")
