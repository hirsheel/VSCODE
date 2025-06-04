import random
cd = input("Enter code/c or decode/d: ")  # takes user input to code or decode
voc = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"  # word library for random letters
if cd.capitalize() in ["Code", "C"]:  # coding part
    st = input("Enter your Word to Code: ")
    word = st.split()
    for w in word:
        if len(w) >= 3:
            w = list(w)
            rp = random.choices(voc, k=3)  # adds random 3 letter prefix
            rs = random.choices(voc, k=3)  # adds random 3 letter suffix
            w.append(w[0])  # writes 1st letter of word at last
            w.pop(0)  # removes 1st letter from original word
            jk = rp + w + rs  # joins the random letter and finalize
            print("".join(jk), end=" ")  # prints finalized word
        else:
            print(w[::-1], end=" ")  # reverse the 2/1 character word
elif cd.capitalize() in ["Decode", "D"]:  # decoding part
    de = input("Enter your Code to Decode: ")
    ds = de.split()
    for d in ds:
        if len(d) >= 9:
            d = list(d)
            k = d[3:-3]
            k.insert(0, k.pop())
            print("".join(k), end=" ")
        else:
            print(d[::-1], end=" ")
else:
    print("Next Time Enter a Valid Option, THANKS ;]")

