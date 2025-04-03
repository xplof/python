from stu_func import* #각각의 함수명 가져옴

students=[ #리스트타입
    {"no":1,"name": "홍길동","kor":100,"eng":100,"math":100,"total":300,"avg":100,"rank":1},
    {"no":2,"name": "유관순","kor":100,"eng":100,"math":99,"total":299,"avg":99.67,"rank":1},
    {"no":3,"name": "이순신","kor":100,"eng":100,"math":99,"total":299,"avg":99.67,"rank":1}
]

# 1.학생성적입력
def stu_rank(students):
    print("등수처리")
    for s in students:
        num=1
        for ss in students:
            id s['total']<ss['total']:
                num+=1
        s['rank']=num
    print("등수처리 완")
