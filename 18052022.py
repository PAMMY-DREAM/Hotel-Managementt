from contextvars import Context
from decimal import ConversionSyntax
import random
import datetime
import sqlite3 as sql
from sqlite3 import Error
import os

name = []
phno = []
checkin = []
checkout = []
address = []
email = []
room = []
price = []
rc = []
p = []
roomno = []
custid = []
day = []

i = 0
db=sql.connect(r"C:\Users\TEMP.LAPTOP-49RFGT85.004\OneDrive\เดสก์ท็อป\PYTHON\project2\tel.db")
idr = None
roomsingle = []
roomtwin = []
roomtripple = []
roomsuit = []

stock = sql.connect(r"C:\Users\TEMP.LAPTOP-49RFGT85.004\OneDrive\เดสก์ท็อป\PYTHON\project2\stockdp.db")
for j in stock.execute("select * from single"):
    roomsingle.append([j[2],j[3]])

for j in stock.execute("select * from twin"):
    roomtwin.append([j[2],j[3]])

for j in stock.execute("select * from tripple"):
    roomtripple.append([j[2],j[3]])

for j in stock.execute("select * from suit"):
    roomsuit.append([j[2],j[3]])


def create_connection():
    conn = None
    try:
        conn = sql.connect("tel.db")
        query = conn.cursor()
        query.execute('''
            CREATE TABLE IF NOT EXISTS mphotel (
                [id] INTEGER PRIMARY KEY, 
                [name_lastname] TEXT,
                [phone] TEXT, 
                [check_in] TEXT, 
                [check_out] TEXT, 
                [room_type] TEXT, 
                [price] REAL
            )
        ''')

    except Error as e:
        print(e)
    return conn

def ddate(c):
    if 2022 <= c[2] <= 2030:  # กำหนดค่าให้เช็ค ปีที่เช็คอิน
        if c[1] != 0 and c[1] <= 12:  # 12เดือน
            if c[1] == 2 and c[0] != 0 and c[0] <= 31:
                if c[2] % 4 == 0 and c[0] <= 29:
                    pass
                elif c[0] < 29:
                    pass
                else:
                    print("Invalid date\n")
                    name.pop(i)
                    phno.pop(i)
                    checkin.pop(i)
                    checkout.pop(i)
                    Room()
            elif c[1] <= 7 and c[1] % 2 != 0 and c[0] <= 31:
                pass
            elif c[1] <= 7 and c[1] % 2 == 0 and c[0] <= 30 and c[1] != 2:
                pass
            elif c[1] >= 8 and c[1] % 2 == 0 and c[0] <= 31:
                pass
            elif c[1] >= 8 and c[1] % 2 != 0 and c[0] <= 30:
                pass

            else:
                print("Invalid date\n")
                name.pop(i)
                phno.pop(i)
                checkin.pop(i)
                checkout.pop(i)
                Room()
        else:
            print("Invalid date\n")
            name.pop(i)
            phno.pop(i)
            checkin.pop(i)
            checkout.pop(i)
            Room()
    else:
        print("Invalid date\n")
        name.pop(i)
        phno.pop(i)
        checkin.pop(i)
        checkout.pop(i)
        Room()

def Home():
    os.system("cls")
    print("-" * 120)
    print("\t\t\t\t 🏢🏢WELCOME TO PM HOTEL🏢🏢 ")
    print("-" * 120)
    print("\t\t\t 1 Booking\n")
    print("\t\t\t 2 Payment\n")
    print("\t\t\t 3 Record\n")
    print("\t\t\t 0 Exit\n")

    ch = int(input("👉👉 "))
    if ch == 1:
        os.system("cls")
        print(" ")
        Room()
    elif ch == 2:
        os.system("cls")
        print(" ")
        Payment()
    elif ch == 3:
        os.system("cls")
        print(" ")
        Record()
    elif ch == 0:
        os.system("cls")
        exit()

