"""
6-1
"""
friend_info = {'first_name' : 'wenping', 'last_name' : 'wang', 'age' : '25', 'city' : 'chongqong'}

first_name = friend_info['first_name']
last_name = friend_info['last_name']
age = friend_info['age']
city = friend_info['city']

print(first_name + last_name + age + city)
"""
6-2
"""
num = {'wwp' : '13', 'zcy' : '8', 'zmm' : '1', 'zss' : '2', 'ww' : '5'}

print('wwp favorite number is ' + num['wwp'])
print('zcy favorite number is ' + num['zcy'])
print('zmm favorite number is ' + num['zmm'])
print('zss favorite number is ' + num['zss'])
print('ww favorite number is ' + num['ww'])
"""
6-3
"""
vocabulary = {'C++' : 'first', "C#" : 'second', 'python' : 'OK', 'java' : 'dif'}

print('C++ : ' + vocabulary['C++'])
print('C# : ' + vocabulary['C#'])
print('python : ' + vocabulary['python'])
print('java : ' + vocabulary['java'])

"""
6-4
"""
vocabulary = {'C++' : 'first', "C#" : 'second', 'python' : 'OK', 'java' : 'dif'}

for language, info in vocabulary.items():
    print(language + ":\n" + info)

"""
6-5
"""
rivers = {'nile' : 'egypt', 'Yangtze' : 'china', 'amazon' : 'Brazil'}

for river, country in rivers.items():
    print("The" + river.title() + ' runs through ' + country.title())
"""
6-6
"""
favorite_languages = {'jen': 'python', 'sarah': 'c', 'edward': 'ruby', 'phil': 'python'}

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + language.title() + ".")

survey_list = ['jen', 'link', 'sarah', 'lisa']
for investigated in survey_list:
    if investigated in favorite_languages:
        print(investigated + ", Thank you for your cooperation.")
    else:
        print(investigated + ", Could you do me a favor?")
"""
6-7
"""
jams = {'first_name': 'leboron', 'last_name': 'jams', 'age': 34, 'city': 'akron'}
wade = {'first_name': 'dwayne', 'last_name': 'wade', 'age': 34, 'city': 'miami'}
bosh = {'first_name': 'cris', 'last_name': 'bosh', 'age': 32, 'city': 'washington'}
peoples = [jams, wade, bosh]

for people in peoples:
    print(people)
"""
6-8
"""
zmm_cat = {'name' : 'zmm_cat', 'owner' : 'zmm'}
zss_cat = {'name' : 'zss_cat', 'owner' : 'zss'}
zcy_dog = {'name' : 'zcy_cat', 'owner' : 'zcy'}
pets = [zmm_cat, zss_cat, zcy_dog]

for pet in pets:
    print("The owner of the " + pet['name'] + " is " + pet['owner'])
"""
6-9
"""
favorite_places = {'jams': {'NewYork', 'Miami', 'Aklon'},
                   'wade': {'Miami', 'Aklun'},
                   'bosh': {'toronto', 'Miami'}
                   }

for name, places in favorite_places.items():
    print(name.title() + " favorite places:")
    for place in places:
        print(place)
"""
6-10
"""
nums = {'wwp' : {'13','3'},
       'zcy' : {'8', '18'},
       'zmm' : {'1','11'},
       'zss' : {'2','12'},
       'ww' : {'5','15'}
       }
for name, num in nums.items():
    print(name.title() + " favorite number is: ")
    for num_ in num:
        print(num_)
"""
6-11
"""
cities = {'chongqing' :{'country' : 'china', 'population' : '111111111111', 'fact' : 'hotpot'},
          'chengdu' : {'country' : 'china', 'population' : '111111111111', 'fact' : 'panda'},
          'zaozhuang' : {'country' : 'china', 'population' : '111111111111', 'fact' : 'mozi'}
          }
for city_name, info in cities.items():
    print(city_name + info['country'])
    print(city_name + info['population'])
    print(city_name + info['fact'])
