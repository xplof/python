# txt='abBBcDd hello apple'
# print(txt.upper()) #대문자 
# print(txt.lower()) #소문자
# print(txt.swapcase()) #대문자는 소문자로, 소문자는 대문자로
# print(txt.title()) #단어 첫글자 대문자

# a_list=[1,2,3,4,5]

# # 문자열 index번호 가짐
# print(txt[1])
# print(a_list[1])
# print(a_list[1:3]) #[1,2]
# print(txt[1:3])
# print(txt[2:])
# print(txt[:3])
# print(len(txt)) #길이
# print(txt[::-1]) #역순

# txt="파이썬 공부가 쉬워요~ 너무 쉬워요. 파이썬은 재밌어요."
# print(txt.count("파이썬")) #글자 개수
# print(txt.count("요"))
# print(txt.find("공부")) #있을때 index번호
# print(txt.find("자바")) #없을때 -1

# t="aaa.py"
# print(t.endswith("py")) #있으면 true 없으면 false

# 문자열
txt= "  안녕하  세요  "
print(txt)
print(txt.strip()) #앞뒤공백제거 -rstrip():오른쪽 -lstrip():왼쪽
print(txt.replace(" ","")) #문자를 다른 문자로 치환
print(txt.replace("안녕","hello"))
txt="파이썬 공부가 쉬워요~ 너무 쉬워요. 파이썬은 재밌어요."
print(txt.replace("파이썬","자바"))

txt3="----파이썬----"
print(txt3.strip("-")) #특정 글자 제거

# 데이터베이스는 리스트를 저장할 수 없음
txt="a,b,c,d,안녕,반가워"
txt_list=txt.split(",")
print(txt_list)

txt="1,홍길동,100,100,100,300,100,1"
txt_list=txt.split(",")
txt_list[1]='유관순'
print(txt_list)

txt=","
txt2=txt.join("안녕하세요") # 글자 사이에 ,
print(txt2)

# map(함수,데이터값)
score=['100','99','98']
#함수
def cal(x):
    return int(x)*100
s_list=list(map(cal,score))
print(s_list)
# sum=0
# for s in score:
#     sum=sum+int(s)
# print("합계 :",sum)    

# a="1234"
# if a.isdigit(): #숫자로 변환가능
# while True:
        
#     my_input=input("숫자를 입력하세요 : ")
#     if my_input.isdigit():
#         my_input=int(my_input)
#     else:
#         print("숫자가 아닙니다. 숫자를 입력해주세요.")    
        
print('213'.isdigit()) #숫자인지 확인
print('213'.isalpha()) #알파벳인지 확인
print('213'.isalnum()) #전부 숫자인지 확인
print('213'.islower()) #전부 소문자인지 확인
print('213'.isupper()) #전부 대문자인지 확인    
