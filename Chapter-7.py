"""
7-1
"""
message = input("What kind of car would you like?\n")

print("Let me see if I can find you a " + message)
"""
7-2
"""
num = input("How many seats would you like?\n")
num = int(num)
if num < 8:
    print("Welcome to")
else:
    print("Sorry, there are no seats in the restaurant")
"""
7-3
"""
num = input("please input a number:\n")
num = int(num)

if num % 10 == 0:
    print(str(num) + " 是10的倍数")
else:
    print(str(num) + " 不是10的倍数")
"""
7-4
"""
while True:
    message = input("请输入你的配料：\n")

    if message == 'quit':
        break
    else:
        print("我们会在比萨中添加 " + message + " 配料")
"""
7-5
"""
while True:
    age = input("请问你的年龄： \n")
    age = int(age)

    if age < 3:
        print("免费")
    elif 3 <= age < 12:
        print("票价10美元")
    else:
        print("票价15美元")
"""
7-6
"""
active = True

while active:
    age = input("请问你的年龄： \n")

    if age == 'quit':
        active = False
    elif int(age) < 3:
        print("免费")
    elif 3 <= int(age) < 12:
        print("票价10美元")
    else:
        print("票价15美元")
"""
7-7
"""
while True:
    print("OK")
"""
7-8
"""
sandwich_orders = ['egg', 'apple', 'huotui', 'banana']
finished_sandwiches = []

for sandwich_order in sandwich_orders:
    print("I made your " + sandwich_order + " sandwich.")

    finished_sandwiches.append(sandwich_order)

print(finished_sandwiches)
"""
7-9
"""
sandwich_orders = ['egg', 'pastrami', 'huotui', 'pastrami','pastrami']

print("五香牛肉卖完了，好可惜")

active = True

while active:
    specie = 'pastrami'
    while specie in sandwich_orders:
        sandwich_orders.remove('pastrami')
    active = False

finished_sandwiches = []

for sandwich_order in sandwich_orders:
    print("I made your " + sandwich_order + " sandwich.")

    finished_sandwiches.append(sandwich_order)

print(finished_sandwiches)
"""
7-10
"""
places = []
names = []

active = True

while active:
    print("This is a survey")
    name = input("What is ur name\n")
    place = input("If you could visit one place in the world, where would you go?\n")

    names.append(name)
    places.append(place)

    print(name + " love " + place)
    print(names)
    print(places)

