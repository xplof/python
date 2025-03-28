# i=0
# while i<10:              # 조건이 맞을때만 반복. 무한반복 가능
#     print(i,end="")    
#     i += 1 #1씩 증가
# print()                  # 설정한 횟수만큼 반복
# for j in range(10):
#     print(j,end="")
    
# while True:
#     print(i)
#     i+=1

# lst=[1,5,10,9,8,20]

# a=5
# if a in lst: #lst안에 a가 있냐?
#     print(f"{a}가 존재합니다")
# else: print(f"{a}가 존재하지 않습니다.")

# 입력한 숫자를 5번 반복해서 리스트에 추가하는 프로그램 구현

# for i in range(10):
    
#     # num이 lst에 있는지 확인해서 없으면 입력, 있으면 제외
        
lst=[]
i=1
while i<=10:
    num=int(input(f"{i}번째 숫자를 입력하세요 : "))
    if num not in lst:
       lst.append(num)
       i+=1
            
        

print(lst)