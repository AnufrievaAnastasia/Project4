# Random password and login generator.

import random

import string

length = int(input('Укажите длину пароля: '))
large_letters = str.lower(input('Разрешено ли использовать заглавные буквы? '))
special_letters = str.lower(input('Разрешено ли использовать специальные символы? '))
name = str.lower(input('ВВедите Ваше имя (на русском языке): '))
surname = str.lower(input('Введите Вашу фамилию (на русском языке): '))
symbols = '_-'

# Create a random password with restrictions.
if large_letters == 'да':
    if special_letters == 'да':
        password = ''
        for i in range(length):
            password += random.choice(string.printable)
    else:
        password = ''
        for i in range(length):
            password += random.choice(string.ascii_letters + string.digits)
else:
    if special_letters == 'да':
        password = ''
        for i in range(length):
            password += random.choice(string.punctuation +
                                      string.ascii_lowercase + string.digits)
    else:
        password = ''
        for i in range(length):
            password += random.choice(string.ascii_lowercase + string.digits)

# Transliteration of Russian words.
name_1 = name.translate({ord('ь'): '', ord('ъ'): '', ord('а'): 'a',
       ord('б'): 'b', ord('в'): 'v', ord('г'): 'g', ord('д'): 'd',
       ord('е'): 'e', ord('ё'): 'yo', ord('ж'): 'zh', ord('з'): 'z',
       ord('и'): 'i', ord('й'): 'y', ord('к'): 'k', ord('л'): 'l',
       ord('м'): 'm', ord('н'): 'n', ord('о'): 'o', ord('п'): 'p',
       ord('р'): 'r', ord('с'): 's', ord('т'): 't', ord('у'): 'u',
       ord('ф'): 'f', ord('х'): 'h', ord('ц'): 'ts', ord('ч'): 'ch',
       ord('ш'): 'sh', ord('щ'): 'sch', ord('ы'): 'yi',
       ord('э'): 'e', ord('ю'): 'yu', ord('я'): 'ya'})

name_2 = surname.translate({ord('ь'): '', ord('ъ'): '', ord('а'): 'a',
       ord('б'): 'b', ord('в'): 'v',ord('г'): 'g', ord('д'): 'd',
       ord('е'): 'e', ord('ё'): 'yo', ord('ж'): 'zh', ord('з'): 'z',
       ord('и'): 'i', ord('й'): 'y', ord('к'): 'k', ord('л'): 'l',
       ord('м'): 'm', ord('н'): 'n', ord('о'): 'o', ord('п'): 'p',
       ord('р'): 'r', ord('с'): 's', ord('т'): 't', ord('у'): 'u',
       ord('ф'): 'f', ord('х'): 'h', ord('ц'): 'ts', ord('ч'): 'ch',
       ord('ш'): 'sh', ord('щ'): 'sch', ord('ы'): 'yi',
       ord('э'): 'e', ord('ю'): 'yu', ord('я'): 'ya'})

login = name_1.capitalize() + random.choice(symbols) + name_2.capitalize()

print('Ваш логин : ', login[0:15] + random.choice(string.digits)
      + random.choice(string.digits))

print('Ваш пароль:', password)
