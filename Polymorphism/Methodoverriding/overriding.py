class Grand:
    def method(self):
        print("grand class")
class Parent(Grand):
    def method(self):
        print("parent class")

class Child(Parent):
    def method(self):
        #we can also call parent class by super().method().first prints parent class then child class
        print("child class")
c=Child()
c.method() #here it is overriding parent class.parent class is overriding grand class
p=Parent()
p.method() #it is overriding grand class