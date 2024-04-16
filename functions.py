def area(l1,l2=5):  # here default value of l2 is 5
    print("Area is ",l1*l2)
    a = l1+l2
    return a
a = int(input("Enter length:"))
b = int(input("Enter breadth:"))

print(area(a,b))