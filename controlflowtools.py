
condition = ''

if condition:
    print('Evaluating to True')
else:
    print('Evaluating to False')

import sys

print(sys.version)

print('------------------------------------------------------------------------------------')

print(sys.executable)

('------------------------------------------------------------------------------------')


# Fibonacci series:
# the sum of two elements defines the next

a, b = 0, 1
while a <= 34:
  
    print(a)
    a, b = b, a+b

print('------------------------------------------------------------------------------------')

x = int(0)

if x < 0:
    x = 0
    print('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')

print('------------------------------------------------------------------------------------')

words = ['cat', 'dog', 'parrot']

for w in words:
    print(w, len(w))

print('------------------------------------------------------------------------------------')

for w in words[:]: #loops over a slice copy of the entire list
    if(len(w)) >= 6:
        print(w, len(w)) 

print(words)

for i in range(10):
    print(i)

a = ['Mary', 'has', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])

seasons = ['Spring', 'Summer', 'Fall', 'Winter']

print(list(enumerate(seasons)))

print(range(10))

print(list(range(5)))

print('------------------------------------------------------------------------------------')

for n in range(2, 10):
    for x in range(2,n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
        break
    else: # Loop fell through without finding a factor
        print(n, 'is a prime number')

for num in range(2, 10):
    if num % 2 == 0:
        print("Found an even number", num)
        continue
    print("Found a number", num)

while True:
    pass # Busy-wait for keyboard interrupt(Ctrl + C)

###################################################

print('dda')

nums = [1, 2, 3, 4, 5]

for n in nums:
    print(n)
