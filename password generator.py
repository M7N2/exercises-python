# Password generator.
from random import choice

letters = 'abcdefghijklmnopqrstuvwxyz'
upper_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789' 
all_chars = letters + upper_letters + numbers
users_list = ['oliver', 'michael', 'tomas', 'kate']               


def generate_password(length):
    """Password generator from all_chars"""
    while True:
        password = ''
        for i in range(length):
            password += choice(all_chars)
        return password

# Test.        
password_1 = generate_password(8)
print(password_1)


def check_password_strength(password):
    """Check password for: string length, capital letter and number"""
    length_ok = False
    has_upper = False
    has_digit = False
   
    if len(password) >= 8:  # Length check.
        length_ok = True
    else:
        length_ok = False   
    
    for char in password: # проверка на заглавную букву
        if char.isupper():
            has_upper = True
            break
    
    for char in password: # проверка на наличие цифры
        if char.isdigit():
            has_digit = True
            break

    if length_ok and has_upper and has_digit: # оценка силы пароля
        return "Strong"
    elif ((length_ok and has_upper) or
        (length_ok and has_digit) or
        (has_upper and has_digit)):
        return "Medium"
    else:
        return "Weak"

# Test
print(check_password_strength(password_1))  


def create_user_passwords(users):
    """добавляем список имен пользователей, генерация паролей для каждого"""
    user_passwords = {} # пустой словарь
    for user in users:
        password = generate_password(8)
        user_passwords[user] = password # заполнение словаря
    return user_passwords

       
def show_user_passwords(users):
    """отображает список пользователей и их пароли"""
    users_and_passwords = create_user_passwords(users)
    print("\nUsers and passwords:")
    for name, password in users_and_passwords.items():
        strength = check_password_strength(password)
        print(f"\t{name.title()}: {password} - {strength}")


create_user_passwords(users_list)
show_user_passwords(users_list)
