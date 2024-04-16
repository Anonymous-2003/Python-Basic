l = [5,6,3,89,33,0]
print(f"The original list is {l}")
print(l.pop(3))    # return(because of print) and removes the element at index 3
print(l)
del l[1]
print(l)
l.remove(33)    # removes the value passed not index number
print(l) 
l.clear()   # clears the whole list
print(l)

# to update list

ls = [34,36,23,90,200]
ls[1] = 50  #updates the list : value at index number 1 will be replaced by 50
print(ls)


ls.insert(2,100)    # 100 will be inserted at index 2 without replacing any elements
print(ls)

ls.append(87)   # 87 will be added to last index of list
print(ls)

ls1 = [11,12,13]
ls.append(ls1)  # new list will be added as a list 
print(ls)

ls.extend(ls1)  # new list will be extended and become single list
print(ls)  