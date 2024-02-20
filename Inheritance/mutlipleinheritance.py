class Father:
    def method1(self):
        print("Father class")

class Mother:
    def method2(self):
        print("mother class")
class Child(Father,Mother):
    def method3(self):
        print("child class")

c=Child()
c.method1()
c.method2()


#father <-> mother -> child class