# 반복해서 리스트에 10개를 랜덤으로 입력시키는 프로그램 구현
# 중복 제외

# import random
# rst=[]
# i=0

# while i<6:
#     rn=random.randint(1,45)
#     if rn not in rst:
#         rst.append(rn)
#         i +=1
# print(rst)




# 랜덤 1~45번 숫자 6개를 ran list에 저장
# 입력받은 숫자 6개를 my list에 저장
# 랜덤번호
# 입력번호
# 당첨개수
# 

import random
ran_list=random.sample(range(1,45+1),6) #랜덤번호 6개리스트
my_list=[] #입력번호 저장리스트
lotto_count=0 #당첨개수
lotto_list=[] #당첨번호

i=0
while i<6:
    print(f"랜덤번호 : {ran_list}")  
    my_input=int(input(f"{i+1}번째 숫자를 입력하세요")) #입력번호
    if my_input not in my_list:
        my_list.append(my_input) #입력번호 추가
        i=i+1
        
#당첨 비교 프로그래밍 - 
 
# for j in range(6):
#      for k in range(6):
#          if ran_list[j]==my_list[k]:
#              lotto_count=lotto_count+1
#              lotto_list.append(my_list[k])
#              break
 
for j in range(6):
     if ran_list[j] in my_list:
             lotto_count=lotto_count+1
             lotto_list.append(my_list[j])
             
           
        
print(f"랜덤번호 : {ran_list}")   
print(f"입력번호 : {my_list}")      
print(f"당첨개수 : {lotto_count}")        
print(f"당첨번호 : {lotto_list}")        
  
