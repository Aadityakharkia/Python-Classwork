st = 1
sp = 0
l = 7
for i in range (1,9):
    for t in range (0,1):
        print("*", end = " ")
    for k in range (0, sp + 1):
        print(" ", end =" ")
    for t in range (1,st + 1):
        print("*", end = " ")
    for g in range (1, l+1):
        print(" ", end =" ")
    for d in range (1,st + 1):
        print("*", end = " ")

    print() 
    sp = sp+1
    l = l-1 