class Father:
    def method1(self):
        print("Father class")

class Child1(Father):
    def method2(self):
        print("child1 class")
class Child2(Father):
    def method3(self):
        print("child2 class")

c=Child1()
c.method1()
c.method2()
c2=Child2()
c2.method1()
c2.method3()

#one parent has mutliple child
