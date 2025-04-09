#숫자맞추기
import random
flist=[i+1 for i in range(25)]
random.shuffle(flist)

alist=[[0]*5 for i in range(5)]
for i in range(5):
    for j in range(5):
        alist[i][j]=flist[5*i+j]


while True:
    print("좌표맞추기 프로그램")
    print("-"*44)
    print("*   ㅣ",end="\t")
    for i in range(5):
        print(i, end="\t")
    print()
    print("-"*44)
    for i in range(5):
        print(f"{i}   ㅣ",end="\t")
        for j in range(5):
            print(alist[i][j],end="\t")
        print()
    
    
    num=int(input("1~25번 숫자를 입력하세요 : "))
    
    for i in range(5):
        for j in range(5):
            if alist[i][j]==num:
                alist[i][j]="X"