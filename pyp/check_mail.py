from pyp.queries_db import *


valid_characters = 'qwertyuiopasdfghjklzxcvbnm1234567890@.'
services = ['gmail.com', 'yandex.ru', 'mail.ru', 'icloud.com']

# Создания собственных исключений.


class DbError(Exception):
    pass


class IncorrectSymbol(Exception):
    pass


class PointsError(Exception):
    pass


class ServiceError(Exception):
    pass


# Функция для проверки почтового адреса на правильность.
def check_mail(email):
    global valid_characters
    # Если во время проверки возникли ошибки, то возращаем соотвествующую ошибку.
    # Если все хорошо, возращаем True.
    try:
        if set(email.lower()) <= set(valid_characters):
            if email.count('..'):
                raise PointsError
            if email.count('@') != 1:
                raise SyntaxError
            if email.count('.') != 1:
                raise SyntaxError
            name, service = email.split('@')
            if not name or not service:
                raise SyntaxError
            if service not in services:
                raise ServiceError
            query_db = email_db(email)
            if query_db:
                raise DbError
            return email, True
        else:
            raise IncorrectSymbol
    except DbError:
        return 'аккаунт с такой почтой уже существует', False
    except IncorrectSymbol:
        return 'в адресе использованы неккоректные символы', False
    except PointsError:
        return 'адрес не может содержать подряд идущие точки', False
    except SyntaxError:
        return 'неверный синтаксис адреса', False
    except ServiceError:
        return 'извините, но данное доменное имя не поддерживается', False
