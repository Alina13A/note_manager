
username = input('Имя пользователя: ')
titles = [input('Заголовок 1: '), input('Заголовок 2: '), input('Заголовок 3: ')]
content = input('Описание: ')
status = input('Статус: ')
created_date = input('Дата создания заметки в формате "день-месяц-год": ')
issue_date = input('Дата истечения заметки (дедлайн) в формате "день-месяц-год": ')


print('Имя пользователя: ', username)
print('Заголовок заметки: ', titles)
print('Описание заметки: ', content)
print('Статус заметки: ', status)
print(f'Дата создания заметки в формате "день-месяц-год":  {created_date [0:5]}')
print(f'Дата истечения заметки (дедлайн) в формате "день-месяц-год":  {issue_date [0:5]}')

print(username, titles, content, status, created_date, issue_date)








