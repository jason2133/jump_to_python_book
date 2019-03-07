s1 = set([1, 2, 3])
print(s1)

s2 = set("koreauniv")
print(s2)

s3 = set([1, 2, 3, 4, 5, 6])
s4 = set([4, 5, 6, 7, 8, 9])

print(s3 & s4) # 교집합
print(s3.intersection(s4))

print(s3.union(s4)) # 합집합

print(s3 - s4) # 차집합 1
print(s4 - s3) # 차집합 2
print(s3.difference(s4)) # 차집합 1
print(s4.difference(s3)) # 차집합 2

s3.update([7, 8, 9]) # 값 여러개 추가하기
print(s3)
s3.remove(9) # 특정 값 제거하기
print(s3)


