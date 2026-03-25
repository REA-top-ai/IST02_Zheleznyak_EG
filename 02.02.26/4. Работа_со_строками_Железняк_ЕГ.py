favour_word = "What"
print (favour_word)


first_name = "Виталий"
last_name = "Красилов"
new_account = last_name[:5]
temp_password = last_name[2:6]


first_name = input()
last_name = input()
account_generator = first_name[:3] + last_name[:3]
new_account = account_generator
print (new_account)


first_name = input()
last_name = input()
password_generator = first_name[-3:] + last_name[-3:]
temp_password = password_generator
print (temp_password)


company_motto = "Мечты сбываются"
second_to_last = company_motto[-2]
print (second_to_last)
final_word = company_motto[-4:]
print (final_word)