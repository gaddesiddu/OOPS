class Grand:
    def method1(self):
        print("grandparent class")

class Parent(Grand):
    def method2(self):
        print("parent class")
class Child(Parent):
    def method3(self):
        print("child class")

c=Child()
c.method1()
c.method2()
c.method3()

#grandparent -> parent class -> child class