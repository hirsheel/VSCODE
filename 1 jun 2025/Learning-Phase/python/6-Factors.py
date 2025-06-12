print("This Program is to Get All The Factors of given number")
num = input("Enter Your Integer: ")
try:  # checks whether its a number or string
    flo = float(num)
    if flo.is_integer():  # checks whether float is integer
        flo = int(flo)
        i = 1
        fac = []
        while i <= flo: # check for divisors
            if flo % i == 0:
                fac.append(str(i))  
            i += 1
        print('Factors: ', ", ".join(fac))
    else:  # executes when float is a decimal
        print("Give a Valid Integral Input please!")
except:  # executes when input isnt a number
    print("Give a Valid Integer!")