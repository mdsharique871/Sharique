
import sqlite3
con = sqlite3.connect('Attendance.db')
cur = con.cursor()

table = """CREATE TABLE Attendance(Empid int, Password VARCHAR(30),  EmpName VARCHAR(30), Date int, EntryTime, DepartureTime, Hours)"""

cur.execute(table)

con.commit()

con.close()