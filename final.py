
username = input('Имя пользователя: ')
titles = ([input('Заголовок 1: '), input('Заголовок 2: '), input('Заголовок 3: ')])
content = input('Описание: ')
status = input('Статус: ')
created_date = input('Дата создания заметки в формате "день-месяц-год": ')
issue_date = input('Дата истечения заметки (дедлайн) в формате "день-месяц-год": ')


note= [username,
       titles,
       content,
       status,
       created_date,
       issue_date]


print('Имя пользователя: ', note[0])
print('Заголовок: ', note[1])
print('Описание: ', note[2])
print('Статус: ', note[3])
print(f'Дата создания заметки в формате "день-месяц-год": {created_date [0:5]}')
print(f'Дата истечения заметки (дедлайн) в формате "день-месяц-год": {issue_date [0:5]}')


