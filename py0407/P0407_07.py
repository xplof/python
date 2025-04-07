class Car:
    speed=0
    tire=4
    door=5
    def speedup(self,s):
        self.speed+=s
        print("현재 속도 :",self.speed)
        
class Sedan(Car):
    color="red"
    

c=Car()    
# print(c.giretype) #없는변수출력시 에러

a=Sedan()
print(a.speed)