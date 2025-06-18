def f(n):
    # fb(0) == 0
    # fb(1) == 1
    # fb(n) == fb(n-1) + fb(n-2)
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return f(n-1) + f(n-2)
l = []
i = 0
while i != 15:
    m = int(input('json: '))
    f(m) 
    l.append(f(m))
    i += 1
else:
    for k in l:
        print(k, end =", ")
    