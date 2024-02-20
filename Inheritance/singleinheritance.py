class Parent:
    def method1(self):
        print("parent class")
class Child(Parent):
    def method2(self):
        print("child class")

c=Child()
c.method1()
#parent class -> child class
#child class can access parent class
#parent class cannot access child class
