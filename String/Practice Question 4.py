s= input("Please enter a sentence ")
s= s.strip()
l = len(s)
c = 0 
for i in range(0,l):
    if (s[i]==' ' and s[i+1]!=' '):
            c=c+1
print(" Number of vowels a in the sentence ",s, "is",c)