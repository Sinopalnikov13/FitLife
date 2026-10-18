# Проект FitLife - MVP версия 1.0


WATER_PER_KG = 30
ML_IN_LITER = 1000


# 2. Сбор и проверка корректности ввода данных
user_name = input('Ведите ваше имя: ')
while True:
    try:
        user_age = int(input('Сколько вам полных лет: '))
        if 100 > user_age > 0:
            break
        else:
            print('Значение должно быть от 0 и до 100')
    except ValueError:
        print('Введите корректное значение')
while True:
    try:
        user_weight = float(input('Введите ваш вес в килограммах: '))
        if 250 > user_weight > 0:
            break
        else:
            print('Значение должно быть от 0 и до 250 киллограмм')
    except ValueError:
        print('Введите корректное значение')
while True:
    try:
        user_height = float(input('Введите ваш рост в метрах : '))
        if 2.30 > user_height > 0.40:
            break
        else:
            print('Значение должно быть от 0.40 мета и до 2.30 метров')
    except ValueError:
        print('Введите корректное значение (например, 1.75)')


# 3. Логика расчетов
# Формула ИМТ: вес разделить на (рост в квадрате)
def get_bmi(weight, height):
    """Возвращает индекс массы тела"""
    bmi = weight / height ** 2
    return round(bmi, 1)


# Подсчет воды: вес * 30 мл
def get_water_needed(weight):
    """Возвращает расчет потребления воды"""
    water_ml = (weight * WATER_PER_KG) / ML_IN_LITER
    return round(water_ml, 1)


# 4. Вывод результата

bmi = get_bmi(user_weight, user_height)
water_liters = get_water_needed(user_weight)
print(f"\nОтчет для пользователя: {user_name} ({user_age} лет)")
print(f"Индекс Массы Тела: {bmi} кг/м²")
print(f"Норма воды: {water_liters} л. в день")


print("Расчет окончен. Будьте здоровы!")
