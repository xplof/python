# 카드 spade-4, diamond-3, heart-2, clover-1
# 번호 1-a,2,3,4,5,6,7,8,9,10,11-j,12-q,13-k
# 카드 1장 - 카드모양, 번호
# 카드모양 4개
# 번호 13개
# 카드 총 개수 : 52개

# 리스트-딕셔너리
# clist=[
#     {"shape":'spade','no':1},
#     {"shape":'spade','no':2}
# ]
import random
clist=[]
sh=['Clover','Heart','Diamond','Spade']
no=['','A','2','3','4','5','6','7','8','9','10','J','Q','K']

# 카드 생성
for i in range(52):
    clist.append({"shape": i//13, "no":i%13+1})

# 카드 랜덤으로 섞기
random.shuffle(clist)

#mycard, yourcard
# 5장을 입력
mycard=[]
yourcard=[]

# 카드 5장씩 배분
for i in range(5):
    mycard.append(clist[i])
    
for i in range(5,10):
    yourcard.append(clist[i])
  
# 내카드출력
print("[내 카드]")
for i in mycard:
    print(f"[{sh[i['shape']]},{no[i['no']]}]")  
print("[상대 카드]")
for i in yourcard:
    print(f"[{sh[i['shape']]},{no[i['no']]}]")

# 내카드 상대카드 비교 후 승리 패배 무승부 출력
score=[0]*5
for i in range(5):
    if mycard[i]['no']>yourcard[i]['no']:
        score[i]=2
    elif mycard[i]['no']<yourcard[i]['no']:
        score[i]=1
    else:
        score[i]+=0
        
print("[카드 승부 확인]")
print(f"승리 : {score.count(2)}, 패배 : {score.count(1)}, 무승부 : {score.count(0)}")

print("[승리카드]")
for i,c in enumerate(mycard):
    if score[i]==2:
        print(f"[{sh[c['shape']]},{no[c['no']]}]",end=",") 

# print("[내 카드]")
# for i in mycard:
#     print(f"[{sh[i['shape']]},{no[i['no']]}]")  
# print("[상대 카드]")
# for i in yourcard:
#     print(f"[{sh[i['shape']]},{no[i['no']]}]")

# # 내카드 상대카드 비교 후 승리 패배 무승부 출력
# score={"mywin":0,"youwin":0,"draw":0}
# for i in range(5):
#     if mycard[i]['no']>yourcard[i]['no']:
#         score['mywin']+=1
#     elif mycard[i]['no']<yourcard[i]['no']:
#         score['youwin']+=1
#     else:
#         score['draw']+=1
        
# print("[카드 승부 확인]")
# print(f"승리 : {score['mywin']}, 패배 : {score['youwin']}, 무승부 : {score['draw']}")

# 승리 카드 출력
# print(f"승리 카드 : {win}")

# # 패배 카드 출력
# print(f"패배 카드 : {win}")
# # 무승부 카드 출력
# print(f"무승부 카드 : {win}")



#전체카드 출력
# for c in clist:
    # print(c['shape'],c['no'])/
    

# import math
# import random

# # 0.0000000000000000<= x <1.0000000000000000
# print(random.random())
# print(random.randint(1,45)) #1~45 숫자 중 1개 랜덤추출

# # 리스트에서 1개 랜덤추출
# a_list=[1,2,3,4,5]
# print(random.choice(a_list))
# # 리스트에서 개수만큼 중복없이 랜덤추출
# print(random.sample(a_list,2))

# # 리스트 순서를 랜덤으로 섞기
# random.shuffle(a_list)
# print(a_list)

# # a=3.141592
# b=3.51582
# print(math.ceil(a)) #4 #올림
# print(round(b,2))#반올림,자릿수지정
# print(math.floor(a)) #버림

# # a에서 ceil올림해서 2자리까지표시
# # a*100/100
# # a*100 #314.159
# print(math.ceil(a*100)/100)

# # b에서 소수점5자리에서 ceil올림해서 4자리표시
# print(math.ceil(b*10000)/10000)

# # math안에 있는 함수를 출력
# print(dir(math))
