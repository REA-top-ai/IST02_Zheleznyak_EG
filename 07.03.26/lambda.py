#Задание 1
contains_a = lambda check: "a" in check
print(contains_a(input()))


#Задание 2
long_string = lambda string: len(string) > 12
print(long_string(input()))


#Задание 3
end_in_a = lambda stroka: stroka[-1] == "a"
print(end_in_a(input()))


#Задание 4
even_or_odd = lambda num: "четное" if int(num)%2 == 0 else "нечетное"
print(even_or_odd(input()))


#Задание 5
multiple_three = lambda num: "кратно трем" if int(num) % 3 == 0 else "не кратное"
print(multiple_three(input()))


#Задание 6
rate_movie = lambda rating: "Мне нравится этот фильм" if float(rating) > 8.5 else "Этот фильм был не очень хорошим"
print(rate_movie(input()))
