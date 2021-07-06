# -*- coding: utf-8 -*-

# Цикл while (повторение части кода)

# while <условие>:
#     <блок кода>
# ВНОСИМ НЕПОПРАВИМЫЕ УЛУЧШЕНИЯ, ЧТОБ СОЗДАТЬ POOL REQUEST
print('дратути!')
i = 1
while i < 10:
    i = i * 2
    print(i)
print('дотвидания!')
# ВНОСИМ НЕПОПРАВИМЫЕ УЛУЧШЕНИЯ, ЧТОБ СОЗДАТЬ POOL REQUEST

# else
i = 1
while i < 10:
    i *= 2
    print(i)
else:
    print('i >= 10')
print('дотвиданя!')

# break
my_pets = ['cat', 'dog', 'hamster']
i = 0
while i < len(my_pets):
    pet = my_pets[i]
    print('Проверяем ', pet)
    if pet == 'cat':
        print('Ура, кот найден!')
    i += 1
print('дотвиданя!')

# ВНОСИМ НЕПОПРАВИМЫЕ УЛУЧШЕНИЯ, ЧТОБ СОЗДАТЬ POOL REQUEST
# continue
my_pets = ['lion', 'dog', 'skunk', 'hamster', 'cat', 'monkey']
i = -1
while i < len(my_pets):
    i += 1
    if i == 2:
        continue
    pet = my_pets[i]
    print('Проверяем ', pet)
    if pet == 'cat':
        print('Ура, кот найден!')
        break
print('дотвиданя!')
# ВНОСИМ НЕПОПРАВИМЫЕ УЛУЧШЕНИЯ, ЧТОБ СОЗДАТЬ POOL REQUEST

# else, break and continue - все вместе
f1, f2, count = 0, 1, 0
while f2 < 10000:
    count += 1
    if count > 27:
        print('Итераций больше чем 27. Прерываюсь.')
        break
    f1, f2 = f2, f1 + f2
    if f2 < 1000:
        continue
    print(f2)
else:
    print('Было', count, 'итераций')

# ВНОСИМ НЕПОПРАВИМЫЕ УЛУЧШЕНИЯ, ЧТОБ СОЗДАТЬ POOL REQUEST

