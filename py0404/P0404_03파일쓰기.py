# # 파일쓰기  - w
# f=open("aa.txt","w",encoding="utf-8")

# f.write("안녕하세요.\r\n") #\r-문장 끝으로 이동 #\n-줄바꿈
# f.write("반가워요\n")
# f.close


# f=open("aaa.txt","w",encoding="utf-8")
# for i in range(10):
#     f.write(f"{i+1}.안녕하세요\n")
    
# f=open("memo.txt","w",encoding="utf-8")
# print(["메모장"])
# print("------------")
# print("저장하려는 글자를 입력하세요.(x.종료) :")
# while True:
#     line=input("")
#     if line.lower()=="x": break    
#     f.write(line+"\n")
# f.close

# 파일 이어쓰기 - a (있는 글에서 이어쓰기)

# f=open("py0404/memo2.txt","w",encoding="utf-8")
# f.write("1.홍길동,100,100,99")
# f.write("2.유관순,50,50,50")
# f.close()