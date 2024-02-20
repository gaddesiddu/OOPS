class Grand:
    def method1(self):
        print("grand class")
class Parent1(Grand):
    def method2(self):
        print("parent1 class")
class Parent2:
    def method3(self):
        print("parent2 class")
class Child(Parent1,Parent2):
    def method4(self):
        print("child class")

c1=Child()
c1.method1()
c1.method2()
c1.method3()
c1.method4()
#combination of more than 1 inheritance
#Grand to Parent is single inheritance
#parent1, parent2 to child is multiple inheritance 
#grand to parent to child is multilevel inheritance