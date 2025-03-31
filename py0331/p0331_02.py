# index 번호를 넣으려면 enumerate사용. 중요
# a_list=[273,10,5,9,100,1000,50]
# for idx,value in enumerate(a_list):
#     print(f"{idx+1} : {value}") 
    
    
# #리스트- append로 추가하는 방법
# a_list=[]

# for i in range(1,11):
#     a_list.append(i)
# print(a_list)

# #리스트 내포 - 파이썬에서만 가능
# a_list=[i for i in range(1,11)]  
# print(a_list)

# # append, inset, extend
# a_list=[1,2,3]
# a_list.append(4) #맨 뒤에 4 추가

# a_list.insert(1,100) #지정한 위치에 값 추가

# a_list.extend([100,200,300]) #리스트를 추가
# print(a_list)


# 삭제 - del, pop, remove, clear
a_list=[1,2,3,4,5]
del a_list[2] #위치값 삭제
print(a_list)

a_list.pop() #맨 뒤 삭제, 특정위치 삭제 가능
print(a_list)

a_list.remove(1)
print(a_list) #데이터값으로 삭제

a_list.clear() # 전체삭제
print(a_list)

       