"""
3-1
"""
names = ['wwp','wwp1','wwp2']

print(names[0])
print(names[1])
print(names[2])

"""
3-2
"""
names = ['wwp','wwp1','wwp2']
message = 'Hello'

print(names[0] + message)
print(names[1] + message)
print(names[2] + message)

"""
3-3
"""
ways = ['bike', 'car', 'bus']
message = 'I would like to own a Honda '

print(message +ways[0])
print(message +ways[1])
print(message +ways[2])

"""
3-4
"""
friends = ['Mary', 'Bom', 'Jack']
message = ", I want to invite u to dinner"

print(friends.pop() + message)
print(friends.pop() + message)
print(friends.pop() + message)

"""
3-5
"""
friends = ['Mary', 'Bom', 'Jack']
message = ", I want to invite u to dinner"

print(friends[0] + message)
print(friends[1] + message)
print(friends[2] + message)
print(friends[0] + ' donnot have time')

friends[0] = 'wwp'
print(friends[0] + message)
print(friends[1] + message)
print(friends[2] + message)

"""
3-6
"""
friends = ['Mary', 'Bom', 'Jack']
message = ", I want to invite u to dinner"

print(friends[0] + message)
print(friends[1] + message)
print(friends[2] + message)
print('I find a bigger desk and I can invite more friends!')

friends.insert(0, 'wwp1')
friends.insert(2, 'wwp2')
friends.append("wwp3")

for friend in friends:
    print(friend + message)

"""
3-6
"""
friends = ['Mary', 'Bom', 'Jack']
message = ", I want to invite u to dinner"

print(friends[0] + message)
print(friends[1] + message)
print(friends[2] + message)
print('I find a bigger desk and I can invite more friends!')

friends.insert(0, 'wwp1')
friends.insert(2, 'wwp2')
friends.append("wwp3")

for friend in friends:
    print(friend + message)

print("Sorry, now I have to invite two friends to dinner")
print(friends.pop() + "Sorry, I cannot invite u")
print(friends.pop() + "Sorry, I cannot invite u")
print(friends.pop() + "Sorry, I cannot invite u")
print(friends.pop() + "Sorry, I cannot invite u")

print(friends[0] + ", I still invite u")
print(friends[1] + ", I still invite u")

del friends[0]
del friends[0]

print(friends)

"""
3-8
"""
places = ['Beihai', 'Dongjidao', 'Athens', 'Shamen', 'Paris']

print(sorted(places))#字母顺序排列

print(sorted(places, reverse=True))

places.reverse()
print(places)

places.sort()
print(places)

places.sort(reverse=True)
print(places)

"""
3-9
"""
friends = ['Mary', 'Bom', 'Jack']
message = ", I want to invite u to dinner"

print(friends[0] + message)
print(friends[1] + message)
print(friends[2] + message)
print("I invite " + str(len(friends)) + " friends.")
