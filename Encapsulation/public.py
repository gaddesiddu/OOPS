class A:
    publicdata = 10
    def method(self):
        print(self.publicdata)
class B(A):
    def method(self):
        print(self.publicdata)


b=B()
b.method()

#B class is accessing public data which is used by inheritance concept