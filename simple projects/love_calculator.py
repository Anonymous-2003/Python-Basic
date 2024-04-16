
name1=input("Enter your name\n")
name2=input("Enter his/her name\n")
# l_name1=name1.lower() # lowers all the alphabets 
# l_name2=name2.lower()
name=name1.lower()+name2.lower()
true = str(name.count("t")+name.count("r")+name.count("u")+name.count("e"))
love = str(name.count("l")+name.count("o")+name.count("v")+name.count("e"))
total = true + love
print(f"your love score is {total}")

