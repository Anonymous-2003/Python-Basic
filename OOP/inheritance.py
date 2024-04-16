class A:
    def show(self):
        print("In class A")
class B():
    def show1(self):
        print("In class B")
class C(A,B):   # inheriting both A and B in C
    def show2(self):
        print("In class C")
obj = C()
obj.show()
obj.show1()
obj.show2()