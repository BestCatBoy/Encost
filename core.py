from os import open, close, O_RDWR as read_and_write_mode, read, write
from os.path import getsize as get_size
from typing import Final as const

class file:

    __entity = None
    __file_size = 0
    __charset: const['str'] = 'utf-8'

    def __new__(cls, *args, **kwargs):
        """
        singleton pattern
        """

        if cls.__entity is None:
            cls.__entity = super().__new__(cls)

        return cls.__entity

    def __init__(self, file_name, line_size):
        """
        initialize the file object:

            f = file('filename.txt', line_size)
        """

        self.__verify_file(file_name)

        self.__file_size = get_size(file_name)
        self.__file_name = file_name
        self.__line_size = line_size

    def get_data(self, *args) -> str:
        """
        get data from a file:

            f = file('filename.txt', line_size)

            all_data = f.get_data()                 # return all data
            line_1_data = f.get_data(a)             # return line number a
            lines_0_10_data = f.get_data(a, b)      # return all lines in the range from a to b
        """

        interval = list(args)
        self.__verify_interval(interval)

        file = open(self.__file_name, read_and_write_mode)
        bytes_lines = str(read(file, self.__file_size))
        close(file)

        lines = bytes_lines[2:bytes_lines.index("\\")]
        offset = self.__line_size

        if not len(args):
            return lines

        return lines[args[0]*offset:args[len(args)-1]*offset+offset*(len(args)%2)]

    def add_data(self, data):
        """
        Add data to the end of the file:

            f = file('filename.txt', 10)
            f.add_data(["1234567890", "0123456789"])
        """

        self.__verify_data(data, self.__line_size)

        file = open(self.__file_name, read_and_write_mode)
        existing_bytes_data = self.get_data().encode(self.__charset)

        for line in data:
            write(file, existing_bytes_data + line.encode(self.__charset))

        close(file)

    @classmethod
    def __verify_file(cls, file_name):
        """
        verify the file for suitability for initialization
        """

        if not isinstance(file_name, str):
            raise TypeError(
                "file name must be represented by the str data type"
            )

        try:
            open(file_name, read_and_write_mode)
        except:
            raise FileNotFoundError(
                f"no such file or directory: {file_name}"
            )

    @classmethod
    def __verify_data(cls, data, line_size):
        """
        verify data for suitability for writing to file
        """

        if not hasattr(data, '__iter__'):
            raise TypeError(
                "data must be an iterable object"
            )

        if not len(data):
            raise ValueError("data cannot be empty")

        data_len_set = list(set([len(line) for line in data]))

        if len(data_len_set) != 1:
            raise ValueError(
                "line lengths must be the same"
            )

        if data_len_set[0] != line_size:
            raise ValueError(
                "line lengths must be equal to the \"line_size\" value"
            )

    @classmethod
    def __verify_interval(cls, interval):
        """
        verify interval for suitability for receiving data
        """

        if not hasattr(interval, '__iter__'):
            raise TypeError(
                "interval must be an iterable object"
            )

        if len(interval) > 2:
            raise SyntaxError(
                "number of points in the interval should not exceed 2"
            )

        if (len(interval) == 2) and (interval[0] > interval[1]):
            raise ValueError(
                "beginning of the interval should not be greater than its end"
            )