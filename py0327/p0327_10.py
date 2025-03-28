# 랜덤숫자 1~100 생성해서 정답 맞추는 프로그램 구현

# 1.랜덤숫자 생성
# 2. num list 생성
# 3. n 변수 생성
# 4. 10번 for문 생성
# 5. 입력된 숫자를 num list에 저장
# 6. 정답비교
# 7. 데이터 출력

num=[]
n=213
import random
rannum=random.randint(1,100)
for n in range(1,11):
    innum=int(input("숫자를 입력하세요 : "))
    num.append(innum)
    if rannum==innum:
        print("정답입니다. 랜덤숫자 : {}".format(rannum))
        break
    elif innum>rannum:
        print("더 작은 수를 입력하세요")
    else:
        print("더 큰 수를 입력하세요")
print("도전 횟수 : {}".format(n))
print("입력된 숫자 : {}".format(num))
print("랜덤 숫자 : {}".format(rannum))
        
        
    
