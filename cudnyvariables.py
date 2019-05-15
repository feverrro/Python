absolute = abs(-4)
print('Wartosc bezwzgledna: ', absolute)

print(round(5.7548, 3))

x = '400'
y = '500'

print(int(x) != int(y))

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

num_1 = 4
num_2 = 5

nums_tab = [num_1, num_2, 3, 4, 6]
print(nums_tab)
nums_tab.sort()
print(nums_tab)