def Room():
    os.system("cls")
    global i

    print("***โปรดป้อนข้อมูลก่อนจองห้อง***")
    print(" ")

    n = str(input("Name and lastname: "))
    while n.isnumeric() or n == "":
        print("กรุณากรอกชื่อใหม่")
        n = str(input("Name and lastname: "))
    name.append(n)

    p1 = str(input("Phone No.: "))
    while not p1.isnumeric() or p1 == "" or len(p1) != 10:
        print("กรุณาเบอร์โทรใหม่")
        p1 = str(input("Phone No.: "))
    phno.append(p1)

    get_addr = str(input("Address: "))
    while get_addr == "":
        print("กรุณากรอกที่อยู่")
        get_addr = str(input("Address: "))
    address.append(get_addr)

    get_email = str(input("Email: "))
    while get_email == "" or len(get_email.split('@')) < 2 or len(get_email.split('.com')) < 2:
        print("กรุณากรอก Email ให้ถูกต้อง")
        get_email = str(input("Email: "))
    email.append(get_email)

    cii = str(input("Check-In: "))
    checkin.append(cii)
    cii = cii.split('/')
    ci = cii
    ci[0] = int(ci[0])
    ci[1] = int(ci[1])
    ci[2] = int(ci[2])
    ddate(ci)

    coo = str(input("Check-Out: "))
    checkout.append(coo)
    coo = coo.split('/')
    co = coo
    co[0] = int(co[0])
    co[1] = int(co[1])
    co[2] = int(co[2])
    ddate(co)

    if co[1] < ci[1] and co[2] < ci[2]:
        print("\n\tว้าาาาาา\n\t❌การเช็คอินไม่ถูกต้อง\n")
        name.pop(i)
        phno.pop(i)
        checkin.pop(i)
        checkout.pop(i)
        Room()

    ddate(co)
    d1 = datetime.datetime(ci[2], ci[1], ci[0])
    d2 = datetime.datetime(co[2], co[1], co[0])
    d = (d2 - d1).days
    day.append(d)


    print("\n----SELECT ROOM TYPE----")
    print(" 1. single bed room 900 bath")
    print(" 2. twin bed room 1,000 bath")
    print(" 3. tripple bed room 1,500 bath")
    print(" 4. room suit 1,700 bath")

    ch = int(input("👉👉 "))
    os.system("cls")
    if ch == 1:
        room.append('single')
        print("Room Type- single bed room")
        for j in range(len(roomsingle)):
            print(j+1,"\t",roomsingle[j][0],"\t",roomsingle[j][1])
        idroom = int(input("\nPlease select your idroom :"))
        roomsingle[idroom-1][1] = "unavalible"
        idr = roomsingle[idroom-1][0]
        os.system("cls")
        for j in range(len(roomsingle)):
            print(j+1,"\t",roomsingle[j][0],"\t",roomsingle[j][1])
        price.append(900)
        print("Price- 900")
    elif ch == 2:
        room.append('twin')
        print("Room Type- twin bed room")
        for j in range(len(roomtwin)):
            print(j+1,"\t",roomtwin[j][0],"\t",roomtwin[j][1])
        idroom = int(input("\nPlease select your idroom :"))
        roomtwin[idroom-1][1] = "unavalible"
        idr = roomtwin[idroom-1][0]
        os.system("cls")
        for j in range(len(roomtwin)):
            print(j+1,"\t",roomtwin[j][0],"\t",roomtwin[j][1])
        price.append(1000)
        print("Price- 1000")
    elif ch == 3:
        room.append('tripple')
        print("Room Type- tripple bed room")
        for j in range(len(roomtripple)):
            print(j+1,"\t",roomtripple[j][0],"\t",roomtripple[j][1])
        idroom = int(input("\nPlease select your idroom :"))
        roomtripple[idroom-1][1] = "unavalible"
        idr = roomtripple[idroom-1][0]
        os.system("cls")
        for j in range(len(roomtripple)):
            print(j+1,"\t",roomtripple[j][0],"\t",roomtripple[j][1])
        price.append(1500)
        print("Price- 1500")
    elif ch == 4:
        room.append('suit')
        print("Room Type- room suit")
        for j in range(len(roomsuit)):
            print(j+1,"\t",roomsuit[j][0],"\t",roomsuit[j][1])
        idroom = int(input("\nPlease select your idroom :"))
        roomsuit[idroom-1][1] = "unavalible"
        idr = roomsuit[idroom-1][0]
        os.system("cls")
        for j in range(len(roomsuit)):
            print(j+1,"\t",roomsuit[j][0],"\t",roomsuit[j][1])
        price.append(1700)
        print("Price- 1700")
    else:
        print("ไม่มีห้องนี้ โปรดเลือก 1 2 3 4 จ้า")

    rc.append(0)
    p.append(0)

    if p1 not in phno:
        phno.append(p1)
    elif p1 in phno:
        for n in range(0, i):
            if p1 == phno[n]:
                if p[n] == 1:
                    phno.append(p1)
    elif p1 in phno:
        for n in range(0, i):
            if p1 == phno[n]:
                if p[n] == 0:
                    print("\tข้อมูลไม่ถูกต้อง")
                    name.pop(i)
                    checkin.pop(i)
                    checkout.pop(i)
                    Room()
    print("")
    print("\t***จองห้องเรียบร้อยแล้วจ้า***\n")

    conn = create_connection()  # เชื่อม SQL

    cur = conn.cursor()  # ชี้ SQL
    list_to_database = [str(name[i]), str(phno[i]), str(checkin[i]), str(checkout[i]), str(room[i]), str(price[i]),str(email[i]),str(address[i])]
    # เอา List มาเรียงกัน
    try:  # เพิ่มข้อมูล
        db.execute(
            f"insert into mphotel(name_lastname, phone, check_in, check_out, room_type, price,roomid,email,address) VALUES(?, ?, ?, ?, ?, ?,'{idr}',?,?)",
            list_to_database)
        db.commit()
    except Error as e:  # เผื่อ Error
        print(e)

    conn.close()  # ปิดการเชื่อมต่อ

    i = i + 1
    n = int(input("0-BACK\n 👉👉 "))
    if n == 0:
        Home()
    else:
        exit()

