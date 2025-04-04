# 파일 입출력: 파일열기,파일읽기,파일쓰기,파일닫기
# 파일열기 : 3가지모드 - r:읽기모드 w쓰기모드 a추가모드 b이진파일-파일복사
# f=open("a.txt","r") #읽기
# f=open("a.txt","w") #쓰기
# f=open("a.txt","a") #추가

f=open("py0404/news.txt","r",encoding="utf-8")
for line in f:
    print(line.strip())
f.close    
# lines=f.readlines()
# print(lines)

# 파일읽어오기 - 절대경로
f=open("C:/workspace/python/a.txt","r",encoding="utf-8")
f=open("py0404/b.txt","r",encoding="utf-8") #폴더 안


# 파일읽기 readlines() : 모두 읽어오기
f=open("a.txt","r",encoding="utf-8")
lines=f.readlines() #모두읽기
for line in lines: #리스트형태로 저장
    print(line.strip())
f.close()    

while True:
    line=f.readline()
    if not line : break
    print(line.strip())

# # 파일읽기-r
# f=open("a.txt","r",encoding="utf-8")
# print(type(f))
# for line in f:
#     print(line.strip())
# f.close    