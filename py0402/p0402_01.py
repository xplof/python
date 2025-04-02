# dic={"no":1, 'name':'홍길동','kor':100,'eng':90,'math':80,'total':270}
# dic={"no":1, 'name':'홍길동','kor':100,'eng':90,'math':80,'total':270}
# dic['kor']=100 #딕셔너리 추가
# # del dic['no'] #딕셔너리 삭제
# dic['name']='유관순' #딕셔너리
# print(dic)

# print(dic['name']) #딕셔너리 개별출력
# print(dic.get('123')) #get()함수 사용시 없는 키는 none출력
# print(dic.keys()) #key 출력
# print(dic.values()) #value 출력
# print(dic.items()) #key, value를 튜플형태로 출력

# if 'no' in dic: #딕셔너리를 비교할떄 key를 가지고 비교하게됨
#     print("있습니다")
    
#     # 딕셔너리 정렬
# import operator
# dic_sort=sorted(dic.items(),key=operator.itemgetter(0))   
# print(dic_sort) 

# # 딕셔너리 전체출력
# for k in dic:
#     print(dic[k])
# for k,v in dic.items():
#     print(k,v)

# # 리스트 정렬
# for i in list: #리스트 전체출력
#     print(i)
# # list.sort() #오름차순
# # list.reverse() #내림차순
# # print(list)


# # 리스트 내포
# # 1~10리스트생성
# a_list=[i+1 for i in range(10)]
# print(a_list)

# b_list=[0]*10
# print(b_list)

# c_list=[i for i in range(1,51) if i%2==1]
# print(c_list)


i_list=[1,2,3,4,5,1,2,10]
txt_list=['안녕','반가워','다음','내일','봐','잘','지내','봐요']
# zip
for i,t in zip(i_list,txt_list):
    print(i,t)
    
 # zip 사용해서 list 생성
new_list=list(zip(i_list,txt_list))
print(new_list)    

# zip 사용해서 dict 생성
new_dic= dict(zip(i_list,txt_list)) #중복은 덮어씌워짐
print(new_dic) 

# 얕은복사, 깊은복사
new_list=i_list #얕
new_list2=[*i_list] #깊







# list[1]=11 #리스트 수정
# list.append(100) #리스트 추가
# del list[0] #리스트 삭제
# print(list)
