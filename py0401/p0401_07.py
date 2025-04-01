# 딕셔너리 생성
dic1={1:"a", 2:"b", 3:"c"}
print (dic1)

students_list=[1,"홍길동",100]
students={"no": 1, "name":"홍길동",'kor':100 }
print (students)

student1={'학번':1000,'이름':'홍길동','학과':'컴퓨터학과'}

# 딕셔너리 추가
dic={}
dic['no']=1
dic['name']='홍길동'
dic['kor'] = 100
print(dic)

# 딕셔너리 삭제
del dic['no'] #del키로 삭제
print(dic)

# 딕셔너리 수정
dic['name']='홍길동'
print(dic)

# 딕셔너리 출력
# print(dic['total']) # 없는 키값을 입력하면 에러
print(dic.get('total')) #없으면 none

print(dic.keys()) #key값을 리스트 형태로 출력
print(dic.values()) #value값을 리스트 형태로 출력
print(dic.items()) #('name','이순신') 튜플형태로 출력

# 전체출력 - 키, 값 모두 출력
for i,value in enumerate(dic):
    print(f"{i} : {value}")
    
# 키를 돌려줌
for key in dic:
    print(key) #키 출력
    print(dic[key]) # 값 출력
    
# 존재하는지 확인
if 'name' in dic:
    print("키 값이 존재합니다.")

if 'no' in dic:
    print(f"no : {dic['no']}")
else: 
    print("no 키는 존재하지 않습니다.")        


# number=[273,103,5,32,65,9,72,800,99]

# # 100 이상의 숫자만 출력하라
# # 그 합도 구하라
# sum=0
# for i in number:
#     if i>=100:
#         print(i)
#         sum=sum+i
#     else: pass    
# print(sum)    

# # 자릿수와 값을 구하라
# for n in number:
#     length=len(str(n))
#     print(f"자릿수 : {length}, 값 : {n}")