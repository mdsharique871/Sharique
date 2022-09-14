
def insert(xid,xname):
  import sqlite3
  con = sqlite3.connect('Attendance.db')
  cur = con.cursor()
  xid = input("Enter Employee id =  ")
  xname = input("Enter Employee name = ")
  cur.execute("""INSERT INTO Attendance (Empid, EmpName) VALUES(?,?)""", (xid, xname,))
  con.commit()
  con.close()

def update(xid,xdate,xent):
 import sqlite3
 con = sqlite3.connect('Attendance.db')
 cur = con.cursor()
 xid = input("Enter Employee id =  ")
 xdate = input("Enter today's Date (dd/mm/yy) format = ")
 xent = input ("Enter Entrry Time in office (24 hours) format = ")
 data = cur.execute('''UPDATE Attendance SET Date = ?, EntryTime = ?'''   '''where Empid = ?''', (xdate,xent, xid, ))
 con.commit()
 con.close()

def update2(xid,xdept,xhour):
 import sqlite3
 con = sqlite3.connect('Attendance.db')
 cur = con.cursor()
 xid = input("Enter Employee id which u want update =  ")
 xdept = input("Enter Departure Time from office (24 hours) format = ")
 xhour = input("Enter ypour working hours in  = ")
 data = cur.execute('''UPDATE Attendance SET DepartureTime = ?, Hours = ?'''  '''where Empid = ?''', (xdept, xhour, xid, ))
 con.commit()
 con.close()

def fetch():

  import sqlite3
  con = sqlite3.connect('Attendance.db')
  cur = con.cursor()
  data = cur.execute('''select * from Attendance''')
  for row in data:
   xid = row[0]
   xname = row[1]
   xdate = row[2]
   xent = row[3]
   xdept = row[4]
   xhour = row[5]
   print(str(xid) + " , " + str(xname) + " , " + str(xdate) + " , " + str(xent) + " , " + str(xdept) + " , " + str(xhour))
  con.close()

choice = 9
while (choice != 0):
 print("Enter 1 for Insert")
 print("Enter 2 for Update Date and arrival time ")
 print("Enter 3 for Update Departure time and working hours ")
 print("Enter 4 for Fetch all detail ")
 print("")
 print("Enter 0 to exit")
 print("")
 choice = int(input("Enter Your Choice = "))
 if choice == 1:
    print(insert('xid', 'xname'))
 elif choice == 2:
    print(update('xid', 'xdept', 'xhour'))

 elif choice == 3:
    print(update2('xid', 'xdept', 'xhour'))

 elif choice == 4:
    print(fetch())





choice = 9
while (choice != 0):
 print("Enter 1 for Insert")
 print("Enter 2 for Update Date and arrival time ")
 print("Enter 3 for Update Departure time and working hours ")
 print("Enter 4 for Fetch all detail ")
 print("")
 print("Enter 0 to exit")
 print("")
 choice = int(input("Enter Your Choice = "))
 if choice == 1:
    print(insert('xid', 'xname'))
 elif choice == 2:
    print(update('xid', 'xdept', 'xhour'))

 elif choice == 3:
    print(update2('xid', 'xdept', 'xhour'))

 elif choice == 4:
    print(fetch())
