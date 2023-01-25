a = int(input("enter the lower value of range = "))
b = int(input("enter the upper value of range = "))
for number in range(a, b + 1):
    count = 0
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            count = count + 1
            break

    if count == 0 and number != 1:
        print("%d" % number, end=" ")
