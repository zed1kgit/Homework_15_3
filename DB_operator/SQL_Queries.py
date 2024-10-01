def create_database_default(name):
    COMMAND = fr"CREATE DATABASE {name};"
    return COMMAND


def create_database(name, size, maxsize, filegrowth):
    COMMAND = fr"""
CREATE DATABASE {name}
ON
(
NAME = {name}Database_data,
FILENAME = 'T:\Program Files\Microsoft SQL Server\MSSQL16.SQLEXPRESS\MSSQL\DATA\{name}Database_data.mdf',
SIZE = {size}MB,
MAXSIZE = {maxsize}GB,
FILEGROWTH={filegrowth}
)
LOG ON
(NAME = {name}Database_log,
FILENAME = 'T:\Program Files\Microsoft SQL Server\MSSQL16.SQLEXPRESS\MSSQL\DATA\{name}Database_data.ldf',
SIZE = {size}MB,
MAXSIZE = {str(round(int(maxsize) * 0.1))}GB,
FILEGROWTH = {filegrowth}
)"""
    return COMMAND


def create_employers(table_name):
    QUERY = fr"""CREATE TABLE {table_name}
            (employer_id int PRIMARY KEY,
            employer_name nvarchar(100),
            employer_url nvarchar(200));"""
    return QUERY


def create_vacancies(table_name):
    QUERY = fr"""CREATE TABLE {table_name}
            (vacancy_id int PRIMARY KEY,
            vacancy_name nvarchar(100),
            vacancy_url nvarchar(200),
            vacancy_salary_from int,
            vacancy_salary_to int,
            employer_id int
            REFERENCES employers(employer_id));"""
    return QUERY


def create_customers_data(table_name):
    QUERY = fr"""CREATE TABLE {table_name}
                (customer_id nvarchar(10) PRIMARY KEY,
                company_name nvarchar(100) NOT NULL,
                contact_name nvarchar(50) NOT NULL);"""
    return QUERY


def create_employees_data(table_name):
    QUERY = fr"""CREATE TABLE {table_name}
                (employee_id int IDENTITY(1, 1) PRIMARY KEY,
                first_name nvarchar(100) NOT NULL,
                last_name nvarchar(100) NOT NULL,
                title nvarchar(100) NOT NULL,
                birth_date date NOT NULL,
                notes nvarchar(1000) NOT NULL);"""
    return QUERY


def create_orders_data(table_name):
    QUERY = fr"""CREATE TABLE {table_name}
                (order_id int IDENTITY(1, 1) PRIMARY KEY,
                customer_id nvarchar(10) REFERENCES customers_data(customer_id) NOT NULL,
                employee_id int REFERENCES employees_data(employee_id) NOT NULL,
                order_date date NOT NULL,
                ship_city nvarchar(100) NOT NULL);"""
    return QUERY


def drop_table(table_name):
    QUERY = fr"DROP TABLE {table_name}"
    return QUERY
