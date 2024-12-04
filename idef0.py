import sqlite3
from datetime import datetime


# Создание базы данных и таблиц
def create_tables():
    conn = sqlite3.connect('vet_clinic.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS clients (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            phone TEXT NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS pets (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            species TEXT NOT NULL,
            breed TEXT,
            age INTEGER,
            owner_id INTEGER,
            FOREIGN KEY(owner_id) REFERENCES clients(id)
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS appointments (
            id INTEGER PRIMARY KEY,
            pet_id INTEGER,
            date TEXT NOT NULL,
            reason TEXT NOT NULL,
            treatment TEXT,
            FOREIGN KEY(pet_id) REFERENCES pets(id)
        )
    ''')

    conn.commit()
    conn.close()


# Функция добавления нового клиента
def add_client(name, phone):
    conn = sqlite3.connect('vet_clinic.db')
    cursor = conn.cursor()

    cursor.execute('INSERT INTO clients (name, phone) VALUES (?, ?)', (name, phone))

    conn.commit()
    conn.close()


# Функция добавления нового питомца
def add_pet(name, species, breed, age, owner_id):
    conn = sqlite3.connect('vet_clinic.db')
    cursor = conn.cursor()

    cursor.execute('INSERT INTO pets (name, species, breed, age, owner_id) VALUES (?, ?, ?, ?, ?)',
                   (name, species, breed, age, owner_id))

    conn.commit()
    conn.close()


# Функция записи на прием
def add_appointment(pet_id, date, reason, treatment=None):
    conn = sqlite3.connect('vet_clinic.db')
    cursor = conn.cursor()

    cursor.execute('INSERT INTO appointments (pet_id, date, reason, treatment) VALUES (?, ?, ?, ?)',
                   (pet_id, date, reason, treatment))

    conn.commit()
    conn.close()


# Функция получения информации о клиентах
def get_clients():
    conn = sqlite3.connect('vet_clinic.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM clients')
    clients = cursor.fetchall()

    conn.close()
    return clients


# Функция получения информации о питомцах клиента
def get_pets_by_owner(owner_id):
    conn = sqlite3.connect('vet_clinic.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM pets WHERE owner_id = ?', (owner_id,))
    pets = cursor.fetchall()

    conn.close()
    return pets


# Функция получения записей на прием для питомца
def get_appointments_by_pet(pet_id):
    conn = sqlite3.connect('vet_clinic.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM appointments WHERE pet_id = ?', (pet_id,))
    appointments = cursor.fetchall()

    conn.close()
    return appointments


# Основной блок: создание таблиц и примеры добавления данных
if __name__ == '__main__':
    # Создание таблиц
    create_tables()

    # Примеры добавления данных
    add_client("Иван Иванов", "+79123456789")
    add_client("Анна Смирнова", "+79234567890")

    add_pet("Барсик", "Кот", "Сиамский", 3, 1)
    add_pet("Шарик", "Собака", "Лабрадор", 5, 2)

    add_appointment(1, str(datetime.now()), "Проверка здоровья", "Прописан витамины")
    add_appointment(2, str(datetime.now()), "Вакцинация")

    # Вывод данных
    print("Клиенты:", get_clients())
    print("Питомцы клиента 1:", get_pets_by_owner(1))
    print("Записи на прием для питомца 1:", get_appointments_by_pet(1))
