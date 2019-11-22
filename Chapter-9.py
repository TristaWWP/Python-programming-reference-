"""
9-1
"""
class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(self.restaurant_name + " is a " + self.cuisine_type + "cuisine_type")

    def open_restaurant(self):
        print(self.restaurant_name + " is busy")

restaurant = Restaurant('wwp', 'zcy')
restaurant.describe_restaurant()
restaurant.open_restaurant()
"""
9-2
"""
class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(self.restaurant_name + " is a " + self.cuisine_type + "cuisine_type")

    def open_restaurant(self):
        print(self.restaurant_name + " is busy")

restaurant1 = Restaurant('wwp', 'zcy')
restaurant1.describe_restaurant()
restaurant1.open_restaurant()
restaurant2 = Restaurant('wwp', 'zcy')
restaurant2.describe_restaurant()
restaurant2.open_restaurant()
restaurant3 = Restaurant('wwp', 'zcy')
restaurant3.describe_restaurant()
restaurant3.open_restaurant()
"""
9-3
"""
class User:

    def __init__(self, first_name, last_name, age, sex, num):
        self.name = first_name + last_name
        self.age = str(age)
        self.sex = sex
        self.num = num

    def describe_user(self):

        if self.sex == '男':
            print(self.name + " is " + self.age + " and his number is " + self.num)
        else:
            print(self.name + " is " + self.age + " and her number is " + self.num)

    def greet_user(self):
        print(self.name + " Welcome")

user = User('wen', 'wang', 25, '女', '123456789')
user.describe_user()
user.greet_user()
"""
9-4
"""
class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(self.restaurant_name + " is a " + self.cuisine_type + "cuisine_type")

    def open_restaurant(self):
        print(self.restaurant_name + " is busy")

    def set_number_served(self):
        self.number_served = 1
        print("就餐人数" + str(self.number_served))

    def incerment_number_served(self):
        self.number_served = self.number_served + 1
        print(str(self.number_served))

restaurant = Restaurant('wwp', 'zcy')
restaurant.set_number_served()
restaurant.incerment_number_served()
"""
9-5
"""
class User:

    def __init__(self, first_name, last_name, age, sex, num):
        self.name = first_name + last_name
        self.age = str(age)
        self.sex = sex
        self.num = num
        self.login_attempts = 0

    def describe_user(self):

        if self.sex == '男':
            print(self.name + " is " + self.age + " and his number is " + self.num)
        else:
            print(self.name + " is " + self.age + " and her number is " + self.num)

    def greet_user(self):
        print(self.name + " Welcome")

    def increment_login_attempts(self):
        self.login_attempts = self.login_attempts + 1
        print(self.login_attempts)

    def reset_login_attempts(self):
        self.login_attempts = 0
        print(self.login_attempts)

user = User('wen', 'wang', 25, '女', '123456789')
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.reset_login_attempts()
"""
9-6
"""
class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
        self.flavors = []

    def describe_restaurant(self):
        print(self.restaurant_name + " is a " + self.cuisine_type + "cuisine_type")

    def open_restaurant(self):
        print(self.restaurant_name + " is busy")

    def set_number_served(self):
        self.number_served = 1
        print("就餐人数" + str(self.number_served))

    def incerment_number_served(self):
        self.number_served = self.number_served + 1
        print(str(self.number_served))

class IceCreamStand(Restaurant):
    def show_icecream(self):
        print("ice cream:")
        for flavor in self.flavors:
            print(flavor)

    def recived_flavors(self):
        flavor = input("Please enter ice cream：\n")
        self.flavors.append(flavor)

icecreamstand = IceCreamStand('wwp', 'zcy')
icecreamstand.recived_flavors()
icecreamstand.show_icecream()
"""
9-7
"""
class User:

    def __init__(self, first_name, last_name, age, sex, num):
        self.name = first_name + last_name
        self.age = str(age)
        self.sex = sex
        self.num = num
        self.login_attempts = 0

    def describe_user(self):

        if self.sex == '男':
            print(self.name + " is " + self.age + " and his number is " + self.num)
        else:
            print(self.name + " is " + self.age + " and her number is " + self.num)

    def greet_user(self):
        print(self.name + " Welcome")

    def increment_login_attempts(self):
        self.login_attempts = self.login_attempts + 1
        print(self.login_attempts)

    def reset_login_attempts(self):
        self.login_attempts = 0
        print(self.login_attempts)

class Admin(User):
    def __init__(self, first_name, last_name, age, sex, num):
        super().__init__(first_name, last_name, age, sex, num)
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        for privilege in self.privileges:
            print(privilege)

user = Admin('wenping', 'wang', 25, '女', '1234567')

user.show_privileges()
"""
9-8
"""
class User:

    def __init__(self, first_name, last_name, age, sex, num):
        self.name = first_name + last_name
        self.age = str(age)
        self.sex = sex
        self.num = num
        self.login_attempts = 0

    def describe_user(self):

        if self.sex == '男':
            print(self.name + " is " + self.age + " and his number is " + self.num)
        else:
            print(self.name + " is " + self.age + " and her number is " + self.num)

    def greet_user(self):
        print(self.name + " Welcome")

    def increment_login_attempts(self):
        self.login_attempts = self.login_attempts + 1
        print(self.login_attempts)

    def reset_login_attempts(self):
        self.login_attempts = 0
        print(self.login_attempts)

class Privileges:
    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        for privilege in self.privileges:
            print(privilege)

class Admin(User):
    def __init__(self, first_name, last_name, age, sex, num):
        super().__init__(first_name, last_name, age, sex, num)
        self.privileges = Privileges()

    def show_privileges(self):
        self.privileges.show_privileges()

admin = Admin('wenping', 'wang', 25, '女', '1234567')

admin.show_privileges()
"""
9-9
"""
class Car:

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, milegeage):
        if milegeage >= self.odometer_reading:
            self.odometer_reading = milegeage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles


class Battery:

    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kWh battery")

    def upgrade_battery(self):
        if self.battery_size != 85:
            self.battery_size = 85

    def get_range(self):

        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = "This car can go approximately " + str(range)
        message += "miles on a full charge."
        print(message)
        self.upgrade_battery()


class ElectricCar(Car):

    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery_size = Battery()

    def describe_battery(self):
        self.battery_size.battery_size

    def get_range(self):
        self.battery_size.get_range()


my_car = ElectricCar('battery', 'model s', 2019)
my_car.get_range()
my_car.get_range()


