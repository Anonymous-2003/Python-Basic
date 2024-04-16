a = input("Enter anything:")
l = a.split() #by default it takes space, and converts the words to lists seprated by space
print(l)

l1 = []
for i in range(1,4):
    n = input(f"Enter value{i}:")
    l1.append(n)
print(l1)