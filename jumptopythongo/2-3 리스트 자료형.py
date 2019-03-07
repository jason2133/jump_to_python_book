#리스트의 인덱싱과 슬라이싱
a = [1, 2, 3]
print(a)
print(a[0])
print(a[0] + a[1])
print(a[-1])

b = [1, 2, 3, ['a','b', 'c']]
print(b[-1][0], b[-1][1], b[-1][2]) # 이중 인덱스에서 슬라이싱 하기

# 중첩된 리스트에서 슬라이싱 하기
a = [1, 2, 3, ['a', 'b', 'c'], 4, 5]
print(a[2:5])
print(a[3][:2])

# 리스트 더하기랑 곱하기
a = ["제이슨", "안암", "골"]
b = ["민족고대", "호안정대", "통계6반"]
print(a + b) # 리스트 더하기
print(a * 3) # 리스트 곱하기

# 리스트의 수정, 변경과 삭제
c = [1, 2, 4]
c[1:2] = ['a', 'b', 'c']
print(c)

d = [1, 2, 4]
d[1] = ['a', 'b', 'c']
print(d)
# c와 d는 리스트 수정할 때 주의할 점을 적어놓은 것이다. 차이 알겠지?

# 리스트 관련 함수들
e = [1, 4, 3, 2]
e.sort() # 리스트의 요소를 순서대로 정렬한다
print(e)

f = [1, 4, 3, 2]
f.sort() # 리스트의 요소를 순서대로 정렬한 다음
f.reverse() # 역순으로 정렬한다 reverse
print(f)

"""
튜플 자료형 - 튜플과 리스트의 차이점으로는,
인덱스는 []를 사용한다는 점이고,
튜플은 ()를 사용한다는 점이다.
그리고 인덱스는 수정(추가, 삭제 포함)이 가능한 반면,
튜플은 수정이 불가능하다.
평균적으로는 인덱스를 튜플보다 많이 사용한다.
"""

t1 = (1, 2, 'a', 'b')
print(t1[0])
print(t1[3])
print(t1[1:])
t2 = (3, 4)
print(t1 + t2)
print(t2 * 3)

