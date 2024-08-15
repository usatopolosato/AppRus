import sqlite3

'''Функция, которая добавляет в базу данных пользователей(в таблицу dates) некую информацию о 
пользователе. Нужна при регистрации пользователя в систему.'''


def add_data(name, email, surname, clas):
    con = sqlite3.connect('db/users.sqlite')
    cur = con.cursor()
    query = '''INSERT INTO dates(name, email, surname, class) VALUES(?, ?, ?, ?) RETURNING id'''
    result = cur.execute(query, (name, email, surname, clas)).fetchone()
    con.commit()
    return result[0]


'''Функция, которая добавляет в базу данных пользователей(в таблицу accounts) некую информацию о 
пользователе. Нужна при регистрации пользователя в систему.'''


def add_account(login, password, id_data, id_statistic):
    con = sqlite3.connect('db/users.sqlite')
    cur = con.cursor()
    query = '''INSERT INTO accounts(login, password, data, statistic) VALUES(?, ?, ?, ?)'''
    cur.execute(query, (login, str(password), id_data, id_statistic))
    con.commit()


'''Функция, которая добавляет в базу данных пользователей(в таблицу statistics) некую информацию о 
пользователе. Нужна при регистрации пользователя в систему.'''


def add_statistic():
    con = sqlite3.connect('db/users.sqlite')
    cur = con.cursor()
    query = '''INSERT INTO statistics(statistic) VALUES(?) RETURNING id'''
    statistic = '_'.join(["0 0"] * 26)
    result = cur.execute(query, (statistic, )).fetchone()
    con.commit()
    return result[0]


'''Функция, которая обновляет статистику пользователя. Обновление происходит после получения
   результата тестирования(раздел Практика).'''


def new_statistic(login, password, task, answer):
    con = sqlite3.connect('db/users.sqlite')
    cur = con.cursor()
    query = '''SELECT statistic FROM accounts WHERE login = ? AND password = ?'''
    #  Получаем id пользователя в таблице статистика.
    id_statistic = cur.execute(query, (login, password)).fetchone()[0]
    query = '''SELECT statistic FROM statistics WHERE id = ?'''
    statistic = cur.execute(query, (id_statistic, )).fetchone()[0]
    # Получаем статистику пользователя.
    statistic = list(map(lambda x: list(map(int, x.split())), statistic.split('_')))
    if answer:
        statistic[task][0] += 1
    else:
        statistic[task][1] += 1
    # Изменяем статистику пользователя.
    statistic = '_'.join([' '.join(list(map(str, x))) for x in statistic])
    query = '''UPDATE statistics SET statistic = ? WHERE id = ?'''
    cur.execute(query, (statistic, id_statistic))
    # Сохраняем изменения.
    con.commit()
