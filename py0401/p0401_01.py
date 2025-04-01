# 1차원 리스트
import random
s_list=[i for i in range(1,26)]
random.shuffle(s_list)
# random.random(), random.randint(), random.sample(), random.shuffle

# 2차원 리스트
my_list=[[0]*5 for i in range(5)]

# 1차원리스트 값-> 2차원 리스트 입력
for i in range(5):
    for j in range(5):
        my_list[i][j]=s_list[5*i+j] #5x + y

#화면출력
while True:
    print(" "*10,end="")
    print("[좌표 맞추기 프로그램]")
    print("-"*44)
    print("*   ㅣ",end="\t")
    for i in range(5):
        print(i,end="\t")
    print()
    print("-"*44)   
    for i in range(5): 
        print(f"{i}   ㅣ",end="\t")
        for j in range(5):
            print(my_list[i][j],end="\t")
        print()      

    print("-"*44)

    #좌표입력  
    # x= int(input("x좌표를 입력하세요 : "))
    # y= int(input("y좌표를 입력하세요 : "))

    # my_list[y][x]="X"
    
    # 번호입력 x표시 25개 전부 비교
    num= int(input("1~25 숫자를 입력하세요 : "))
    stop=0
    for i in range(5):
        for j in range(5):
            if my_list[i][j]==num:
                my_list[i][j]="X"
                stop=1
                break #가장 가까운 for문을 빠져나옴
        if stop==1: break        
            