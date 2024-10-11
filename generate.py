import pandas as pd
import random
import uuid
from datetime import datetime, timedelta

# Количество записей для генерации
NUM_VACANCIES = 10000
NUM_RESUMES = 10000
NUM_AREAS = 85  # Число регионов в РФ

# Списки значений для генерации
vacancy_names = [
    'Водитель', 'Программист', 'Менеджер по продажам', 
    'Дизайнер', 'Аналитик', 'Водитель такси', 
    'Водитель грузовика', 'Инженер', 'Маркетолог', 
    'Разработчик'
]

work_schedules = ['Гибкий график', 'Полный рабочий день', 'Частичная занятость', 'Удаленная работа']

area_names = [
    'Москва', 'Санкт-Петербург', 'Новосибирск', 'Екатеринбург',
    'Казань', 'Нижний Новгород', 'Челябинск', 'Омск',
    'Ростов-на-Дону', 'Уфа', 'Красноярск', 'Пермь'
]

regions = [
    'Москва', 'Санкт-Петербург', 'Свердловская область', 
    'Татарстан', 'Нижегородская область', 'Челябинская область',
    'Омская область', 'Ростовская область', 'Калининградская область', 
    'Красноярский край'
]

currencies = {
    'RUB': 1.0,
    'USD': round(random.uniform(60.0, 90.0), 2),
    'EUR': round(random.uniform(70.0, 100.0), 2),
}

# Генерация данных для таблицы vacancy
def generate_vacancy_data(num_records):
    data = []
    for _ in range(num_records):
        vacancy_id = random.randint(1, 100000)
        name = random.choice(vacancy_names)
        work_schedule = random.choice(work_schedules)
        disabled = random.choice([True, False])
        area_id = random.randint(1, NUM_AREAS)  # Учитываем регионы
        creation_time = random_date(datetime(2020, 1, 1), datetime(2021, 12, 31)).strftime('%Y-%m-%d %H:%M:%S')
        archived = random.choice([True, False])
        if "Водитель" in name and random.choice([True, False]):
            disabled = False  # Не удаляем водителей
        data.append([vacancy_id, name, work_schedule, disabled, area_id, creation_time, archived])
    
    df = pd.DataFrame(data, columns=['vacancy_id', 'name', 'work_schedule', 'disabled', 'area_id', 'creation_time', 'archived'])
    df.to_csv('vacancy.csv', index=False, header=False)

# Генерация данных для таблицы resume с зарплатами в разных валютах и возможностью отсутствия зарплаты
def generate_resume_data(num_records):
    data = []
    for _ in range(num_records):
        resume_id = random.randint(1, 100000)
        disabled = random.choice([True, False])
        is_finished = 1  # Все резюме будут завершенными
        area_id = random.randint(1, NUM_AREAS)  # Учитываем регионы
        # Вероятность, что зарплата не указана
        if random.random() < 0.2:
            compensation = None
            currency = None
        else:
            compensation = random.randint(30000, 200000)
            # Случайный выбор валюты
            currency = random.choice(list(currencies.keys()))
            # Если валюта не рубли, пересчитаем зарплату в соответствии с курсом
            if currency != 'RUB':
                compensation = int(compensation / currencies[currency])
        position = random.choice(['Программист', 'Аналитик', 'Менеджер', 'Дизайнер', 'Водитель'])
        birth_day = (datetime(1970, 1, 1) + timedelta(days=random.randint(0, (datetime(2010, 1, 1) - datetime(1970, 1, 1)).days), hours=random.randint(0, 23), minutes=random.randint(0, 59), seconds=random.randint(0, 59))).strftime('%Y-%m-%d %H:%M:%S')
        role_id_list = random.choice([91, 92, 93, 94, 95])  # Включаем разработчиков
        data.append([resume_id, disabled, is_finished, area_id, compensation, currency, position, birth_day, role_id_list])
    
    df = pd.DataFrame(data, columns=['resume_id', 'disabled', 'is_finished', 'area_id', 'compensation', 'currency', 'position', 'birth_day', 'role_id_list'])
    df.to_csv('resume.csv', index=False, header=False)

# Генерация данных для таблицы area
def generate_area_data(num_records):
    data = []
    for i in range(num_records):
        area_id = i + 1  # Уникальный ID для каждого региона
        area_name = random.choice(area_names)
        region_name = random.choice(regions)
        country_name = 'Россия'
        data.append([area_id, area_name, region_name, country_name])
    df = pd.DataFrame(data, columns=['area_id', 'area_name', 'region_name', 'country_name'])
    df.to_csv('area.csv', index=False, header=False)

# Генерация данных для таблицы currency
def generate_currency_data():
    data = [
        ['RUB', 1.0],
        ['USD', round(random.uniform(60.0, 90.0), 2)],
        ['EUR', round(random.uniform(70.0, 100.0), 2)],
    ]
    df = pd.DataFrame(data, columns=['code', 'rate'])
    df.to_csv('currency.csv', index=False, header=False)

# Генерация случайной даты
def random_date(start, end):
    return start + timedelta(days=random.randint(0, (end - start).days))

# Генерация данных
generate_vacancy_data(NUM_VACANCIES)
generate_resume_data(NUM_RESUMES)
generate_area_data(NUM_AREAS)  # 85 регионов
generate_currency_data()
