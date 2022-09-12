st = 1
sp = 4
for i in range (1,6):
    for l in range (1,sp + 1):
        print(" ", end = " ")
    for k in range (1, st + 1):
        print("*  ", end =" ")
    st = st+1
    sp = sp - 1 
    print() 