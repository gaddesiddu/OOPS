class A:
    __privatedata = 10
    def method(self):
        print(self.__privatedata)
class B(A):
    def method(self):
        print(self.__privatedata)

a=A()
a.method()
b=B()
b.method()