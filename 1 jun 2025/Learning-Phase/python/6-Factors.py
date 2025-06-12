print("This Program is to Get All The Factors of given number")
num = input("Enter Your Integer: ")
try:
    flo = float(num)
    if flo.is_integer():
        flo = int(flo)
        i = 1
        fac = []
        while i <= flo:
            if flo % i == 0:
                fac.append(str(i))
            i += 1
        print('Factors: ', ", ".join(fac))
    else:
        print("Give a Valid Integral Input please!")
except:
    print("Give a Valid Integer!")