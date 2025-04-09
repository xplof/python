#카드프로그램 - card객체
class Card:
    # self.shape
    # self.number
    #__str__
    pass
class CardFunc:
    #함수
    pass

# cardMain.py
# 카드리스트객체 호출
# 카드객체 45장 호출
# 각각 5장을 나눠준 다음, 비교해서 큰 수 가 승리하는 형태로 구현
class Main : pass

import random
clist=[]
sh=['clover','haert','diamond','spade']
no=['','a','2','3','4','5','6','7','8','9','10','j','q','k']  

#카드 생성
for i in range(52):
    clist.append({"shape":i//13, "no":i%13+1})
print(clist)

random.shuffle(clist)

mycard=[]
yourcard=[]

for i in range(5):
    mycard.append(clist[i])

for i in range(5,10):
    yourcard.append(clist[i])
    
print("내카드")
for i in mycard:
    