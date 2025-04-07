print(1)
print(2)
raise NotImplementedError("프로그램 미구현-수정부분이 프로그램진행해야함")
print(3)

# a_list=[1,2,3,4,5]
# print(a_list)
# try:
#     print(a_list[5])
# except ValueError: #valueeroor만 처리함
#     print("출력되어야 함")
# # except IndexError:
# #     print("인덱스에러임")
# except Exception as e:
#     print(e)
#     print("모든 예외처리가 다 가능함")
# print(7)
# print(8)


# finally-무조건실행
# try:
#     f=open("info.txt","w")
#     raise NotImplementedError
# except Exception  as e:
#     print(e)
# finally:
#     f.close()
    
