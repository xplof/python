# fruits=['사과','배','딸기','바나나','멜론']

# for fruit in fruits:
#     print(fruit,end=" ")
    


fruits=['사과','배','딸기','바나나','멜론']
# 1.사과 2.배 3.딸기

# enumerate index번호 받기
for i,fruit in enumerate(fruits):
    if len(fruits)-1 != i:
        print("{}.{}".format(i+1,fruit),end=",")
    else: 
        print("{}.{}.".format(i+1,fruit))
        