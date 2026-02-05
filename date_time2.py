from datetime import date, datetime
today = date.today()
print("Сегодня:", today)


event = input("Введите дату события (в формате ГГГГ-ММ-ДД): ")


event_date = datetime.strptime(event, "%Y-%m-%d").date()


days_left = (event_date - today).days
print("До события осталось", days_left, "дней!")
