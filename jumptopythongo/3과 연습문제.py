# if문 다음 코드의 결과값은 무엇일까?
a = "Life is too short, you need python"

if "wife" in a: print("wife")
elif "python" in a and "you" not in a: print("python")
elif "shirt" not in a: print("shirt")
elif "need" in a: print("need")
else: print("none")

# while 문
i = 0
while True:
    i += 1
    if i >= 6: break
    print("*" * i)

# for문
A = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
total = 0
for score in A:
    total += score
average = total / 10
print(average)


