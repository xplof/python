# 문서읽어오기 r
# 일반파일 읽어오기 -rb
f=open('py0404/a.jpg','rb') #파일 읽기
fdata=f.read()
f.close()
print("파일 읽어오기 완료")

# 이진파일은 용량이 클 수 있으므로 1byte씩 읽어오기
while True:
    fdata=f.read(1)
    if not fdata:break


# 문서저장 w a
# 파일저장 wb
# 폴더 존재 확인 : os.path.exists()
# 폴더 생성 : os.makedir(): 폴더1개 - c:/down1/aaa/a.jpg 에러
# 폴더 생성 : os.makedirs():모든폴더 생성- c:/down1/aaa/a.jpg

import os
# 폴더가 없으면 생성 후 진행
if not os.path.exists("c:down1"):
    os.makedirs("c:/down1")
ff=open("C:/down1/b.jpg","wb") #파일 쓰기
len=ff.write(fdata)
print(f"파일크기 : {len}바이트")
ff.close()
print("파일저장완료")