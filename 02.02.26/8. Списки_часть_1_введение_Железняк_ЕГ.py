cake = ["торт", 1]


household_chemicals = [["стиральный порошок", 1], ["средство для мытья посуды", 1]]


Names = ["Ben", "Holly", "Ann"]
dogs_names = ["Sharik", "Gab", "Beethoven"]
names_and_dogs_names = zip(Names, dogs_names)
list_of_names_and_dogs_names = list(names_and_dogs_names)
print (list_of_names_and_dogs_names)


orders = ['маргаритки', 'васильки']
print(orders)
orders.append('тюльпаны')
orders.append('розы')
print(orders)


orders = ['маргаритка', 'лютик', 'львиный зев', 'гардения', 'лилия']
new_orders = orders + ['сирень', 'ирис']
print(new_orders)

broken_prices = [5, 3, 4, 5, 4] + [4]
print(broken_prices)