# for i in range(10): #10번 반복
#     print(i)
    
# i=0
# while i<10:
#     print(i)
#     i=i+1

# 10번의 숫자를 입력받아 합계를 구하시오.

# n1=int(input("숫자를 입력하세요 : "))
# sum=0
# i=0
# for i in range(10):
#     n1=int(input("숫자를 입력하세요 : "))
#     sum=sum+n1    
# print(sum)

# j=0
# sum2=0
# while j<10:
#     num=int(input("숫자를 입력하라 : "))
#     sum2=sum2+num
#     j=j+1
# print(sum2)    

# 로또 프로그램
# 6개 랜덤숫자, 6개 입력숫자 
# lotto=[i+1 for i in range(45)] #1,2,3...45
# my_input=[]


# import random
# lotto_input=random.sample(lotto,6) #리스트에서 중복없이 6개 가져오기

# # for i in range(6):
# #     lotto.append(random.randint(1,45)) #중복가능

# # random.shuffle(lotto) #전체 무작위로 섞기

# for i in range(6):
#     num=int(input("숫자를 입력하세요 : "))
#     my_input.append(num)    

# print("로또번호 : ",lotto_input)
# print("입력번호 : ",my_input)    


# ran_list=random.sample(range(1,101),6)


# random.rando()함수 : 0<= x <=1 의 랜덤 실수를 가져옴
# import random
# print(random.random()) #0.000000000<= 1.00000000000
# print(int(random.random()*10)+1) # 1부터 10까지
# print(int(random.random()*10)+0) # 0부터 9까지
# print(random.randint(1,10))

# a_list=[i+1 for i in range(100)]

# a_list에서 홀수의 합계는?
# a_list%2==1
# sum=0 #합계변수 선언
# for i in a_list:
#     if i%2==1: #홀수면
#         sum=sum+i #홀수를 합계변수에 더함 
# print(sum) 

       
#  1~100 오름차순으로 숫자의 합이 200이 넘을때의 숫자는?

# a_list=[i+1 for i in range(100)]
# sum=0
# for i in a_list:
#        sum=sum+i
#        if sum>200: break
# print("200이 넘을 때의 숫자 : {}, 합계 : {}".format(i,sum))
# print("200전의 숫자 : {} ".format(sum-i))       



# 입력한 숫자의 합이 50을 넘으면 프로그램을 종료하고 총합을 구하시오
# 입력한 숫자 중 5의 배수는 제외

# sum=0
# in_list=[]
# while True:
#     n1=int(input("숫자를 입력하세요 : "))
#     in_list.append(n1)
#     sum=sum+n1
#     if sum>50:break
#     elif sum%5==0: continue #실행을 1번 중지
# print("합계 : {}".format(sum))  
# print("입력한 숫자들 : {}".format(in_list)) 



# # continue - 그 위치에서 중지 후 다시 for문 실행
# # 1번부터 10번까지 진행중 1,2,3continue제외 ,4,5,6,7,8,9,10실행(총 9번)

# # break - 반복문 완전 중지
# # 1,2,3break - 반복문 끝

# # pass -
# # 1,2,3pass 4,5,6,7,8,9,10 10번을 실행 

# sum=0
# in_list=[]
# while True:
#     in_list.append(n1)
#     sum=sum+n1
#     if sum<50:
#         n1=int(input("숫자를 입력하세요 : "))
#         if n1%5==0:
#             print(f"입력한 숫자 : {n1}, 5의 배수 제외!")
#             continue #실행을 1번 중지
#     else : break    
    
# print("합계 : {}".format(sum))  
# print("입력한 숫자들 : {}".format(in_list)) 

# for i in range(10):
#     if i%2==0:continue
#     print(i)
    
for i in range(10):
     for j in range(i):
         print("*",end="")   
     print()     
        
        
