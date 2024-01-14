#!/usr/bin/python3
""" get cities of database"""
import MySQLdb
import sys


if __name__ == "__main__":
    con = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3])
    mycursor = con.cursor()

    query = "SELECT cities.id, cities.name \
        FROM cities \
        ORDER BY id"
    mycursor.execute(query)
    data = mycursor.fetchall()
    for row in data:
        print(row)
    mycursor.close()
    con.close()
