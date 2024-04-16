# l = [1,2,3,4,5,6,"Avishek","Basyal",["apple","banana","mango"]]
# print(l[6])
# print(l[0::2])
# print(l[8][1])
# print(l[-1::-1])


#list iteration

# for i in l:
#     print(i)


# for i in range(len(l)):
#     print(l[i])


# for i in range(len(l)-1,-1,-1):
#     print()


#sorting in lists
l = ['a','e','i','o','u','c','f','z','g']
l.sort()
print(l)     #print(l.sort()) doesn't work

#without list comprehension
# new_list = []
# n = int(input("Enter  number:"))
# for i in range(n):
#     fruit = input("Enter fruit name:")
#     new_list.append(fruit)
# print(new_list)