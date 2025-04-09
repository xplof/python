a="홍길동님! 안녕하세요. 반갑습니다. 안녕 반가워. 안녕안녕"
# a.find() #for 문을 사용해서 안녕이 몇번나오는지 개수를 출력
i=0
count=0
while True:
    num=a[i:].find("안녕")
    if num !=-1: #안녕이라는 글자가 있는경우
        count+=1 #개수1증가
        i+=num+1
    else: break
print("개수 :",count)

# print(a[0:].find("안녕"))
# print(a[0+6+1:].find("안녕"))
# print(a[0+6+1+13+1:].find("안녕"))
# print(a[0+6+1+13+1+7+1:].find("안녕"))
# print(a[0+6+1+13+1+7+1+1+1:].find("안녕"))


# n= a.count("안녕")
# print(n)
# count=0
# for i in range(len(a) - 1):  # 문자열의 끝에서 두 번째 인덱스까지 확인
#     if a[i:i+2] == "안녕":  # 두 문자씩 비교
#         count += 1

# print(f'"안녕"은 {count}번 나옵니다.')





# if "안녕"in a:
#     print("안녕이라는 글자가 있습니다")
# print(a.find("안녕"))