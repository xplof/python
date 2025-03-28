# 숫자 맞히기 프로그램
import random

# randint(1,111) - 1~111사이 랜덤숫자 1개 불러오기
lotto = random.randint(1,45)

lst=[]
# -------------
for i in range(10):
    in_num=int(input("1~45 숫자를 입력하세요 : "))
    lst.append(in_num)
    # 랜덤번호 입력번호 비교
    if lotto==in_num:
        print("축하합니다. 당첨입니다")
        break
    elif lotto>in_num:
        print(f"{in_num}보다 더 큰 수를 입력하세요")
    else:
        print(f"{in_num}보다 더 작은 수를 입력하세요")
        
    # ------------
    

print(f"로또번호 : {lotto}")
print(f"입력번호 : {lst}")