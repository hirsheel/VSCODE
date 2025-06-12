print("This Program is to Get All The Factors of given number")
num = input("Enter Your Integer: ")
try:
    flo = float(num)
    if flo.is_integer():
        flo = int(flo)
        i = 1
        while i <= flo:
            if flo % i == 0:
                print(i, end=", ") 
            i += 1
    else:
        print("Give a Valid Integral Input please!")
except:
    print("Give a Valid Integer!")