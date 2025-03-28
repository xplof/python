# 두 수를 입력받아 두 수 사이의 합계를 구하시오

# n1=int(input("숫자를 입력하세요 : "))
# n2=int(input("숫자를 입력하세요 : "))

# n=0
# for i in range(n1,n2+1):
#     n = n+i
#     if n1>n2:
#         c=n1 
#         n1=n2
#         n2=c
#         print("i : {}, sum : {}".format(i,sum))
    
# print("{}에서 {}까지의 합계 : {} ".format(n1,n2,n))

# 구구단 출력
# for i in range(2,9+1):
#     print("[{}단]".format(i))
#     for j in range(1,9+1):
#         print("{}x{}={}".format(i,j,i*j),end=",")
#     print()
    
# 시작단과 끝단을 입력받아 출력

n1=int(input("단을 입력하세요 : "))
n2=int(input("단을 입력하세요 : "))

if n1>n2:
    n1,n2=n2,n1
    
for i in range(n1,n2+1):
    print("[{}단]".format(i))
    for j in range(1,9+1):
        print("{}x{}={}".format(i,j,i*j))
       
    