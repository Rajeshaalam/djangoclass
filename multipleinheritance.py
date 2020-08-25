class parent1:
    def display():
        print("parent1")
class parent2:
    def show1():
        print("parent2")
class child(parent1,parent2):
    def show2():
        print("child class")
obj=child
obj.display()
obj.show1()
obj.show2()
