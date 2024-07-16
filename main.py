from core import file
from time_test import exetime

def main():
    file_name = 'file.txt'
    line_size = 10
    data = ["1234567890", ]

    print("file initialization")
    client = file(file_name, line_size)

    get_data = exetime(client.get_data)
    add_data = exetime(client.add_data)

    print("getting data")
    get_data()

    print("adding data")
    add_data(data)

if __name__ == '__main__':
    main()
