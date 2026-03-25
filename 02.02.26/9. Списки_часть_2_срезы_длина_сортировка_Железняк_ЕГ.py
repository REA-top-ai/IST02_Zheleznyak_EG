list1 = range(2, 20, 2)
list1_len = len(list1)
print(list1_len)

list1 = range(2, 20, 3)
list1_len = len(list1)
print(list1_len)

#изменится шаг перебора чисел, следовательно длина списка уменьшится


shopping_list = ['яйца', 'масло', 'молоко', 'огурцы', 'сок', 'хлопья']
print(len(shopping_list))

last_element = shopping_list[-1]
element5 = shopping_list[5]

print(element5)
print(last_element)


suitcase = ['рубашка', 'рубашка', 'брюки', 'брюки', 'пижамы', 'книги']
beginning = suitcase[0:2]
print(beginning)
print(len(suitcase))

beginning = suitcase[0:4]
print(beginning)

middle = suitcase[2:4]
print(middle)


suitcase = ['рубашка', 'футболка', 'носки', 'очки', 'пижама', 'книги']
start = suitcase[0:3]
print(start)


votes = ['Jake', 'Jake', 'Laurie', 'Laurie', 'Laurie', 'Jake', 'Jake', 'Jake', 'Laurie', 'Cassie', 'Cassie', 'Jake', 'Jake', 'Cassie', 'Laurie', 'Cassie', 'Jake', 'Jake', 'Cassie', 'Jake']

jake_votes = votes.count('Jake')
print(jake_votes)


addresses = ['221 B Baker St.', '42 Wallaby Way', '12 Grimmauld Place', '742 Evergreen Terrace', '1600 Pennsylvania Ave', '10 Downing St.']
print(addresses)
addresses.sort()
print(addresses)


