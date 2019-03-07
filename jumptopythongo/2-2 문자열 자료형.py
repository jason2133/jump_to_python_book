print("jason") # 문자열
print('jason')
print("""jason""")
print('''jason''')
# 위 4개는 모두 같은 결과를 도출하는 문자열임

# 문자열 안에 작은따옴표나 큰따옴표를 포함시키고 싶을때
print("Jason is a student of Korea University..")
print('Jason has loudly shouted "뱃노래"')

# 문자열 연산하기
# 첫번째로 문자열 더해서 연결하기 (concatenation)
head = "Jason is a student at"
tail = " Department of Statistics, Korea University, Seoul."
print(head + tail)

# 문자열 곱하기
a = "gazua"
print(a * 2)
print(a * 5)

# 문자열 인덱싱 - 파이썬은 0부터 숫자를 센다
b = "즐거운 고연전 날에 연대생 우는 소리 지고 가는 연대생이 처량도 하구나"
print(b[5])
print(b[15])
print(b[-27])
print((b[-25] + "하") * 5)

# 문자열 슬라이싱
c = ["즐거운", "고연전", "날에", "연대생", "우는", "소리"]
i = 0
while i < len(c):
    print(c[i])
    i += 1

print(c[0:]) # 문자열 0부터 끝까지 뽑아낸다
print(c[:6]) # 문자열 0부터 5번까지 뽑아낸다
print(c[:]) # 문자열 처음부터 끝까지 뽑아낸다

# 슬라이싱으로 문자열 나누기
d = "고려대통계학과이재승"
univ = d[:3] + " "
department = d[3:7] + " "
name = d[7:]
print(univ + department + name)

print(d[:3] + " 통계학과 " + d[7:])

# 문자열 포매팅 따라하기
print("%s은 %d년에 태어났다" % ("이재승", 1998)) # 숫자, 문자 바로 대입

# 꿀팁 - 포매팅 연산자 %d와 %를 같이 쓸때는 %%를 씁니다
print("나의 Image Classification 정확도 최고 확률은 %d%%" % 99)

# 포맷코드와 숫자 함께 사용하기
print("%10s" % "제이슨")
print("%-10s" % "제이슨" + "갓갓")

# 소수점 표현하기
print("%0.4f" % 3.141592)
print("%10.4f" % 3.141592)

# 문자열 관련 함수들
# 문자 개수 세기 count
e = "염재호 총장의 모토는 '개척하는 지성, 개혁하는 고대'이다. 그는 끊임없이 우리보고 개척하라고 한다."
print(e.count("개"))
print(e.find("개"))
print(e.find("가")) # -1이 나오는 경우는 찾는 문자열이 존재하지 않는 것
print(e.index("총"))

# 문자열 삽입
f = "~~~~~"
print(f.join("기모띠"))
g = "응애응애응애응"
print(g.split("애")) # 문자열 나누기 (split)

# 문자열 바꾸기 (replace)
h = "I'm so sorry but i love you 다 거짓말"
print(h.replace("sorry", "ggooood"))

