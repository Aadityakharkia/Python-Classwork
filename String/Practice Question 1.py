s= input("Please enter a sentence ")
l = len(s)
c = 0 
for i in range(0,l):
    match(s[i]):
         case 'A'| 'E'| 'I'| 'O'| 'U'| 'a'| 'e'| 'i'| 'o'| 'u':
            c=c+1
print(" Number of letter a in the sentence ",s, "is",c)