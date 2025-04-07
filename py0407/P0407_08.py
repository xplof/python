# class Student:
#     #인스턴스 변수 - 객체선언시 각각 변수들이 존재 : 공용으로 사용됨
#     # no=1
#     # name="" 
    
#     #생성자함수
#     count=1 #클래스변수 : 모든 객체가 공용으로 사용하는 변수
    
    
#     def __init__(self,name,kor,eng,math):
#         self.no=Student.count
#         self.name=name
#         self.kor=kor
#         self.eng=eng
#         self.math=math
#         self.total=kor+eng+math
#         self.avg=self.total/3
#         self.rank=0
#         Student.count+=1 #객체선언 할때마다 1증가
#     def __str__(self):
#         return f"{self.no},{self.name},{self.kor},{self.eng},{self.math},{self.total},{self.avg:.2f},{self.rank}"
#     # s=Student("홍길동",100,100,99) #매개변수가 있는 생성자 객체선언
# # print(s.no,s.name,s.kor,s.eng)
# # s2=Student("유관순",99,99,98)
# # print(s2.no,s2.name,s2.kor,s2.eng,Student.count)
# # print(s2.no,s2.name,s2.kor,s2.eng)
# s=Student("홍길동",100,100,99)
# print(s)
        

# s=Student() #기본생성자
# s.name="홍길동"
# print(s.no,s.name)

# s2=Student()
# s2.no=2
# s2.name='이순신'
# print(s2.no,s2.name)
class Student:
    # 인스턴스 변수 - 객체선언시 각각 변수들이 존재 : 공용으로 사용안됨.
    # no = 1
    # name = "" # 인스턴스 변수
    count = 1   # 클래스변수 - 모든 객체가 공용으로 사용하는 변수
    # 생성자함수
    def __init__(self,name,kor,eng,math):
        self.no = Student.count       # 인스턴스변수
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math
        self.total = kor+eng+math
        self.avg = (kor+eng+math)/3
        self.rank = 0
        Student.count += 1           # 1증가
    def __str__(self):
        return f"""{self.no},{self.name},{self.kor},{self.eng},{self.math},{self.total},{self.avg:.2f},{self.rank}"""
class Students:
    def __init__(self):
        self.students = []
    def add(self,s):
        self.students.append(s)
    def __str__(self):  # 리턴이 무조건 문자열을 해줘야 함.
        for s in self.students:
            print(s.no,s.name,s.kor,s.eng,s.math,s.total,s.avg,s.rank)
        return ""