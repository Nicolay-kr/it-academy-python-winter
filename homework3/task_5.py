# Уникальные элементы в списке
# Дан список. Выведите те его элементы, которые встречаются в списке
# только один раз. Элементы нужно выводить в том порядке, в котором
# они встречаются в списке.

lst = [s for s in input('Введите элементы списка через пробел: ').split()]
lst1 = []
for element in lst:
    if lst.count(element) == 1:
        lst1.append(element)
print(lst1)
