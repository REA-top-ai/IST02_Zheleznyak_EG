#bool_variable = true
#print (bool_variable) - ошибка: имя true не определено

bool_variable = "true"
print (bool_variable)
print (type(bool_variable))
#переменная bool_variable имеет класс str т.к. значение переменной занесено под ковычки

bool_variable_2 = True
print (type(bool_variable_2))


print ((6 * 6) - 1 == 8 + 1) #ложно
print (13 - 7 != (3 * 2) + 1) #истинно
print (3 * (2 - 1) == 4 - 1) #истинно


user_name = input("Введите имя ")
Dmitriy_check = "Дмитрий, твое рабочее место находится в другой комнате. Отойди от чужого компьютера и займись работой!"
Welcome = "Добро пожаловать"
a = Dmitriy_check if user_name == "Дмитрий" else Welcome
print (a)


enter_number = int(input("Количество использованых попыток "))
a = "попробуйте еще раз" if enter_number < 3 else "Вы привысили количество попыток. Ваша учетная запись заблокирована. Для разблокировки обратитесь в аслужбу поддержки"
print (a)