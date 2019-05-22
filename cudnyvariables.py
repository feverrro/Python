absolute = abs(-4)
print('Wartosc bezwzgledna: ', absolute)

print(round(5.7548, 3))

x = '400'
y = '500'

print(int(x) != int(y))
print('___________________________________________________')

#tables
tab = [True, False, True, True]
tab_index = 2
print(tab[tab_index])
print(len(tab))
print(tab[:2])
tab.append('ASx')
tab.append(1.2)

tab_2 = ['Kappa', abs(-1)]
tab.insert(1, tab_2)

print(tab[tab_2[1]])

tab.remove('ASx')
popped = tab.pop()
print(popped)
print(tab)
tab.reverse()
print(tab)
print('___________________________________________________')

num_1 = 4
num_2 = 5

nums_tab = [num_1, num_2, 3, 4, 6]
print(nums_tab)
nums_tab.sort()
print(nums_tab)

nums_tab.extend(tab)
print(nums_tab)
print('___________________________________________________')

tab_words = ['One', 'Two', 'Three', 'Four', 'Five']
tab_words_str = ' - '.join(tab_words)
print(tab_words_str)
new_list = tab_words_str.split(' - ')
print(new_list)
print('___________________________________________________')

#mutable
#Lists
list_1 = ['One', 'Two', 'Three', 'Four', 'Five']
list_2 = list_1
print(list_1)
print(list_2)

list_1[0] = 'Art'
print(list_1)
print(list_2)

#immutable
#Tuples
tuple_1 = ('One', 'Two', 'Three', 'Four', 'Five')
tuple_2 = tuple_1
print(tuple_1)
print(tuple_2)
#to nie zadziala
#tuple_1[0] = 'Art'
#print(tuple_1)
#print(tuple_2)
print('___________________________________________________')

#Sets
cs_nums = {'One', 'Two', 'Three', 'Four', 'Five'}
cs_nums_2 = {'Six', 'Two', 'Seven', 'Eight', 'Five'}
print(cs_nums)
print('One' in cs_nums)
print('Six' in cs_nums)
print(cs_nums.intersection(cs_nums_2))
print(cs_nums.difference(cs_nums_2))
print(cs_nums.union(cs_nums_2))
print('___________________________________________________')

#empty lists/touples/sets
empty_list = []
empty_list = list()

empty_tuple = ()
empty_tuple = tuple()

empty_set = {} # <- not right
empty_set = set()
print('___________________________________________________')

#Dictioneries
car = {'brand': 'Renault', 'BHP': '98', 'add_ons': ['electric windows', 'automatic gearbox']}
print(car['brand'])
print(car.get('add_ons'))
print(car.get('enigine', 'not found!'))
car['engine'] = 'R4 1800ccm'
car['brand'] = 'Citroen'
print(car)
car.update({'brand': 'Audi', 'BHP': '110', 'v-max': '180km/h'})
print(car)
# del car['engine']
# print(car)
engine = car.pop('engine')
print(engine)
print(len(car))
print(car.values())
print(car.items())

for key, value in car.items():
    print(key, value)
print('___________________________________________________')

#conditionals and bools

condition = 'amp'
if condition  == 'amp':
    print('trafiles')
elif condition == 'bmp':
    print('so close')
else:
    print('pudlo')

# conditionals:
# and
# or
# not

user = 'admin'
logged_in = False
if user == 'admin' and logged_in:#
    print('admin page')
elif user == 'admin' and not logged_in:
    print('please log in')
else:
    print('failed')

tab_a = [1, 2, 3]
tab_b = [1, 2, 3]

print(tab_a == tab_b, id(tab_a))
print(tab_a is tab_b, id(tab_b))
print('')
tab_b = tab_a
print(tab_a == tab_b, id(tab_a))
print(tab_a is tab_b, id(tab_b))
print('___________________________________________________')

# False Values:
# False
# None
# Zero of any numeric type
# Any empty sequence. For example: '', (), []
# Any empty mapping. For example: {}

condition = False
if condition:
    print('True')
else:
    print('False')
    
print('___________________________________________________')

#Loops

nums = [1, 2, 3, 4, 5]
for num in nums:
    for letter in 'abc':
        if num == 3:
            print('found!', letter)
            continue
        else:
            print(num, letter)

print('___________________________________________________')

for i in range(10):
    print(i)

x = 0
while x < 10:
    if x == 5:
        print('pienc')
        x += 1
    else:
        print(x)
        x += 1

#infinite loop
# while True:
#     print('a')

print('___________________________________________________')

#functions

def hello_func(first_word, name = "wieje"):
    return '{} {}'.format(first_word, name)
    
print(hello_func('skond', 'pizdzi'))

def function_info(*args, **kwargs):
    print(args)
    print(kwargs)

function_info('abc', 'cba', name = 'Janusz', age = 44)

cars = ['Seat', 'Fiat']
info = {'isfast': True, 'seat-s num': 5}

function_info(*cars, **info)

print('___________________________________________________')

month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap(year):
    """Return True for leap years, False for non leap years."""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

print(is_leap(2020))

def days_in_month(year, month):
    """Return number of days in that year in that month"""
    if not 1 <= month <= 12:
        return 'Invalid month!'
    if month == 2 and is_leap(year):
        return 29
    return month_days[month]

print(days_in_month(2019, 12))