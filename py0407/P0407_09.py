class Stu:
    def __init__(self,no,name,kor,eng):
        self.__no=no
        self.__name=name
        self.__kor=kor  #__언더바 2개 : 캡슐화(접근제한)
        self.__eng=eng
        
    #@어노테이션 @property, @변수.setter - getter,setter만들어짐
    # @property
    # def kor(self):
    #     return self.__kor
    
    # @kor.setter
    # def kor(self,kor):
    #      if kor >=0 and kor<=100:
    #         self.__kor=kor
    
    
    #getter
    def getno(self):
        return self.__no
    def getName(self):
        return self.__name 
    def getkor(self):
        return self.__kor
    def geteng(self):
        return self.__eng
         
     #setter   
    def Setkor(self,kor):
        if kor >=0 and kor<=100:
            self.__kor=kor
        else: raise NotImplementedError("유효값x")
        
    def Seteng(self,eng):
        if eng >=0 and eng<=100:
            self.__eng=eng
        else: raise NotImplementedError("유효값x")
        
        
    def __str__(self):
        return f"{self.no},{self.name},{self.__kor},{self.eng}"
    
class Students:
    def __init__(self):
        self.students=[]

s=Stu(1,'홍길동',100,99)
s.__kor=200 #지역변수
print(s.no,s.name,s.__kor) #지역변수개념의 s.__kor의 값 출력
s.eng=300
s.Setkor(500)
print(s)