# 파일불러오기
# 1.open()
# 2.f.read()
# 3.f.close()
f=open("py0404/stu.txt","r",encoding="utf8")
# 여러줄이면 반복문 실행
students=[]
while True:
    data=f.readline()
    if not data : break
    s=data.strip().split(",")
    students.append({
        "no":int(s[0]),"name":s[1],"kor":int(s[2]),"eng":int(s[3]),
        "math":int(s[4]),"total":int(s[5]),"avg":float(s[6]),"rank":int(s[7])       
    })
f.close()
print(students)
