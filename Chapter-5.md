"""
5-1
"""
car = 'subaru'
print("Is car == 'subaru' ? I predict True.")
print(car == 'subaru')

print("\nIs car == 'audi' ? I predict False")
print(car == 'audi')

name = 'wwp'
print(name == 'wwp')
print(name.title() == 'wwp')
"""
5-2
"""
name_1 = 'wwp'
name_2 = 'Wwp'
print(name_1 == name_2)
print(name_1 == name_2.lower())

num_1 = 1
num_2 = 2
print(num_1 == num_2)
print(num_1 != num_2)
print(num_1 > num_2)
print(num_1 < num_2)
print(num_1 >= num_2)
print(num_1 <= num_2)

if num_1 > 2 and num_2 > 2:
    print("True")
else:
    print("False")

lists = ['1', '2', '3', '4']
list = '0'

if list in lists:
    print(list + " in the lists")
else:
    print(list + " not in the lists")
"""
5-3
"""
alien_color = 'red'

if alien_color == 'green':
    print("You got 5 scores")
else:
    print("You donnot have scores")
"""
5-4
"""
alien_color = 'red'

if alien_color == 'green':
    print("You got 5 scores")
else:
    print("You got 10 scores")
"""
5-5
"""
alien_color = 'red'

if alien_color == 'green':
    print("You got 5 scores")
elif alien_color == 'yellow':
    print("You got 10 scores")
else:
    print("You got 15 scores")

"""
5-6
"""
age = 25

if age < 2:
    print("baby")
elif 2 <= age < 4:
    print("kid")
elif 4 <= age < 13:
    print("child")
elif 13 <= age < 20:
    print("teer")
elif 20 <= age < 65:
    print('adult')
else:
    print("the elder")
"""
5-7
"""
favorite_fruits = ['apple', 'orange', 'banana']

if 'apple' in favorite_fruits:
    print("You really like apple")
if 'banana' in favorite_fruits:
    print("You really like banana")
if 'orange' in favorite_fruits:
    print("You really like orange")
if 'pear' in favorite_fruits:
    print("You really like pear")
else:
    print("not ")
"""
5-8
"""
user_names = ['admin', 'wwp','zcy', 'zmm', 'zss']
for user_name in user_names:

    if user_name == "admin":
        print("Hello admin, would you like to see a status report?")
    else:
        print("Hello " + user_name + ", thank u for logging in again")
"""
5-9
"""
user_names = ['admin', 'wwp','zcy', 'zmm', 'zss']
for user_name in user_names:
    if user_name == '':
        print("We need to find some users.")
    elif user_name == "admin":
        print("Hello admin, would you like to see a status report?")
    else:
        print("Hello " + user_name + ", thank u for logging in again")
"""
5-10
"""
current_users = ['admin', 'wwp','zcy', 'zmm', 'zss']
new_users = ['admin', 'wwp1','zcy1', 'zmm1', 'zss']

for new_user in new_users:
    if new_user in current_users:
        print(new_user + "已被使用，请重新输入")
    else:
        print("Welcome to" + new_user)
"""
5-11
"""
nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

for num in nums:
    if num == '1':
        print('1st')
    elif num == '2':
        print('2nd')
    elif num == '3':
        print('3rd')
    else:
        print(num + 'th')
