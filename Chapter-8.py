"""
8-1
"""
def display_message():

    print("I learned function")

display_message()
"""
8-2
"""
def favorite_book(title):

    print("One of my favorite books is " + title)

favorite_book('Alice in Wonderland')
"""
8-3
"""
def make_shirt(size, word):

    print("Your Tshirt's size " + size + ", and word is " + word)

make_shirt('S', 'wwp')
"""
8-4
"""
def make_shirt(size, word = 'I love Python'):

    print("Your Tshirt's size " + size + ", and word is " + word)


make_shirt('XXXL')
make_shirt('M')
make_shirt(size='S', word='wwp')
"""
8-5
"""
def describe_city(city_name, country = 'Iceland'):

    print(city_name + " is in " + country)

describe_city('Reykjavik')
describe_city('XXX')
describe_city(city_name='Hangzhou', country='China')
"""
8-6
"""
def city_country(city_name, country):

    res = '" ' + city_name.title() + ", " + country.title() + ' "'
    return res

print(city_country('Santiage', 'chile'))
"""
8-7
"""
def make_album(singer, album_name,num = '5'):
    music = {'singer: ': singer, 'album_name: ': album_name, 'num:' : num}
    return music

first = make_album('wwp', 'days', '7')
second = make_album('zmm', '6666')
thirst = make_album('zss', 'meimie')

albums = [first, second, thirst]

for album_names in albums:
    for singer_name, name in album_names.items():
        print(singer_name + name)
"""
8-8
"""
def make_album(singer, album_name,num = '5'):
    music = {'singer: ': singer, 'album_name: ': album_name, 'num:' : num}
    return music

while True:

    singer_name = input("请输入歌手的名字：\n")
    if singer_name == '#':
        break
    album_name = input("请输入专辑的名字：\n")
    if album_name == '#':
        break
    album = make_album(singer_name, album_name)
    print(album)
    for singer, album_name in album.items():
        print(singer, album_name)
"""
8-9
"""
names = []

def show_magicians():

    for name in names:
        print(name)

while True:
    name = input("请输入魔术师的名字：\n")
    if name == '#':
        break

    names.append(name)
    show_magicians()
"""
8-10
"""
names = []

def show_magicians():

    for name in names:
        print(name)

def make_great():
    word = "The great"
    name = names.pop() + word
    names.append(name)

while True:
    new_name = input("请输入魔术师的名字：\n")
    if new_name == '#':
        break

    names.append(new_name)
    make_great()
    show_magicians()
"""
8-11
"""
names = []
new_names = []

def show_magicians():

    for name in names:
        print(name)

def make_great():
    word = " The great"
    name = names.pop() + word
    new_names.append(name)
    print(new_names)

while True:
    new_name = input("请输入魔术师的名字：\n")
    if new_name == '#':
        break

    names.append(new_name)

    show_magicians()
    make_great()
"""
8-12
"""
def chose_materials(*materials):
    print("收集食材：")

    for material in materials:
        print(material)


while True:
    food = input("请输入您想要的食材：\n")

    if food == '#':
        break
    else:
        chose_materials(food )
"""
8-13
"""
profile = {}

def build_profile(first, last, **user_info):

    profile['first_name'] = first
    profile['last_name'] = last

    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('albert', 'einstein',
                             location='princeton',
                             field='physics')
print(user_profile)

me = build_profile('wwp', 'wang',
                       location='chongqing',
                       filed='cs')
print(me)
"""
8-14
"""
def make_car(car_name, made_mercuil, color='white', tow_package=False):

    if tow_package:
        print(car_name + " is " + made_mercuil + " and color is" + color)
        print("Have installed the " + str(tow_package))
    else:
        print(car_name + " is " + made_mercuil + " and color is" + color)
    return car_name

car = make_car('subaru', 'outback', color='blue', tow_package=True)
"""
8-15
"""
from printing_functions import print_models

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

res = print_models(unprinted_designs, completed_models)




