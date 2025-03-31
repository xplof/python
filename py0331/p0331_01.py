# 구구단
# for i in range(2,10):
#     print(f"{i}단")
#     for j in range(1,10):
#         print("{}x{}={}".format(i,j,i*j))
#         print()        

# a_list=[1,2,3,4,5]
# sum=0
# for i in a_list:
#     sum=sum+i
# print(sum)

b_list=[]


# a변수와 b변수는 다른 변수임
a=10; b=0
a=b
b=1000
print("a : ",a)
print("b : ",b)



# a_list와 b_list는 다른 리스트인가?ㄴ

# 주소값 복사 = 얕은 복사
a_list=[1,2,3,4,5]    
b_list=a_list

b_list[1]=200
print(a_list)

# 새롭게 복사 - 깊은 복사
a_list=[1,2,3,4,5]    
b_list=[*a_list] #중요

b_list[1]=200
print(a_list)

