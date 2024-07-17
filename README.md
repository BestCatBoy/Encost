# Encost
task from the "Энкост" company

6:
initialize the file object:

    f = file('filename.txt', line_size)

get data from a file:

    f = file('filename.txt', line_size)

    all_data = f.get_data()                 # return all data
    line_1_data = f.get_data(a)             # return line number a
    lines_0_10_data = f.get_data(a, b)      # return all lines in the range from a to b

Add data to the end of the file:

    f = file('filename.txt', line_size)
    f.add_data(["1234567890", "0123456789"])

8:
initializing a database object:

    client_name = client('database')

add data:

    client_name.add_data('table_name', ["data", ])

get the reasons for the downtime of the equipment:

    client_name.get_reasons('endpoint_name')

get the formatting configuration:

    client_name.get_format_config(["data_from_table_1", ], ["data_from_table_2", ])

format the "id" values of a specific hardware recorded in "data", following the configuration:

    client.format_id(["data", ], format_config)

add the "group" group and put the "endpoints" hardware in it:

    client_name.add_group(["endpoint", ], "group")
