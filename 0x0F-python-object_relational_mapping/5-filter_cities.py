#!/usr/bin/python3
'''
akes in the name of a state as an argument and lists all
cities of that state, using the database hbtn_0e_4_usa
'''


if __name__ == "__main__":
    from sys import argv
    import MySQLdb
    db = MySQLdb.connect(user=argv[1],
                         passwd=argv[2],
                         db=argv[3])
    cr = db.cursor()
    cr.execute("SELECT cities.name FROM cities\
                INNER JOIN states ON cities.state_id = states.id\
                WHERE states.name = %s\
                ORDER BY cities.id", (argv[4], ))
    cities = cr.fetchall()
    first = 0
    for city in cities:
        if first != 0:
            print(", ", end="")
        print("%s" % city, end="")
        first += 1
    print("")
    cr.close()
    db.close()
