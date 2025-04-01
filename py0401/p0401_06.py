a_list = [1,2,3,4,"홍길동",5,11,12,13]

# 리스트 삭제 명령어
del a_list[0] #인덱스 번호로 삭제
a_list.pop() #마지막 데이터 삭제
a_list.pop(2) #인덱스 번호 삭제
a_list.remove(2) #2라는 값을 삭제
a_list.remove("홍길동")
a_list.clear #모두 삭제

# 리스트 추가
a_list.append(1) #마지막에 1추가
a_list.insert(0,"홍길동") #인덱스 위치에 데이터 추가
a_list.extend([10,11,12]) #마지막에 리스트 추가

# 리스트 수정
a_list[0]="유관순"

# 리스트 출력
for a in a_list:
    print(a)
    
# 리스트에 여러 데이터 묶음도 추가 가능- 데이터 종류 상관 x    
a_list.append(['ㅋ,d,f,r']) 

# 리스트 길이
print(len(a_list))

# 개수 확인
s_list=[1,2,3,1,2,2,1,2,3,4,5,7,7,7]

print("{} : {}".format(1,s_list.count(1)))

num=0
for s in s_list:
    if s==1:
        num+=1
print("{} : {}".format(1,num))

#리스트 정렬
s_list.sort() #순차정렬, 오름차순
print(s_list)

s_list.reverse() #내림차순   