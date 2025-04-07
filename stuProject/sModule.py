class Student:
    count=1
    
    def __init__(self,name,kor,eng,math):
        self.no = Student.count
        self.name=name
        self.kor=kor
        self.eng=eng
        self.math=math
        self.rank=0
        Student.count +=1
        
    def __str__(self):
        return f"{self.no},{self.no},{self.no},{self.no},{self.no},{self.no},{self.no},{self.no}"

class Students:
    def __init__(self):
        self.students=[]
    
    def add(self,s):
        self.students.append(s)
    def __str__(self):
        p
    