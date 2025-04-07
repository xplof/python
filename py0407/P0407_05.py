# # 클래스 - 변수 함수 집합체 : 변수에 대한 그룹핑 kor,eng,math
# # list, dict타입 - 함수까지   

# # 입력받을떄 처리 수정할때 직접처리
# # 특정데이터값이 들어왔을떄 잘못된데이터는 입력이안되도록 구현

class Car:
    def __init__(self,color,tire,door): #생성자 __init__
        self.color=color #self.color : Car변수, color:요청받은변수
        self.tire=tire
        self.door=door
        self.speed=0

    #속도올리기
    def speedup(self,s):
        self.speed+=s
    def speeddown(self,s):
        self.speed_=s
 
 #생성자를 사용한 객체선언과 동시에 데이터 입력
c=Car("red",5,4)
c2=Car("blue",5,5)        

        

# a=Car() # 클래스 객체선언
# a.speed=50 #클래스 변수에 값 입력 : 참조변수.변수명
# print(a.speed) #클래스 변수 값 출력

# # 함수 사용방법 
# a.speedup(20)  #참조변수.함수명
# print(a.speed) #클래스 변수 값 출력

# alist2=alist #얕은복사


# 기본형태 객체선언 후 데이터 입력
# #red,5,4
# # 차 구매 후 색칠,문짝,타이어 수정
# a2=Car() #깊은복사. 각각의 변수,함수가 됨
# a2.color="red"
# a2.tire=5
# a2.door=4

# #blue,5,5
# a3=Car()
# a3.color="blue"
# a3.tire=5        
# # a3.door=5        