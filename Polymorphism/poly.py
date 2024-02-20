class A:
    def hi(self):
        print("hello")
class B:
    def hi(self):
        print("hello class b")


def poly(obj):
    obj.hi()

a=A()
b=B()
poly(a)
poly(b)

#using single function we are calling two classes