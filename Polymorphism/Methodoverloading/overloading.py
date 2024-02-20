import multipledispatch
class A:
    @multipledispatch.dispatch(int,int)
    def add(self,a,b):
        print(a+b)
    @multipledispatch.dispatch(int,int,int)
    def add(self,a,b,c):
        print(a+b+c)
    @multipledispatch.dispatch(str,str)
    def add(self,a,b):
        print(a+' '+b)
    @multipledispatch.dispatch(float,float,float,float)
    def add(self,a,b,c,d):
        print(a+b+c+d)

a=A()
a.add(2,3)
a.add(1,2,3)
a.add("siddu","gadde")
a.add(0.1,0.2,0.3,0.4)

#method overloading does not possible in python.so, we implement by importing multipledispatch module
#features are flexibility,readability,less complexity

"""we can also perform this task by

class A:
    def add(self,*args):
        if args:
            sum= type(args[0])()
            for i in args:
                sum+=i
                return sum
a=A()
print(a.add(1,3))
print(a.add(1,3,4))
"""