class A:
    _protecteddata = 10
    def method(self):
        print(self._protecteddata)
class B(A):
    def method(self):
        print(self._protecteddata)

a=A()
a.method()
b=B()
b.method()

#B class is accessing protected data which is used by inheritance concept
#underscore is must for protected access