def getTotalPage(m, n):
    if m % n == 0:
        return(m // n)
        # 절댓값 함수로 abs라는게 있긴한데 그걸 쓸 필요는 없고 // 를 쓰면 나눴을때 정수만 살린다는거 기억하기!~!
    else:
        return(m // n + 1)

print(getTotalPage(5, 10))
print(getTotalPage(15, 10))
print(getTotalPage(25, 10))
print(getTotalPage(30, 10))



