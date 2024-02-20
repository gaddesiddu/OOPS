class Member:
    def __init__(self,fname,lname,email,mid,address,number,dateofjoin):
        self.fname=fname
        self.lname=lname
        self.email=email
        self.mid=mid
        self.address=address
        self.number=number
        self.dateofjoin=dateofjoin
    def getfullname(self):
        print(self.fname+' '+self.lname)
    def changeaddress(self, newaddress):
        self.address = newaddress #we are storing new_Add 
        print("successfully changed")
    def changenumber(self,newnum):
        self.number=newnum
        print("number updated")
class Faculty(Member):
    def __init__(self,fname,lname,email,mid,address,number,salary,subjectsteaching,dateofjoin):
        self.salary=salary
        self.subjectsteaching=subjectsteaching
        Member.__init__(self,fname,lname,email,mid,address,number,dateofjoin)
    def getsalary(self):
        print("your salary is",self.salary)
class Student(Member):
    def __init__(self,fname,lname,email,mid,address,number,subjectslearnt,GPA,dateofjoin):
        self.subjectslearnt=subjectslearnt
        self.GPA=GPA

        Member.__init__(self,fname,lname,email,mid,address,number,dateofjoin)

    def getGPA(self):
        print("your GPA is ",self.GPA)

s=Student("siddu","gadde","siddugadde@gmail.com",1,"hyd",98,5,9.8,22)
s.getGPA()
s.getfullname()
s.changeaddress("knr")



#no need of writting seperate class for faculty and student 
#duplicate code removal
#code reusability
#easy to add new features
#data redundancy
#easy to maintain
#run this code in python interpreter 