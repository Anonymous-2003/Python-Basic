#Stack operation->last in / first out

# 1.push    ->inserting an element
# 2.pop     ->deleting an element(last element)
# 3.peek    ->displaying last element
# 4.display ->displaying list


l = []
while True:
    c=int(input("""
1.Add element to list
2.Remove last element from the list
3.Display last element 
4.Display list
5.Exit
            
Enter your choice:"""))

    if c == 1:
        n = input("Enter you want to push:")
        l.append(n)
        print("Adding to the list.....")
    elif c==2:
        if len(l)==0:
            print("Empty list....")
        else:
            print("popping...")
            p = l.pop
    elif c == 3:
        if len(l)==0:
            print("Empty list....")
        else:
            print(f"last stack value is {l[-1]}")
    elif c==4:
        if len(l)==0:
            print("Empty list....")
        else:
            print(l)
    elif c==5:
        break
    else:
        print("Invalid input")


