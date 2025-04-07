print(1)
print(2)
raise NotImplementedError #프로그램 구현이 아직 진행이 안됨
print(3)




# try:          #프로그램 구현부분
#     print(1)
#     print(2)
#     raise NotImplementedError #예외를 강제로 발생시킴
#     raise ZeroDivisionError
#     choice=int(input("숫자입력 : "))
#     print(3)
#     print(4)
# except Exception as e: #에러가 났을때 실행
#     print(5)
#     print(e)
# else: #에러가 나지 않았을떄 실행
#     print(6)
# finally: #무조건 실행
#     print(7)



# try:
#     num=int(input("원의 반지름을 입력하세요"))
#     print("원의 넓이 :",3.14*num**2)
# except Exception as e:
#     print(e)
# else: #try구문에 에러가 없을시 실행
#     pass



# a_list=["52","273","32","파이썬","103"]
# list_number=[]
# 숫자로 변환가는것만 리스트넘버에 저장

# a_lis변환
# for i in a_list:
#     if i.isdigit():
#         list_number.append(int(i))
#     else: print("숫자가 아님 :",i)
    
# print(list_number)

# for i in a_list:
#     try:
#         list_number.append(int(i))
#     except Exception as e: 
#         print(e)
#         print("데이터출력 : :",i)
    
# print(list_number)        