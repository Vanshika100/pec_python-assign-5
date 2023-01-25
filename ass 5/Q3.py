a = int(input("enter 1st side of triangle = "))
b = int(input("enter 2nd side of triangle = "))
c = int(input("enter 3rd side of triangle = "))
s = (a + c + b) / 2
if c >= a + b:
    print("enter a valid triangle")
elif b >= a + c:
    print("enter a valid triangle")
elif a >= b + c:
    print("enter a valid triangle")
else:
    area = (s * (s - a) * (s - b) * (s - c)) ** (1 / 2)
    print(area)
