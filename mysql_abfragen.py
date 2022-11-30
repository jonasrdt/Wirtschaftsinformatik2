import mysql.connector as mysql
from mysql.connector import errorcode

DB_NAME = "beispieldatenbank"

TABLES = {}

TABLES['employees'] = (
    "CREATE TABLE `employees` ("
    "  `emp_no` int(11) NOT NULL AUTO_INCREMENT,"
    "  `birth_date` date NOT NULL,"
    "  `first_name` varchar(14) NOT NULL,"
    "  `last_name` varchar(16) NOT NULL,"
    "  `gender` enum('M','F', 'D') NOT NULL,"
    "  `hire_date` varchar(30) NOT NULL,"
    "  PRIMARY KEY (`emp_no`)"
    ") ENGINE=InnoDB")

def create_database(cursor):
    """
    It creates a database named `DB_NAME` if it doesn't already exist
    
    :param cursor: The cursor object that we created earlier
    """
    try:
        cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
    except mysql.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)

try:
    db = mysql.connect(user="root", password="root", host="localhost", port="8889", database = "uebungsdatenbank")
    cursor = db.cursor()
except mysql.Error as err:
    print("mehh:", err)


try:
    cursor.execute("USE {}".format(DB_NAME))
except mysql.Error as err:
    print("Database {} does not exists.".format(DB_NAME))
    if err.errno == errorcode.ER_BAD_DB_ERROR:
        create_database(cursor)
        print("Database {} created successfully.".format(DB_NAME))
        db.database = DB_NAME
    else:
        print(err)
        exit(1)


for table_name in TABLES:
    table_description = TABLES[table_name]
    try:
        print("Creating table {}: ".format(table_name), end='')
        cursor.execute(table_description)
    except mysql.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("already exists.")
        else:
            print(err.msg)
    else:
        print("OK")


add_employee = ("INSERT INTO employees "
               "(first_name, last_name, hire_date, gender, birth_date) "
               "VALUES (%s, %s, %s,)")

data_employee = ('Geert', 'Vanderkelen', 'M')
cursor.execute(add_employee, data_employee)

cursor.close()
db.close()