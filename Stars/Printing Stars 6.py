st = 5
sp = 0
for i in range (1,6):
    for k in range (1, st + 1):
        print("*", end =" ")
    for j in range(1, sp+1):
        print(" ", end =" ")
    for i in range (1,st+1):
        print("*" ,end = " ")
    sp = sp+2
    st = st-1
    print()