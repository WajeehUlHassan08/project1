import pypyodbc as odbc

DRIVER_NAME = 'SQL SERVER'
SERVER_NAME = 'DELL100\SQLEXPRESS'
DATABASE_NAME = 'challenge1'

connection_string = f"""
    DRIVER={{{DRIVER_NAME}}};
    SERVER={SERVER_NAME};
    DATABASE={DATABASE_NAME};
    Trust_Connection=yes;
"""

conn = odbc.connect(connection_string)
cursor = conn.cursor()

insert_data_query = '''
INSERT INTO sales (customer_id, order_date, product_id)
VALUES ("C","Jami","2021-01-07","1")
'''

cursor.execute(insert_data_query)
conn.commit()

query = 'SELECT * FROM sales'
cursor.execute(query)

print(cursor.fetchall())