num = input("Enter Your Number: ")
try:
    flo = float(num)
    
    # Check if it's actually an integer (like 56.0)
    if flo.is_integer():
        int_ = int(flo)
        if int_ % 2 == 0:     # Actual Code
            print("The Given Number is an Even Integer!")
        else:
            print("The Given Number is an Odd Integer!")
    else:  
        print("Wanna let you know that decimals \"Can't be Odd/Even!\"")
except:  # For some great Scholars (￣y▽,￣)╭
    print("You Sure are a Mathematician lol, Give a valid Number!")

