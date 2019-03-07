# 10번 찍어 안 넘어가는 나무 없다
treehit = 0
while treehit < 10:
    treehit += 1 #treehit = treehit + 1
    print("나무 %d번 찍었습니다." % (treehit))
    if treehit == 10:
        print("나무 넘어갑니다")

# 조건에 맞지 않는 경우 맨 처음으로 돌아가기
a = 0
while a < 10:
    a = a + 1
    if a % 2 == 0: continue
    print(a)

"""
무한루프
while True:
    "ctrl + c를 눌러야 무한루프를 빠져나갈 수 있습니다."
    
"""



