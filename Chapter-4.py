"""
4-1
"""
pizzas = ['beef', 'chicken', 'fruit']

for pizza in pizzas:
    print(pizza)

for pizza in pizzas:
    print("I like " + pizza + "pizza")

print("I really love pizza")

"""
4-2
"""
animals = ['dog', 'cat', 'pig']

for animal in animals:
    print(animal)

for animal in animals:
    print("A " + animal + " would make a great pet")

print("Any of these animals would make a great pet")

"""
4-3
"""
nums = list(range(1, 21))

for num in nums:
    print(num)

"""
4-4
"""
nums = list(range(1, 1000001))

for num in nums:
    print(num)

"""
4-5
"""
nums = list(range(1, 1000001))

print(min(nums))
print(max(nums))
print(sum(nums))

"""
4-6
"""
nums = list(range(1, 21, 2))
for num in nums:
    print(num)

"""
4-7
"""
nums = list(range(3, 30, 3))
for num in nums:
    print(num)

"""
4-8
"""
res = []
nums = range(1, 11)

for num in nums:
    val = num ** 3
    res.append(val)

print(res)

"""
4-9
"""
res = []
nums = range(1, 11)

for num in nums:
    val = num ** 3
    res.append(val)

print(res)

"""
4-10
"""
pizzas = ['beef', 'chicken', 'fruit','other','pig']

for pizza in pizzas:
    print(pizza)

print("The first thress items in the list are: ")
print(pizzas[:3])

print("Thress items from the middle of the list are: ")
print(pizzas[2:5])

print("The last thress items in the list are: ")
print(pizzas[-3:])

"""
4-11
"""
pizzas = ['beef', 'chicken', 'fruit','other','pig']
friends_pizzas = pizzas[:]#创建副本

pizzas.append("apple")
friends_pizzas.append("banana")

print("My favorite pizzas are: ")
for pizza in pizzas:
    print(pizza)

print("My friends favorite pizzas are: ")
for friends_pizza in friends_pizzas:
    print(friends_pizza)
"""
4-13
"""
foods = ('pizza', 'cake', 'egg', 'beef')

for food in foods:
    print(food)

foods[0] = 'milk'
