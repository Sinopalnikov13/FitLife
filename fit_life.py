# Проект FitLife - MVP версия 1.0


# 1. Знакомство
user_name = input('Ведите ваше имя: ')
user_age = int(input('Сколько вам полных лет: '))


# 2. Сбор данных
user_weight = float(input('Введите ваш вес в килограммах: '))
user_height = float(input('Введите ваш рост в метрах (например, 1.75): '))


# 3. Логика расчетов
# Формула ИМТ: вес разделить на (рост в квадрате)
def get_bmi(weight, height):
    """Возвращает индекс массы тела"""
    bmi = weight / height ** 2
    return round(bmi, 1)


# Подсчет воды: вес * 30 мл
def get_water_needed(weight):
    """Возвращает расчет потребления воды"""
    WATER_PER_KG = 30
    water_ml = (weight * WATER_PER_KG) / 1000
    return round(water_ml, 1)


# 4. Вывод результата
def print_result(name, age, weight, height):
    """Вывод результата вычислений на экран"""
    print(f"\nОтчет для пользователя: {user_name} ({user_age} лет)")
    print(f"Индекс Массы Тела: {get_bmi(user_weight, user_height)} кг/м²")
    print(f"Норма воды: {get_water_needed(user_weight)} л. в день")


print_result(user_name, user_age, user_weight, user_height)

print("Расчет окончен. Будьте здоровы!")
