is_on = True

while is_on:
    users_class = input("Which class are you in ?\n")
    Name = input("Please Enter Your Name : ")
    English = int(input("English : "))
    Maths = int(input("Maths : "))
    Science = int(input("Science : "))
    Hindi = int(input("Hindi : "))
    Computers = int(input("Computers : "))
    with open("marks.txt", "a") as data_file:
        data_file.write(f"{Name} | {users_class} |English:{English} | Maths:{Maths} | Hindi:{Hindi} | Science:{Science} | Computers:{Computers}\n")
    Next_user = input("Is there any other user : ")
    if Next_user=="No":
        is_on= False