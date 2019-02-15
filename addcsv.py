import sqlite3
import csv

f=open('2.csv','r') # open the csv data file
#next(f, None) # skip the header row
reader = csv.reader(f, delimiter =';')

sql = sqlite3.connect('db.sqlite3')
cur = sql.cursor()

			 
for row in reader:
	cur.execute("INSERT INTO ooh_maindatabase VALUES (?, ?, ?,?,?,?,?,?,?,?,?,?,?,?,?,?)", row)
	
f.close()
sql.commit()
sql.close()