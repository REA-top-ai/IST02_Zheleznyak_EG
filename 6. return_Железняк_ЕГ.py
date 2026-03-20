def define_age (current_year, birth_year):
    age = current_year - birth_year
    return age

my_age = define_age(2049, 1993)
print (my_age)


def get_boundaries (target, margin):
    low_limit = target - margin
    hight_limit = margin + target
    return low_limit, hight_limit

low_limit, hight_limit = get_boundaries(100, 20)
print (f"Нижний предел: {low_limit}, верхний предел: {hight_limit}")


def repeat_stuff (stuff, num_repeats = 10):
    return stuff * num_repeats

a = repeat_stuff("Row", 3)
lyrics = a + "Your Boat"
song = repeat_stuff ("Row")
print (song)