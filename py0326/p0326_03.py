print("글자를 출력") #print-출력 #""문자열 #숫자는 쌍따옴표x
print('글자를 출력')
print('"이순신 장군이 말씀하셨습니다."')
print("\"이순신장군이 말했다.\"") #특수기호 앞에 \는 그 뒤 기호를 문자로 인식시켜줌
print("%s : %d " % ("출력값",100)) #주석 단축키 - ctrl /
print("출력값 :",100)
#s는 문자 d는 정수 f는 실수 c는 한글자
print("100/200=0.5")
print(100/200)
print("100/200=", 100/200)
print(10/3)
print("10/3 =", 10/3)
print("%d / %d = %.1f" % (100,200,100/200))
# 100, 200, 계산을 소수점 1자리까지만 출력하시오.
print("%d / %d = %0.1f" % (10,7,10/7))