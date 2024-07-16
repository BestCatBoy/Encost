# Encost
task from the "Энкост" company

initialize the file object:

    f = file('filename.txt', line_size)

get data from a file:

    f = file('filename.txt', line_size)

    all_data = f.get_data()                 # return all data
    line_1_data = f.get_data(a)             # return line number a
    lines_0_10_data = f.get_data(a, b)      # return all lines in the range from a to b

Add data to the end of the file:

    f = file('filename.txt', 10)
    f.add_data(["1234567890", "0123456789"])
