# 여러가지 조건
# 음수, 0, 양수

# n=int(input("숫자를 입력하세요 : "))
# if n>0:
#     print("양수입니다")

# elif n==0:
#     print("0입니다")

# else:
#     print("음수입니다")

# 60점이상 합격, 60점미만 불합격출격
# n=int(input("점수를 입력하세요 : "))
# if n>=60:
#     print("합격")
# else:
#     print("불합격")
    
# 70점이상 합격, 60~69재시험, 60점미만 불합격
# n=int(input("점수를 입력하세요 : "))
# if n>=70:
#     print("합")
# elif n>=60:
#     print("재시험")
# else:   print("불합")

# 시험 : 90이상a 80이상b 70이상c 60이상d 50이상f
# 100-97 a+, 96-93 a, 92-90a, 89-87 b+, 

# print("gd",end="") #end=""사용시 줄바꿈x
# print("gd")

n=int(input("점수를 입력하세요 : "))

if n>=90:
    print("a",end="")
    if n>=97: print("+")
    elif n>93: pass
    else: print("-")
    
elif n>=80:
      print("b",end="")
      if n>=87:print("+")
      elif n>83: pass
      else: print("-")
elif n>=70:
    print("c", end="")
    if n>=77: print("+")
    elif n>=73: pass
    else: print("-")
    
elif n>=60:
    print("d")
else:
    print("f")
