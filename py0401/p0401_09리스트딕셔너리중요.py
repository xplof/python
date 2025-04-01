# # # set -> 중복을 제거해서 키를 확인
# # myset1={1,2,2,3,3,3,5,5,7}
# # print(myset1)

# # menu_list=['삼각김밥','바나나','삼각김밥','사과','바나나','도시락','삼각김밥']
# # print(set(menu_list)) #list타입을 set타입으로 변경해서 확인


# # format함수 천단위 표시
# list=[1,2,3,4,5]
# # list2=['10,100','10,200','10,300','10,400','10,500']
# # list2=[i+100 for i in list]
# list2=["{:,d}".format((i+100)*100) for i in list]
# print(list2)

# # 리스트 내포 : if 조건절을 넣을 수 있음
# n_list=[i for i in range(1,51) if i%2==1]
# print(n_list)

# # 2개의 리스트 출력 가능.
# name_list=['홍길동','유관순','이순신','강감찬','김구']
# t_list=[100,99,89,79,100]
# for n,t in zip(name_list,t_list):
#     print(f"{n} : {t}")
    
# students={"no": 1, "name":"홍길동",'kor':100 }
# for key,value in students.items():
#     print(f"{key} : {value}")

name_list=['홍길동','유관순','이순신','강감찬','김구']
t_list=[100,99,89,79,100]

# zip()- 2개 리스트를 합치는 것. list or dict타입으로 변경 가능
print(list(zip(name_list,t_list)))  
print(dict(zip(name_list,t_list)))
# [
#     ['홍길동',100],
#     ['유관순',99]       #튜플과 리스트의 차이점 : 튜플은 수정 불가
    
# ]

# tuple_list=list(zip(name_list,t_list))