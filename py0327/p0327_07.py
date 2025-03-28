# 날짜, 시간

import datetime
now=datetime.datetime.now()
print("현재시간 : ",now)
print(now.hour)
print(now.year)
print(now.day)
print(now.minute)

# 시간이 12 이상이면 오후, 12 미만이면 오전이라고 출력하라
# 13시 - 오후1시
# 9시 - 오전9시
# 15시 - 오후3시라고 출력

# n=int(input("시간을 입력하세요 : "))

h=now.hour
m="{:02d}".format(now.minute)
if h>12:
    print("오후 {:02d}:{}".format(h-12,m))
else:
    print("오전 {}:{}".format(h,m))
    
    # 날짜출력
print("{}-{:02d}-{:02d}".format(now.year,now.month,now.day))
 