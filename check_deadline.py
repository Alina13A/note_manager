from datetime import datetime

username = input('Имя пользователя: ')
titles = ([input('Заголовок 1: '), input('Заголовок 2: '), input('Заголовок 3: ')])

while True:

    title_new = input('Введите заголовок или оставьте пустым для завершения: ')

    if title_new == "":
        print('Завершение ввода заголовков')
        break
    titles.append(title_new)

content = input('Описание: ')


status = input('Текущий статус заметки: ')

while True:

    number = input('Введите новый статус заметки (номер): "1.Выполнено", "2.В процессе", "3.Отложено": ')

    if number == '1':
        print('Статус заметки успешно обновлён на: Выполнено')
        break
    elif number == '2':
        print('Статус заметки успешно обновлён на: В процессе')
        break
    elif number == '3':
        print('Статус заметки успешно обновлён на: Отложено')
        break
    else:
        print('Некорректный ввод. Попробуйте еще раз')

while True:
    created_date_input = input('Введите дату создания заметки в формате "день-месяц-год": ')
    issue_date_input = input('Введите дату истечения заметки (дедлайн) в формате "день-месяц-год": ')

    try:
        created_date = datetime.strptime(created_date_input, '%d-%m-%Y')
        issue_date = datetime.strptime(issue_date_input, '%d-%m-%Y')
        delta = issue_date - created_date

        print(f'Разница в днях: {delta.days}.')

        if delta.days < 0:
            print(f'Внимание! Дедлайн истёк на {abs(delta.days)} дня(-ей) назад.')
        elif delta.days > 0:
            print(f'До дедлайна осталось {delta.days} день(-дня/-ней).')
        else:
            print('Дедлайн истекает сегодня!')

        break  # Если даты корректные, выходим из цикла

    except ValueError:
        print('Некорректный ввод даты. Пожалуйста, используйте формат "день-месяц-год". Попробуйте ещё раз.')


note = [username,
        titles,
        content,
        status,
        created_date,
        issue_date]

print('Имя пользователя: ', note[0])
print('Заголовки: ', note[1])
print('Описание: ', note[2])
print('Статус: ', note[3])
print(f'Дата создания заметки в формате "день-месяц-год": {created_date.strftime("%d-%m-%Y")}')
print(f'Дата истечения заметки (дедлайн) в формате "день-месяц-год": {issue_date.strftime("%d-%m-%Y")}')

