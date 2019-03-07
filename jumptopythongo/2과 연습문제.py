# 문자열 Q1
pin = "881120-1068234"
yyyymmdd = pin[0:6]
num = pin[7:]
print(yyyymmdd)
print(num)

# 문자열 Q2
print(pin[7])

# 리스트 Q1
a = [1, 3, 5, 4, 2]
a.sort()
a.reverse()
print(a)

# 리스트 Q2
a = ['Life', 'is', 'too', 'short']
result = " ".join(a)
print(result)


# 튜플
a = (1, 2, 3)
a = a + (4,)
print(a)

# 딕셔너리
a = {'A' : 90, 'B' : 80, 'C' : 70}
result = a.pop('B')  # B만 탁 튀어놓는다
print(a)
print(result)

# 집합
a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
aSet = set(a)
b = list(aSet)
print(b)














