import os
import pyodbc
from dotenv import load_dotenv
import SQL_Queries


class ConnectDB:
    @staticmethod
    def connect_to_db(server, database, user, password):
        ConnectionString = f'''DRIVER={{ODBC Driver 18 for SQL Server}};
                               SERVER={server};
                               DATABASE={database};
                               UID={user};
                               PWD={password};
                               ENCRYPT=Optional'''
        try:
            conn = pyodbc.connect(ConnectionString)
            conn.autocommit = True
        except pyodbc.ProgrammingError as ex:
            print(ex)
        else:
            return conn


class MSSQLOperator:

    def __init__(self, connector_obj):
        self.conn = connector_obj

    def create_database(self, database_name, size=None, maxsize=None, filegrowth=None):
        SQL_COMMAND = SQL_Queries.create_database(database_name, size, maxsize, filegrowth)
        try:
            self.conn.execute(SQL_COMMAND)
        except pyodbc.ProgrammingError as ex:
            print(ex)
        else:
            return f"База данных {database_name} успешно создана"

    def create_table(self, database_name, table_name, sql_query):
        cursor = self.conn.cursor()
        cursor.execute(f'USE {database_name}')
        SQL_Query = sql_query(table_name)
        try:
            cursor.execute(SQL_Query)
        except pyodbc.ProgrammingError as ex:
            return ex
        else:
            return f"Таблица: {table_name} успешно создана"

    def drop_table(self, database_name, table_name, sql_query):
        cursor = self.conn.cursor()
        cursor.execute(f'USE {database_name}')
        SQL_Query = sql_query(table_name)
        try:
            cursor.execute(SQL_Query)
        except pyodbc.Error as ex:
            return ex
        else:
            return f"Таблица: {table_name} успешно удалена!"


if __name__ == "__main__":
    load_dotenv()
    SERVER = os.getenv('MS_SQL_SERVER')
    DATABASE = os.getenv('MS_SQL_DATABASE')
    USER = os.getenv('MS_SQL_USER')
    PASSWORD = os.getenv('MS_SQL_KEY')
    new_db = "NorthWind"

    my_conn = ConnectDB.connect_to_db(SERVER, DATABASE, USER, PASSWORD)
    my_db_operator = MSSQLOperator(my_conn)
    print(my_db_operator.create_database(new_db, "10", "20", "5%"))
    print(my_db_operator.create_table(new_db, 'customers_data', SQL_Queries.create_customers_data))
    print(my_db_operator.create_table(new_db, 'employees_data', SQL_Queries.create_employees_data))
    print(my_db_operator.create_table(new_db, 'orders_data', SQL_Queries.create_orders_data))
