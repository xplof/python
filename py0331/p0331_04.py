# a_list=[1,2,3,4,5,6,7,8,9]
# a_list[5]=10

# #  슬라이싱 - 역순 출력
# print(a_list[::-1])

# # 값을 변경할때 1:2는 2의 위치값이 *포함*
# a_list[1:2]=[100,200]
# print(a_list)

# # 1차원 리스트
# aa=[10,20,30]

# # 2차원 리스트
# aa=[
#    [1,2,3,4],
#    [5,6,7,8],
#    [9,10,11,12]
# ]
# print(aa[0][2]) 

# a_list=[[1,2,3],[4,5,6],[7,8,9]]

# for i in range(3): #0,1,2
#     for j in range(3): #0,1,2
#         print(a_list[i][j],end="\t")
#     print()        
    

# 1 2 3 4 5
# 6 7 8 9 10
# 11 12 13 14 15
# 16 17 18 19 20
# 21 22 23 24 25

# a_list=[[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]

# for i in range(5):
#     for j in range(5):
#         print(a_list[i][j], end=" ")
#     print()

# # 랜덤으로 섞여진 리스트
# import random
# a_list=[i+1 for i in range(25)]
# random.shuffle(a_list)
# print(a_list)

# a_list=[i+1 for i in range(25)]

# 5x5리스트 초기화
# a_list=[[0]*5]*5 #얕은복사

# a_list=[[0]*5 for i in range(5)] #깊은복사
# for i in range(5):
#     for j in range(5):
#         a_list[i][j]=5*i+(j+1)
# print(a_list)


# 1.순차적 리스트 생성
# 2.리스트 섞기
# 3. 2차원 초기화 리스트 생성
# 4. 2차원 리스트에 랜덤리스트의 값을 입력 
# import random
# sample_list=[i+1 for i in range(25)]
# random.shuffle(sample_list) #랜덤리스트 


# 리스트 초기화방법1
# a_list=[[0]*5 for i in range(5)]
# for i in range(5):
#     for j in range(5):
#         a_list[i][j]=sample_list[5*i+j] #랜덤숫자가 들어감
        
# print(a_list)        

# for i in range(5):
#     for j in range(5):
#         print(a_list[i][j],end="\t")
#     print()


# 리스트 초기화 방법1
 a_list=[[0]*5 for i in range(5)]
 
# 리스트 초기화 방법2
sample_list=list() #리스트 초기화
for i in range(5):
    temp=[]
    for j in range(5):
        temp.append(j) #0,1,2,3,4
    sample_list.append(temp)#[[0,1,2,3,4]]
    
print(sample_list)


