import csv
from credentials import *
import mysql.connector

db = mysql.connector.connect(
    host= db_host,
    user=db_user,
    passwd=db_password,
    database="hindalco"
)

my_cursor = db.cursor()

# my_cursor.execute("""CREATE DATABASE hindalco""")


# my_cursor.execute("""
#     CREATE TABLE task_data (
#     id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
#     date DATETIME NOT NULL,
#     close DECIMAL(5,2) NOT NULL,
#     high DECIMAL(5,2) NOT NULL,
#     low DECIMAL(5,2) NOT NULL,
#     open DECIMAL(5,2) NOT NULL,
#     volume INT NOT NULL,
#     instrument VARCHAR(50) NOT NULL)""")


# with open('HINDALCO.csv', 'r+') as csvdata:
#     reader = csv.DictReader(csvdata)
#     counter = 0
#     for line in reader:
#         Date_time = line['datetime']
#         Close = line['close']
#         High = line['high']
#         Low = line['low']
#         Open = line['open']
#         Vol = line['volume']
#         Instrument = line['instrument']
#         counter += 1
#         # print(Date_time, Close, Open, High, Low, Vol, Instrument)

#         my_cursor.execute("""
#             INSERT INTO task_data (date, close, high, low, open, volume, instrument)
#             VALUES (%s, %s, %s, %s, %s, %s,%s)""",
#             (Date_time, Close, High, Low, Open, Vol, Instrument))

#     db.commit()
#     print(f"Added {counter} succefully !")

my_cursor.execute("""
    SELECT *
    FROM task_data 
    ORDER BY id""")

for x in my_cursor:
    print(x)