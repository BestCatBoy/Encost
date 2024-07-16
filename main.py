from core import file

def main():
    client = file('file.txt', 10)
    #client.add_data(["1234567890"])
    print(client.get_data(0, 2))

if __name__ == '__main__':
    main()
