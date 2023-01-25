n=int(input("enter a no. = "))
a=int(input("enter the lower value of range = "))
b=int(input("enter the upper value of range = "))
c=b-a
count = 0
while count<=c:
    if(a%n==0):
        print(a)
    else:
        print()
    count=count+1
    a=a+1