def Payment():
    ph = str(input("กรอกหมายเลขโทรศัพทร์ที่ลงทะเบียน : "))
    global i
    f = 0

    for n in range(0, i):
        if ph == phno[n]:
            if p[n] == 0:
                f = 1
                print(" --------------------------------")
                print("Payment")
                print(" --------------------------------")
                print(" MODE OF PAYMENT")

                print(" 1- จ่ายเงิน")
                x = int(input("👉👉 "))
                print("\n ที่ต้องชำระ : ", (price[n] * day[n]))
                print("\n พร้อมเพย์  0️⃣  6️⃣  1️⃣  2️⃣  7️⃣  0️⃣  3️⃣  0️⃣  7️⃣  1️⃣ ")
                print(" (y/n)")
                ch = str(input("👉👉 "))

                if ch == 'y' or ch == 'Y':
                    print("\n\n --------------------------------")
                    print("\t   PM Hotel")
                    print(" --------------------------------")
                    print("\t    Bill")
                    print(" --------------------------------")
                    print(" Name: ", name[n], "\t\n Phone No.: ", phno[n], "\t\n Address:",address[n],"\t\n Email:",email[n])
                    print("\n Check-In: ", checkin[n], "\t\n Check-Out: ", checkout[n], "\t")
                    print("\n Room Type: ", room[n], "\t\n Room Charges: ", price[n] * day[n], "\t")
                    print(" --------------------------------")
                    print("\n Total : ", (price[n] * day[n]) , "\t")
                    print(" --------------------------------")
                    print("\t Thank You")
                    print("\t Visit Again ")
                    print(" --------------------------------\n")
                    p.pop(n)
                    p.insert(n, 1)
                    custid.insert(n, 0)
    n = int(input("0-BACK\n 👉👉 "))
    if n == 0:
        Home()
    else:
        exit()

def Record():
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM mphotel")

    rows = cur.fetchall()

    cur.close()

    if (len(rows) > 0):
        print("*** รายการจองห้องพัก ***\n")
        print("| Name-lastname	  Phone       Check-In   Check-Out	  Room-Type	       Price	 ID room|")
        print(
            "----------------------------------------------------------------------------------------------------------------------")

        for k in db.execute("select * from mphotel"):
            print(k[1],"\t",k[2],"\t",k[3],"\t",k[4],"\t",k[5],"\t",k[6],"\t",k[7])

        print(
            "----------------------------------------------------------------------------------------------------------------------")
    else:
        print("No Records Found")

    n = int(input("0-BACK\n 👉👉 "))
    if n == 0:
        Home()
    else:
        exit()


def start():
    while True:
        try:
            conn = sql.connect("tel.db")
            Home()
        except Error as e:
            print(e)
            break

create_connection()
start()
