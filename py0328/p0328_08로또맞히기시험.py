import random

# 랜덤 1-45번까지 숫자 6개 ran_list 저장
# 입력받은 숫자 6개를 my_list 저장을 시키는 프로그램을 구현하시오.

# 랜덤번호 6개리스트
my_list = []  # 입력번호 저장리스트
lotto_count = 0  # 당첨개수
lotto_list = []  # 당첨번호
ran_list = random.sample(range(1,45+1),6)

i = 0
while i<6:
    print("랜덤번호 : {}".format(ran_list)) 
    my_input = int(input("{}번째 숫자를 입력하세요.".format(i+1))) #입력번호
    if my_input not in my_list:
        my_list.append(my_input) #입력번호 추가
        i = i + 1
        
# 당첨 비교 ran_list, my_list
# for j in range(6):
#     for k in range(6):
#         if ran_list[j] == my_list[k]:
#             lotto_count = lotto_count + 1
#             lotto_list.append(my_list[k])
#             break
for j in range(6):
    print("확인 : ",ran_list[j])
    if ran_list[j] in my_list:
        lotto_count = lotto_count + 1
        lotto_list.append(ran_list[j])
        
print("랜덤번호 : {}".format(ran_list))        
print("입력번호 : {}".format(my_list))        
print("당첨개수 : {}".format(lotto_count))        
print("당첨번호 : {}".format(lotto_list))        




# 반복을 해서 , ran_list 10개를 입력시키는 프로그램을 구현하시오.
# 단, 같은 숫자가 들어가지 않도록 하시오.
 
# ran_list = []
# i = 0
# while i<6:
#     ran_input = random.randint(1,45)
#     if ran_input not in ran_list:
#         ran_list.append(ran_input)
#         i = i + 1

# print(ran_list)