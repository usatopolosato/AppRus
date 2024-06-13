import sqlite3
import random


# Проверка есть ли пользователь в БД
def check_db(login, password):
    con = sqlite3.connect('db/users.sqlite')
    cur = con.cursor()
    query = '''SELECT * FROM accounts WHERE login = ? AND password = ?'''
    result = cur.execute(query, (login, password)).fetchall()
    return result


# Проверка зарегистрирован ли пользователь с таким логином
def check_login(login):
    con = sqlite3.connect('db/users.sqlite')
    cur = con.cursor()
    query = '''SELECT * FROM accounts WHERE login = ?'''
    result = cur.execute(query, (login, )).fetchall()
    return result


# Функция, возращающая имя и фамилию пользователя по заданному логину и паролю
def query_data(login, password):
    con = sqlite3.connect('db/users.sqlite')
    cur = con.cursor()
    query = '''SELECT name, surname FROM dates INNER JOIN accounts
    ON accounts.data = dates.id WHERE accounts.login = ? AND accounts.password = ?'''
    result = cur.execute(query, (login, password)).fetchall()
    return result if result else [('ИМЯ', 'ФАМИЛИЯ')]


# Проверка зарегистрирован ли пользователь с таким почтовым адресом
def email_db(mail):
    con = sqlite3.connect('db/users.sqlite')
    cur = con.cursor()
    query = '''SELECT id FROM dates WHERE email = ?'''
    result = cur.execute(query, (mail, )).fetchall()
    return result


# Функция, возращающая html код по заданному id задания
def html_theory(title):
    con = sqlite3.connect('db/theory_database.sqlite')
    cur = con.cursor()
    query = '''SELECT html FROM data_html INNER JOIN tasks ON data_html.task == tasks.id
     WHERE tasks.title = ?'''
    result = cur.execute(query, (title,)).fetchall()
    return result[0][0]


# Функция составляет вариант по заданному кол-ву заданий и возращает результат.
def make_up_exem(quantity):
    id_questions = []
    con = sqlite3.connect('db/questions_database.sqlite')
    cur = con.cursor()
    query = '''SELECT  questions.id,  questions."group",  questions.task, groups.title,  tasks.title
     FROM (questions INNER JOIN groups
         ON questions."group" = groups.id) INNER JOIN tasks ON tasks.id = questions.task'''
    id_db = cur.execute(query).fetchall()
    groups_1_3 = [i for i in range(1, 11)]
    groups_22_26 = [i for i in range(1, 11)]
    # Создание неких групп 1-3 задания(сделано для того, чтобы пользователь чувствовал себя
    # комфортнее при решении заданий 1-3, работая с одним текстом)
    while quantity[0] != 0 or quantity[1] != 0 or quantity[2] != 0:
        group = random.choice(groups_1_3)
        del groups_1_3[groups_1_3.index(group)]
        task1 = list(filter(lambda x: x[1] == group and x[2] == 1, id_db))
        task2 = list(filter(lambda x: x[1] == group and x[2] == 2, id_db))
        task3 = list(filter(lambda x: x[1] == group and x[2] == 3, id_db))
        if quantity[0] != 0:
            id_questions.append(task1[0][0])
            quantity[0] -= 1
        if quantity[1] != 0:
            id_questions.append(task2[0][0])
            quantity[1] -= 1
        if quantity[2] != 0:
            id_questions.append(task3[0][0])
            quantity[2] -= 1
    # Генерация вопросов 4-21
    for i, el in enumerate(quantity):
        if i in [0, 1, 2, 21, 22, 23, 24, 25]:
            continue
        groups = [i for i in range(1, 11)]
        while el != 0:
            group = random.choice(groups)
            del groups[groups.index(group)]
            task = list(filter(lambda x: x[1] == group and x[2] == i + 1, id_db))
            id_questions.append(task[0][0])
            el -= 1
    # Создание неких групп 22-26 задания(сделано для того, чтобы пользователь чувствовал себя
    # комфортнее при решении заданий 22-26, работая с одним текстом)
    while (quantity[21] != 0 or quantity[22] != 0 or quantity[23] != 0 or
           quantity[24] != 0 or quantity[25] != 0):
        group = random.choice(groups_22_26)
        del groups_22_26[groups_22_26.index(group)]
        task22 = list(filter(lambda x: x[1] == group and x[2] == 22, id_db))
        task23 = list(filter(lambda x: x[1] == group and x[2] == 23, id_db))
        task24 = list(filter(lambda x: x[1] == group and x[2] == 24, id_db))
        task25 = list(filter(lambda x: x[1] == group and x[2] == 25, id_db))
        task26 = list(filter(lambda x: x[1] == group and x[2] == 26, id_db))
        if quantity[21] != 0:
            id_questions.append(task22[0][0])
            quantity[21] -= 1
        if quantity[22] != 0:
            id_questions.append(task23[0][0])
            quantity[22] -= 1
        if quantity[23] != 0:
            id_questions.append(task24[0][0])
            quantity[23] -= 1
        if quantity[24] != 0:
            id_questions.append(task25[0][0])
            quantity[24] -= 1
        if quantity[25] != 0:
            id_questions.append(task26[0][0])
            quantity[25] -= 1
    # Возварщаем id заданий
    return id_questions


# Функция, возращающая html код по заданному id вопроса
def html_quastion(id_t):
    con = sqlite3.connect('db/questions_database.sqlite')
    cur = con.cursor()
    query = '''SELECT task_text FROM questions WHERE id = ?'''
    result = cur.execute(query, (id_t, )).fetchone()
    return result[0]


# Функция, возращающая номер задания по заданному id вопроса
def number_quastion(id_t):
    con = sqlite3.connect('db/questions_database.sqlite')
    cur = con.cursor()
    query = '''SELECT task FROM questions WHERE id = ?'''
    result = cur.execute(query, (id_t, )).fetchone()
    return result[0]


# Функция, возращающая ответы на задания по заданным id вопроса
def answer_question(id_questions):
    con = sqlite3.connect('db/questions_database.sqlite')
    cur = con.cursor()
    answers = []
    for el in id_questions:
        query = '''SELECT answer FROM questions WHERE id = ?'''
        answers.append(cur.execute(query, (el, )).fetchone()[0])
    return answers


# Функция, возращающая статистику пользователя(login, password) по заданному вопросу
def statistic_task(login, password, task):
    con = sqlite3.connect('db/users.sqlite')
    cur = con.cursor()
    query = '''SELECT statistic FROM accounts WHERE login = ? AND password = ?'''
    id_statistic = cur.execute(query, (login, password)).fetchone()[0]
    query = '''SELECT statistic FROM statistics WHERE id = ?'''
    statistic = cur.execute(query, (id_statistic,)).fetchone()[0]
    return list(map(lambda x: list(map(int, x.split())), statistic.split('_')))[task - 1]
