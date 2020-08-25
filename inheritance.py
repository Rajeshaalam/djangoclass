class parent:
    a,b=10,20
    def dispaly():
        print("Iam from parent class")
class child1(parent):
    c,d=7,8
    def show():
        print("Iam from child1 class")
class child2(child1):
    def show1():
        print("Iam from child2 class")
obj=child2
obj.dispaly()
obj.show()
obj.show1()
