
# Operations on strings/Operacje na lancuchach znaków

message = 'Hello Flat'+ ' ' + 'World'
new_message = message.replace('Flat', 'Spheric')
print(new_message)


greeting = 'Witaj'
name = 'uzytkowniku'

placeholder = f'{greeting.lower()} { name.upper()[0:]}. Koniec'
print(placeholder)

Sentence = 'sItanbuls assd'

print(Sentence[:7])
print(Sentence.find('s'))



changer = 'Hello World d lod'

new_changer = changer.replace('lod', ' ,Universe is Flat')


print(new_changer)

print('g' + 3**3*'o' + 'l')

# Liczby/Numbers


absolute = abs(-4)

print('Wartosc bezgledna: ', absolute)

print('Reszta z dzielenia:')

print(3%2)
print(2%2)
print(4%2)
print(5%2)

print('Zaokraglanie liczb:')

print(round(7.4324,0))

print(round(5.7548, 3))

num = 2
num = 10

print(num)

x = int('100')
y = int('a')

print(x + y)