# 구구단
for i in range(1, 10):
    for j in range(1, 10):
        print("%d X %d = %d" % (i, j, i*j))

# 2단 구구단 만들기
for i in range(1, 10):
    print("2 X %d = %d" % (i, 2*i))

# 1부터 9까지 출력하기
a = 1
while a < 10:
    print(a)
    a += 1

# 구구단 함수 만들기
def GuGu(n):
    result = []
    b = 1
    while b < 10:
        result.append(n * b)
        b += 1
    return result

print(GuGu(3))



