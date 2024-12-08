from datetime import datetime

# Змінні з інформацією
name = "Назар"
location = "Львів"
activity = "програмувати"
mood = "натхненно"  # Додано настрій
weather = "сонячна погода"  # Додано опис погоди

# Отримуємо поточний час у форматі "день.місяць.рік години:хвилини"
current_time = datetime.now().strftime("%d.%m.%Y %H:%M:%S")

# Додано більше деталей у вивід
print(f"""{">*<"*20}
{name} почав {activity} {current_time}. 
{location} — чудове місто з {weather} сьогодні. 
Назар працює {mood} і планує досягти великих результатів!
{"<*>"*20}""")