# Q1 함수. 피보나치수열 만들기
# 피보나치 수열 1번
previous = 0
current = 1
i = 0

while i < 20:
    print(current)
    temp = previous
    previous = current
    current = previous + temp
    i += 1

# 피보나치 수열 2번
def fib(n):
    if n == 0 : return 0
    if n == 1 : return 1
    return fib(n-2) + fib(n-1)

for i in range(10):
    print(fib(i))



