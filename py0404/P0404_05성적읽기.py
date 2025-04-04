# with 함수 사용시 f.close() 생략
# 모든 학생 영어점수 +1을 하시오.
# students = [
#     {"no":1,"name":"홍길동","kor":100,"eng":100,"total":300},
#     {"no":2,"name":"유관순","kor":100,"eng":100,"total":299},
#     {"no":3,"name":"이순신","kor":100,"eng":100,"total":299},
# ]
# stu.txt -> 영어성적을 +1 증가하고 합계도 +1증가해서
# 전체리스트를 출력하시오.
# 1,홍길동,100,99,199
# 2,유관순,90,90,180
# 3,이순신,80,81,161
f = open("py0404/stu.txt","r",encoding="utf-8")
students = []
while True:
    line = f.readline()
    if not line: break
    print(line.strip())
    s = line.strip().split(",") # list타입으로 변경해서 전달
    # list수정
    print("{},{},{},{},{}".format(*s))
    students.append({"no":int(s[0]),"name":s[1],"kor":int(s[2])
                     ,"eng":int(s[3])+1,"total":int(s[4])+1})
f.close()
for ss in students:
    print(ss)
print(students)
# students = [
#     {"no":1,"name":"홍길동","kor":100,"eng":100,"total":300},
#     {"no":2,"name":"유관순","kor":100,"eng":100,"total":299},
#     {"no":3,"name":"이순신","kor":100,"eng":100,"total":299},
# ]
# ['1', '홍길동', '100', '99', '199']
# f = open("py0404/stu2.txt","r",encoding="utf-8")
# line = f.readline()
# a_list = line.strip().split(",")
# print(a_list)
# print(int(a_list[3])+1)
# f.close()
# while True:
#     line = f.readline()
#     if not line: break
#     a_list = line.split(",") # list타입으로 변경해서 전달
# print(a_list)
# print(int(a_list[3])+1)
# with open("py0404/stu.txt","r",encoding="utf-8") as f:
#    for line in f:
#      print(line.strip())
