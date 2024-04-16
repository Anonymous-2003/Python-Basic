#using zip function

l1 = [10,20,30,40]
l2 = [50,60,70,80,90]
for i,j in zip(l1,l2):  # zip function iterates over 2 lists at same time. It iterates for same number
    print(i,j)          # of elements on both lists. Here 90 is ignored

#without using zip function

for i in range(len(l1)):
    print(l1[i],l2[i])