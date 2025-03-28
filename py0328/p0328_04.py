# 1,3,5,7,9,,,99. 1~100 홀수만 더해서 합계를 구하시오
# n=0
# for i in range(1,101,2):
#     n=n+i
# print("합계 : ",n)


# 3의 배수면서 5의 배수
sum=0
for i in range(1,101):
    if i%3==0 and i%5==0:
        sum=sum+i
        print("i : {}, sum : {}".format(i,sum))
print("합계 : ", sum)



sum=0
for i in range(1,101):
    if i%3==0 or i%7==0:
        sum=sum+i
        print("i : {}, sum : {}".format(i,sum))
print("합계 : ", sum)