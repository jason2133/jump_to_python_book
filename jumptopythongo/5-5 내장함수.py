print(abs(-3))    # 절댓값

print(all([1, 2, 3])) # all 반복가능한 자료형 x를 입력인수로 받음
print(all([1, 2, 3, 0])) # 안에 있는게 모두 참이면 True, 거짓이 하나라도 있으면 False

print(any([1, 2, 3, 0])) # all의 반대는 any
print(any([0, ""])) # 즉 안에 있는게 하나라도 참이 있으면 True, 모두 거짓이면 False

print(chr(97)) # 아스키 코드값을 입력으로 받아 그 코드에 해당하는 문자를 출력하는 함수
print(chr(95))
print(chr(88))

print(dir([1, 2, 3])) # dir은 객체가 자체적으로 가지고 있는 변수나 함수를 보여줌
print(dir([4, 5, 6]))
print(dir({'1':'a'}))

print(divmod(5, 2))
print(divmod(8.5, 1.6)) # divmod(a, b)는 a를 b로 나눈 몫과 나머지를 튜플 형태로 리턴하는 함수임

for i, name in enumerate(['body', 'too', 'far']):
    print(i, name)        # enumerate를 for문과 함께 사용하면 자료형의 현재 순서와 그 값을 쉽게 알 수 있다
    # for문처럼 반복되는 구간에서 객체가 현재 어느 위치에 있는지 알려주는 인덱스 값이 필요할 때 enumerate 함수를
    # 사용하면 매우 유용함

print(eval('1+2'))
print(eval("'ja'+'son'")) # 실행 가능한 문자열을 입력으로 받아 문자열을 실행한 결과값을 리턴하는 함수
print(eval('divmod(5, 2)')) # 입력받은 문자열로 파이썬 함수나 클래스를 동적으로 실행하고 싶은 경우에 사용함

def positive1(numberList):
    result = []
    for num in numberList:
        if num > 0:
            result.append(num)
    return result

print(positive1([1, -3, 2, 0, -5, 6]))

def positive2(x):
    return x > 0

print(list(filter(positive2, [1, -3, 2, 0, -5, 6])))

print(list(filter(lambda x: x > 0, [1, -3, 2, 0, -5, 6])))

print(hex(234)) # 16진수로 변환하여 리턴
print(hex(3)) # 16진수로 변환하여 리턴

a = 3
print(id(3))  # id는 객체를 입력 받아 객체의 고유 주소값(레퍼런스)을 리턴하는 함수
print(id(a))
b = a
print(id(b))
print(id(17))

print(int('11', 2))
print(int('1A', 16))

class Person: pass
a = Person()
print(isinstance(a, Person))

b = 3
print(isinstance(b, Person))

sum = lambda a, b: a + b
print(sum(3, 4))

def sum(a, b):
    return a + b

print(sum(3, 4))

myList = [lambda a, b : a + b, lambda a, b : a * b]
print(myList[0](3, 5))
print(myList[1](8, 5))

print(len("python"))

print(list("python"))
print(list((1, 2, 3)))











