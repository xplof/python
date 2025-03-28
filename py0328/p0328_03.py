# 반복문으로 1-10출력
# for i in range(1,11):
#     print(i)
    
# a=1123
# if a>5 and a<10:
#     print(a)
# if a>5 or a<10: print(a)

# lst=[1,2,3,4,5]
# print(lst[2])
# print(lst[0:5]) #[시작위치:끝나는위치-1]슬라이싱 !!!!!!!
# print(lst[:3]) #[:끝나는위치-1]- 처음부터시작
# print(lst[2:]) #[시작위치:] - 끝까지
# print(lst[::2]) #2개씩 증가해서 출력
# print(lst[::3])
# print(lst[::-1]) #역순으로 출력 !!!!!!!
# print(lst[:-1]) #마지막기준 출력x !!!!!!!!!

# a="안녕하세요"
# print(a[2])
# print(a[:3])
# print(a[::-1])
# print(a[:7]) #슬라이싱은 없는 값 출력시 에러 x
# print()

# print(len(lst)) #len - 리스트 개수 확인
# print(lst[:len(lst)-1])
# print(len(a)) #문자열 길이

# for i in range(1,11,2):
#     print(i,end="입니다. ")
    
    
    
# 합계가 100이 넘는 숫자의 위치는?
sum=0
i=678 #바깥에 빼주기
for i in range(1,100+1):
    sum=sum+i
    print("i:{}, sum : {}".format(i,sum))
    if sum>=100: break
    
print("합계 : {}".format(sum))
print("sum이 100이 넘었을 때 i의 값 : ",i)
print("합계가 100이 넘었을때 sum의 값 : ",sum)
