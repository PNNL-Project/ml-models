#mysql-connector-python
from datetime import datetime
from mysql.connector import errorcode
import mysql

def getDate (value):
    value = value.strip()
    return datetime.strptime(value, "%Y-%m-%d").date()

def getElements (line):
    date = getDate(line[0])
    label = line[1]
    frequency = int(line[2])
    return date, label, frequency

def readData (lines, metric):
    try:
        # Note: Make sure to enter credentials before use
        client = mysql.connector.connect(user='', password='',
                                        host='', database='')
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Incorrect user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
        return

    cursor = client.cursor()
    insertData = ("INSERT INTO " + metric + "_labeled_agg" +
                  "(`Date`, `Label`, `Frequency`) " +
                  "VALUES (%s, %s, %s)")

    for line in lines:
        valuesData = (getElements(line))
        try:
            cursor.execute(insertData, valuesData)
        except mysql.connector.Error as err:
            if err.errno == 1146: # table does not exits error
                print("create table?")
                # table = ("CREATE TABLE IF NOT EXISTS " + metric + "_labeled_agg " +
                #          "(`Date` Date, `Label` VARCHAR(50), `Frequency` INT," +
                #          "PRIMARY KEY (`Date`, `Label`))")
                # cursor.execute(table)
                # cursor.execute(insertData, valuesData)
            else:
                # all other errors, rollback, does not insert the data into the database
                # handle different errors differently?
                print(err)
                client.rollback()
                return

    cursor.close()
    client.commit()
    client.close()

# Driver / test code
lines = [['2021-03-19', 'Group 0', 1000],
         ['2021-03-19', 'Group 1', 500],
         ['2021-03-19', 'Group 2', 500]]
metric = 'zonetemp'

readData (lines, metric)
print("Done Inserting")
