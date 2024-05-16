import datetime
def calculate_age(birth_date):
    today = datetime.date.today()
    age = today.year - birth_date[0] - ((today.month, today.day) < (birth_date[1], birth_date[2]))
    return age
birth_date = (2013, 1, 17)
print(calculate_age(birth_date))