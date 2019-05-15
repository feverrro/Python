# Operations on strings/Operacje na lancuchach znaków

# message = 'Hello Flat'+ ' ' + 'World'
# new_message = message.replace('Flat', 'Spheric')
# print(new_message)


# greeting = 'Witaj'
# name = 'uzytkowniku'

# placeholder = f'{greeting.lower()} { name.upper()[0:]}. Koniec'
# print(placeholder)

# Sentence = 'sItanbuls assd'

# print(Sentence[:7])
# print(Sentence.find('s'))



# changer = 'Hello World d lod'

# new_changer = changer.replace('lod', ' ,Universe is Flat')


# print(new_changer)

# print('g' + 3**3*'o' + 'l')

# # Liczby/Numbers


# absolute = abs(-4)

# # print('Wartosc bezgledna: ', absolute)

# # print('Reszta z dzielenia:')

#  print(3%2)
#  print(2%2)
#  print(4%2)
#  print(5%2)

# print('Zaokraglanie liczb:')

# print(round(7.4324,0))

# print(round(5.7548, 3))

# num = 2
# num = 10

# print(num)

# # x = int('100')
# y = int('a')

# print(x + y)

# Lists/listy

squares = [1, 4, 9, 16, 25]

print(squares)

squares_2 = squares + [36, 49, 64, 81, 100]

print(squares_2)

cubes = [1, 8, 27, 65, 125]

cubes[3] = 64
cubes[4] = 128

print(cubes)

cubes.append(256)

print(cubes)
print('___________________________________________________')

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters)

letters[:4] = ['A', 'B', 'C', 'D']
print(letters)

letters[4:] = []
print(letters)

letters[:] = []
letters[0:2] = ['Nowa', 'lista']
print(letters)

len(letters) 
print(len(letters))

a = [1, 2, 3]
n = ['Slownik', 'Ksiazka Fantasy', 'Poradnik']
x = [a,n]
print(x)
print(x[1][1])

x.insert(0, 'Pierwszy element')
print(x)

y = ['ostatni element', 'kolejna rzecz']
x.extend(y)
x.append(y)

x.remove('ostatni element')
print(x)

popped = x.pop()
print(popped)
print(x)

x.reverse()
print(x)

nums = [10, 20, 30, 40, 35]
nums.sort(reverse=True)
print(nums)

print('___________________________________________________')

courses = ['Math','English','Programming']
print(courses)
courses_sorted = sorted(courses)
print(courses_sorted)

print(courses.index('Math'))

print('Art' in courses)
print('Math' in courses)

for course in courses:
    print(course)

print('___________________________________________________')

for index, course in enumerate(courses, start=1):
    print(index, course)
print('___________________________________________________')

course_str = ' -'.join(courses) + '!'

print(course_str)

new_list = course_str.split(' -')

print(course_str)
print(new_list)

print('___________________________________________________')

# Tuples

tuple_1 = ('History', 'Math', 'Physics','CompSci')
tuple_2 = tuple_1

print(tuple_1)
print(tuple_2)

print('___________________________________________________')

cs_courses  = {'Art', 'Math', 'Physics','CompSci'}
art_courses  = {'Art', 'Math', 'Desing','Modeling'}

print('Math' in cs_courses)
print(cs_courses.intersection(art_courses))
print(cs_courses.difference(art_courses))
print(cs_courses.union(art_courses))

print('___________________________________________________')

empty_list = []
empty_list = list()

empty_tuple = ()
empty_tuple = tuple()

empty_set = set()