# 정수형
a = 123
print(a)

# 실수형
b = 1.2
print(b)

c = 4.24e-10
print(c)

# 복소수
d = 1 + 2j # 일반적인 복소수는 i로 표현하지만 파이썬에서는 i를 j로 표현한다!
print(d.real) # 복소수의 실수 부분
print(d.imag) # 복소수의 허수 부분
print(d.conjugate) # 복소수의 켤레복소수 부분
print(abs(d)) # 복소수의 절댓값

#사칙연산
e = 7
f = 4
print(e + f) # 덧셈
print(e - f) # 뺄셈
print(e * f) # 곱셈
print(e / f) # 나눗셈
print(e ** f) # e의 f제곱
print(e % f) # e를 f로 나누고 나머지
print(e // f) # 나눗셈 연산하고 결과값을 내림하는데 정수부분을 남겨두고 소수부분을 없앰


