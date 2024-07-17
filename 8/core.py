import sqlite3

class client:

    __entity = None

    __column_count = {
        'endpoints':            3,
        'endpoint_reasons':     4,
        'endpoint_groups':      3
    }

    def __new__(cls, *args, **kwargs):

        """ singleton pattern """

        if cls.__entity is None:
            cls.__entity = super().__new__(cls)

        return cls.__entity

    def __init__(self, database: str):

        """ initializing a database object """

        self.__verify_database(database)
        self.__database = database

    def add_data(self, table: str, data: list):

        """ add the data "data" to the table "table" """

        self.__verify_data(data)

        with sqlite3.connect(self.__database) as db:
            cursor = db.cursor()

            sql = f'''
                INSERT INTO
                    {table}
                VALUES(
                    {('?,'*self.__column_count[table])[:-1]}
                )
            '''

            id = self.__get_last_id(table) + 1

            cursor.execute(sql, [id] + data)

    def add_group(self, endpoints: list, group: str):

        """ add the "group" group and put the "endpoints" hardware in it """

        self.__verify_data(endpoints)

        endpoints_id = list(map(self.__get_endpoint_id, endpoints))

        for id in endpoints_id:
            self.add_data('endpoint_groups', [id[0][0]] + [group])

    def get_reasons(self, endpoint_name: str) -> list:

        """ get the reasons for the downtime of the equipment
        with the name "endpoint_name" """

        data = None

        with sqlite3.connect(self.__database) as db:
            cursor = db.cursor()

            sql = f'''
                SELECT
                    endpoints.id,
                    reasons.reason_name,
                    reasons.reason_hierarchy
                FROM
                    endpoints,
                    endpoint_reasons AS reasons
                WHERE
                (
                    endpoints.name = "{endpoint_name}"
                )
                    AND reasons.endpoint_id = endpoints.id
            '''

            cursor.execute(sql)
            data = cursor.fetchall()

        return data

    def get_format_config(self, association: list, recipient: list) -> dict:

        """ get the formatting configuration """

        self.__verify_data(association)
        self.__verify_data(recipient)

        keys = list(map(self.__get_endpoint_id, association))
        values = list(map(self.__get_endpoint_id, recipient))

        format_config = {str(key[0][0]):value[0][0] for key, value in zip(keys, values)}

        return format_config

    @staticmethod
    def format_id(data: list, format_config: dict) -> list:

        """ format the "id" values of a specific hardware recorded in "data",
        following the configuration recorded in "format_config" """

        self.__verify_data(data)

        return [[format_config[str(line[0])]] + list(line[1:]) for line in data]

    def __get_endpoint_id(self, endpoint: str) -> int:

        """ get the "id" of the equipment """

        endpoint_id = None

        with sqlite3.connect(self.__database) as db:
            cursor = db.cursor()

            sql = f'''
                SELECT
                    id
                FROM
                    endpoints
                WHERE name = "{endpoint}"
            '''

            cursor.execute(sql)
            endpoint_id = cursor.fetchall()

        return endpoint_id

    def __get_last_id(self, table: str) -> int:

        """ get the value of the "id" column
        from the last row in the "table" table """

        last_id = None

        with sqlite3.connect(self.__database) as db:
            cursor = db.cursor()

            sql = f'''
                SELECT
                    id
                FROM
                    {table}
                ORDER BY
                    id
                DESC LIMIT 1
            '''

            cursor.execute(sql)
            last_id = cursor.fetchall()[0][0]

        return last_id

    @classmethod
    def __verify_database(database: str):

        """ check the database for suitability for initialization """

        try:
            sqlite3.connect(database)
        except:
            raise ConnectionError(
                f"unable to connect to the database \"{database}\""
            )

    @classmethod
    def __verify_data(data: str):

        """ check the data for belonging to the required data type (list) """

        if not isinstance(data, list):
            raise TypeError(
                "data must be represented by the list data type"
            )