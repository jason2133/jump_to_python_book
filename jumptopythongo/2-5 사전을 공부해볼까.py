# 딕셔너리 쌍 추가하기
a = {1: 'a'}
a[2] = 'b'
a['name'] = 'pey'
a[3] = [1, 2, 3]
del a[2] # 딕셔너리 요소 삭제하기
print(a)

dic = {'name' : 'Jason Lee', 'Birthday' : '19981121', 'talk' : '감빡이'}
print(dic['name'])
print(dic['Birthday'])
print(dic['talk'])
print(dic.keys()) # 딕셔너리의 key 리스트 만들기

for k in dic.keys():
    print(k)

print(list(dic.keys()))
print(dic.values()) # value 리스트 만들기
print(dic.items()) # key, value 쌍 얻기 items

