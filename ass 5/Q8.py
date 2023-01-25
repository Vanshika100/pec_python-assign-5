for i in range (1,11):
    i = int(input("enter a number = "))
    if (i>=0):
        if i == 0:
            print("zero")
        else:
            print("positive number")
    else:
        print("negative number")
    if(i%2) == 0:
        print(str(i) + " is even")
    else:
        print(str(i) + " is odd")
