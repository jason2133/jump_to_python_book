# 전형적인 for문
test_list = ['one', 'two', 'three']
for i in test_list:
    print(i)

# 다양한 for문의 사용
a = [(1,2), (3,4), (5,6)]
for (first, last) in a:
    print(first + last)

# for문의 응용
marks = [90, 25, 67, 45, 80]
number = 0
for mark in marks:
    number += 1
    if mark >= 60:
        print("%d번 학생은 합격입니다." % number)
    else :
        print("%d번 학생은 불합격입니다." % number)

# for문과 continue문
marks = [90, 25, 67, 45, 80]
number = 0
for mark in marks:
    number += 1
    if mark < 60: continue
    print("%d번 학생. 축하합니다. 최종 합격하셨습니다." % number)

# for과 range를 활용한 구구단
for i in range(2, 10):
    for j in range(1, 10):
        print(i*j, end=" ")
        # 여기서 입력인수 end는 해당 결과값을 출력할때
        # 다음 줄로 넘기지 않고 그줄에 계속해서 출력하기 위한 것이다.
    print('')

