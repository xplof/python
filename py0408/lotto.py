#로또
import random

ran_list=random.sample(range(1,46),6)
my_list=[]
lotto_count=0
lotto_list=[]

i=0
while i<6:
    my_input=int(input(f"{i+1}번째 숫자를 입력하세요"))
    if my_input not in my_list:
        my_list.append(my_input)
        i+=1

for j in range(6):
    if ran_list[j] in my_list:
        lotto_count+=1
        lotto_list.append(my_list[j])

print(f"랜덤번호 : {ran_list}")
print(f"입력번호 : {my_list}")
print(f"당첨개수 : {lotto_count}")
print(f"당첨번호 : {lotto_list}")