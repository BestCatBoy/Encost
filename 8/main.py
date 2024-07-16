import sqlite3

def get_last_id(table: str) -> int:
    """

    """

    with sqlite3.connect('client.sqlite') as db:
        cursor = db.cursor()

        sql = f"SELECT id FROM {table} ORDER BY id DESC LIMIT 1"
        cursor.execute(sql)
        last_id = cursor.fetchall()[0][0]

        return last_id

def add_data(table: str, data):
    """

    """

    column_count = {
        'endpoints':            3,
        'endpoint_reasons':     4,
        'endpoint_groups':      3
    }

    with sqlite3.connect('client.sqlite') as db:
        cursor = db.cursor()

        sql = f"INSERT INTO {table} VALUES({('?,'*column_count[table])[:-1]})"
        id = get_last_id(table) + 1

        cursor.execute(sql, [id] + data)

"""
2.1) получить три массива с причинами (3, 4 столбцы) по станкам:
    "Фрезерный станок", "Старый ЧПУ", "Сварка"
2.3) добавить эти причины по каждому новому соответствующему id станка

3.1) добавить "Цех №2" в endpoint_groups и поместить туда новые станки

4.1) добавить станки 4 и 5 к новой группе
"""

def main():
    data = [
        ["Сварочный аппарат №1",    "true"],
        ["Пильный аппарат №2",      "true"],
        ["Фрезер №3",               "true"]
    ]

    for line in data:
        add_data('endpoints', line)

if __name__ == '__main__':
    main()
