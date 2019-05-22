
nums = [1, 2, 3, 4, 5]

for n in nums:
    if n == 3:
        print('Found!')
        continue
    print(n)

print('---------------------------------------')

for num in nums:
    for letter in 'abc':
        print(num, letter)

print('---------------------------------------')

for i in range(10):
    print(i)

x = 0 

print('---------------------------------------')

while x < 10:
    if x == 5:
        break
    print(x)
    x += 1 

print('---------------------------------------')



def hello_func(greeting, name = 'Youy'):
    return '{}, {} '.format(greeting, name)

print(hello_func('Hi','Function'))

print('---------------------------------------')

def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

courses = ['Math', 'Art']
info = {'name': 'John', 'age':22}

student_info(*courses, **info)