def fill_employers(table_name, data_to_fill):
    QUERY = fr"""INSERT INTO {table_name} (employer_id, employer_name, employer_url)
                        VALUES
                        ('{data_to_fill['id']}',
                         '{data_to_fill['name']}',
                         '{data_to_fill['alternate_url']}');"""
    return QUERY


def fill_vacancies(table_name, data_to_fill):
    QUERY = fr'''INSERT INTO {table_name} (vacancy_id, vacancy_name, vacancy_url, vacancy_salary_from, vacancy_salary_to, employer_id)
                        VALUES 
                        ('{data_to_fill['id']}',
                         '{data_to_fill['vacancy']}',
                         '{data_to_fill['url']}',
                         '{data_to_fill['salary_from']}',
                         '{data_to_fill['salary_to']}',
                         '{data_to_fill['employer_id']}');'''
    return QUERY


def fill_customers_data(table_name, data_to_fill):
    QUERY = fr'''INSERT INTO {table_name} (customer_id, company_name, contact_name)
                        VALUES 
                         ('{data_to_fill['customer_id']}',
                         '{data_to_fill['company_name']}',
                         '{data_to_fill['contact_name']}');'''
    return QUERY


def fill_employees_data(table_name, data_to_fill):
    QUERY = fr'''INSERT INTO {table_name} (first_name, last_name, title, birth_date, notes)
                        VALUES 
                        ('{data_to_fill['first_name']}',
                         '{data_to_fill['last_name']}',
                         '{data_to_fill['title']}',
                         '{data_to_fill['birth_date']}',
                         '{data_to_fill['notes']}');'''
    return QUERY


def fill_orders_data(table_name, data_to_fill):
    QUERY = fr'''INSERT INTO {table_name} (customer_id, employee_id, order_date, ship_city)
                        VALUES 
                        ('{data_to_fill['customer_id']}',
                         '{data_to_fill['employee_id']}',
                         '{data_to_fill['order_date']}',
                         '{data_to_fill['ship_city']}');'''
    return QUERY
