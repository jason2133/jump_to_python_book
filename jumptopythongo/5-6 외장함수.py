import sys
print(sys.path)

import os
print(os.environ)

print(os.getcwd())

import time
print(time.time())

print(time.localtime(time.time()))
print(time.asctime(time.localtime(time.time())))
print(time.ctime())

import time
for i in range(10):
    print(i)
    time.sleep(0.0001)

import calendar
print(calendar.calendar(2018))

print(calendar.weekday(2018, 11, 21))

print(calendar.monthrange(2018, 8))

import random
print(random.random())
print(random.randint(1, 10))

import random
def random_pop1(data):
    number = random.randint(0, len(data)-1)
    return data.pop(number)

if __name__ == "__main__":
    data = [1, 2, 3, 4, 5]
    while data: print(random_pop1(data))

import random
def random_pop2(data):
    number = random.choice(data)
    data.remove(number)
    return number

if __name__ == "__main__":
    data = [1, 2, 3, 4, 5, 7, 85]
    while data: print(random_pop2(data))

import random
data3 = [1, 25, 58, 97, 62, 52, 468]
random.shuffle(data3)
print(data3)

import webbrowser
webbrowser.open("http://korea.ac.kr")




