# Проект FitLife - MVP версия 1.0


# 1. Константы для проекта
WATER_PER_KG = 30
ML_IN_LITER = 1000
AGE_MIN = 0
AGE_MAX = 100
WEIGHT_MIN = 0
WEIGHT_MAX = 250
HEIGHT_MIN = 0.40
HEIGHT_MAX = 2.30


# 2. Сбор и проверка корректности ввода данных
user_name = input('Ведите ваше имя: ')
while True:
    try:
        user_age = int(input('Сколько вам полных лет: '))
        if AGE_MAX > user_age > AGE_MIN:
            break
        else:
            print(f'Значение должно быть от {AGE_MIN} и до {AGE_MAX}')
    except ValueError:
        print('Введите корректное значение')
while True:
    try:
        user_weight = float(input('Введите ваш вес в килограммах: '))
        if WEIGHT_MAX > user_weight > WEIGHT_MIN:
            break
        else:
            print(f'Значение должно быть от '
                  f'{WEIGHT_MIN} и до {WEIGHT_MAX} киллограмм')
    except ValueError:
        print('Введите корректное значение')
while True:
    try:
        user_height = float(input('Введите ваш рост в метрах : '))
        if HEIGHT_MAX > user_height > HEIGHT_MIN:
            break
        else:
            print(f'Значение должно быть от '
                  f'{HEIGHT_MIN} метра и до {HEIGHT_MAX} метров')
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
