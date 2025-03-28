# n=7
# if 10>=n>=0:       #파이썬만 가능
#     print(10)
    
# if 10>=n and n>=0:
#     print("10")

# 345 - 봄, 678- 여름, 91011-가을, 1212-겨울

n=int(input("몇 월인지 입력하세요 : "))

if n>=9 and n<=11:
    print("가을")
elif n>=6 and n<=8:
    print("여름")
elif n>=3 and n<=5:
    print("봄")
else:
     print("겨울")