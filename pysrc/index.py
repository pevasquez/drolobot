#!/usr/bin/python

# Turn on debug mode.
import cgitb
cgitb.enable()


# Connect to the database.
import pymysql
conn = pymysql.connect(
    db='example',
    user='root',
    passwd='not_posting_it_here',
    host='localhost')
c = conn.cursor()

# Insert some example data.
c.execute("INSERT INTO numbers VALUES (1, 'One!')")
c.execute("INSERT INTO numbers VALUES (2, 'Two!')")
c.execute("INSERT INTO numbers VALUES (3, 'Three!')")
conn.commit()

# Print the contents of the database.
c.execute("SELECT * FROM numbers")

# Print necessary headers.
print("Content-Type: text/html\r\n")
print([(r[0], r[1]) for r in c.fetchall()])

