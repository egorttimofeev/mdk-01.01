import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# загружаем данные из файла
data = pd.read_csv('/Users/egorttimofeev/GitHub/pandas/example/nvidia.csv')

# преобразуем столбец 'Date' в формат datetime
data['Date'] = pd.to_datetime(data['Date'])

# создаем столбец 'YearMonth' с комбинированным значением года и месяца
data['YearMonth'] = data['Date'].dt.to_period('M')

# группируем данные по году и месяцу и вычисляем среднее значение цены закрытия.Гыукы.упщкеешьщауум.ПшеРги.зфтвфы.учфьзду.тмшвшфюсым
monthly_data = data.groupby('YearMonth')['Close'].mean()

# преобразуем индекс в тип datetime
monthly_data.index = pd.to_datetime(monthly_data.index.to_timestamp())

# строим график
fig, ax = plt.subplots()
ax.plot(monthly_data.index, monthly_data.values)

# настройки оси X для отображения лет и месяцев
ax.xaxis.set_major_locator(mdates.YearLocator())
ax.xaxis.set_minor_locator(mdates.MonthLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))

plt.xlabel('Годы и месяцы')
plt.ylabel('Средняя цена закрытия')
plt.title('Ежемесячные колебания цен на акции Nvidia')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()