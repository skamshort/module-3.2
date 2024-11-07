def send_email(message, recipient, sender = 'university.help@gmail.com'):
    if "@" not in recipient or not (recipient.endswith(".com") or recipient.endswith(".ru") or recipient.endswith(".net")):
     # если получатель не содержит "@" или не оканчиваются на ".com"/".ru"/".net", то
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}.')# вывод на консоль строки:
        return
    if "@" not in sender or not (sender.endswith(".com") or sender.endswith(".ru") or sender.endswith(".net")):
     # если отправитель не содержит "@" или не оканчиваются на ".com"/".ru"/".net", то
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}.')# вывод на консоль строки:
        return
    if sender == recipient:# проверка на совпадение
        print("Нельзя отправить письмо самому себе!")
        return
    if sender =="university.help@gmail.com": # отправитель по умолчанию:
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}.')
    else:  #  в противном случае вывести сообщение:
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.')

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!','urban.fan@mail.ru',sender= 'urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание','urban.student@mail.ru', sender= 'urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре','urban.teacher@mail.ru', sender= 'urban.teacher@mail.ru')

