st = 5
sp = 1
for i in range (1,6):
    for j in range(1, sp+1):
        print(" ", end =" ") 
    for k in range (1, st + 1):
        print("*", end =" ")
    sp = sp+1
    st = st-1
    print()