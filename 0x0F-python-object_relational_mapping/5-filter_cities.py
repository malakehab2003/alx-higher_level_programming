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

    query = "SELECT cities.name \
        FROM cities \
        INNER JOIN states \
        ON cities.state_id = states.id \
        WHERE states.name LIKE %s \
        ORDER BY cities.id".format(sys.argv[4])
    mycursor.execute(query, (sys.argv[4],))
    data = mycursor.fetchall()
    tmp = list(i[0] for i in data)
    for item in tmp:
        if item != tmp[len(tmp) - 1]:
            print(item, end=", ")
        else:
            print(item)
    mycursor.close()
    con.close()
