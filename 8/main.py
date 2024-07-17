from core import client

def main():

    ## config
    database_name = 'client.sqlite'

    endpoints_table = 'endpoints'
    endpoint_reasons_table = 'endpoint_reasons'

    active = 'true'

    old_endpoints = ["Фрезерный станок", "Старый ЧПУ", "Сварка"]
    new_endpoints = ["Сварочный аппарат №1", "Пильный аппарат №2", "Фрезер №3"]
    old_endpoints_for_adding = ["Пильный станок", "Старый ЧПУ"]

    new_group = "Цех №2"

    ## working with database
    name = client(database_name)

    for endpoint in new_endpoints:
        name.add_data(endpoints_table, [endpoint] + [active])

    old_endpoints_reasons = list(map(name.get_reasons, old_endpoints))
    format_config = name.get_format_config(old_endpoints, new_endpoints)
    new_endpoints_reasons = [
        client.format_id(endpoint, format_config)
        for endpoint in old_endpoints_reasons
    ]

    for new_endpoints_reason in new_endpoints_reasons:
        for endpoint in new_endpoints_reason:
            name.add_data(endpoint_reasons_table, endpoint)

    name.add_group(new_endpoints, new_group)
    name.add_group(old_endpoints_for_adding, new_group)

if __name__ == '__main__':
    main()