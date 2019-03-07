"""
이것은 간단한 사칙연산 및 기본적인 파이썬을 공부하려고 하는 것이다.
"""

print(int(2) + int(5))
print(str(2)+ str(5))
print(float(2) + float(5))

print(1 + 2)
print(3 / 2.4)
print(3 * 9)

a = 1
b = 2
print(a + b)

a = "Jaeseung"   
print(a)

a = 3
if a > 1:
    print("a is greater than 1")

for a in [1, 2, 3]:
    print(a)

i = 0
while i < 3:
    i += 1
    print (i)

def sum (a, b):
    return a + b

print(sum (3, 4))
