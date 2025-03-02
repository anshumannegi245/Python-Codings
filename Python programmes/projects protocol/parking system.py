import os
import platform
import mysql.connector
import datetime
now = datetime.datetime.now()

mydb = mysql.connector.connect(host="localhost", user="root", password="password", database='parking')
mycursor = mydb.cursor()

def Add_Record():
    L = []
    try:  # Handle potential errors during input
        id1 = int(input("Enter the parking number: "))
        L.append(id1)
        pname1 = input("Enter the Parking Name: ")
        L.append(pname1)
        level1 = input("Enter level of parking: ")
        L.append(level1)
        freespace1 = input("Is there any freespace or not: YES/NO ")
        L.append(freespace1)
        vehicleno1 = input("Enter the Vehicle Number: ")
        L.append(vehicleno1)
        nod1 = int(input("Enter total number of days for parking: "))
        L.append(nod1)

        if nod1 == 1:
            Payment1 = 20
        elif nod1 == 2:
            Payment1 = 40
        elif nod1 == 3:
            Payment1 = 60
        elif nod1 == 4:
            Payment1 = 80
        elif nod1 == 5:
            Payment1 = 100
        elif nod1 == 6:
            Payment1 = 120
        else:  # Handle cases where nod1 is outside the range
            print("Invalid number of days. Setting payment to 0.")
            Payment1 = 0

        L.append(Payment1)
        stud = tuple(L)  # Convert to tuple for database insertion

        sql = 'insert into parkmaster12(pid, pnm, level, freespace, vehicleno, nod, payment) values(%s,%s,%s,%s,%s,%s,%s)'
        mycursor.execute(sql, stud)
        mydb.commit()
        print("Record added successfully!")

    except ValueError:
        print("Invalid input. Please enter numbers for parking number and number of days.")
    except mysql.connector.Error as err:
        print(f"Database error: {err}")


def Rec_View():
    print("Select the search criteria:")
    print("1. Parking Number")
    print("2. Parking Name")
    print("3. Level No")
    print("4. All")

    try:
        ch = int(input("Enter the choice: "))

        if ch == 1:
            s = int(input("Enter Parking no: "))
            rl = (s,)
            sql = "select * from parkmaster12 where pid=%s"
        elif ch == 2:
            s = input("Enter Parking Name: ")
            rl = (s,)
            sql = "select * from parkmaster12 where pnm=%s"
        elif ch == 3:
            s = int(input("Enter Level of Parking: "))
            rl = (s,)
            sql = "select * from parkmaster12 where level=%s"
        elif ch == 4:
            sql = "select * from parkmaster12"
            mycursor.execute(sql)  # No parameters needed for select all
            res = mycursor.fetchall()
        else:
            print("Invalid choice.")
            return  # Exit the function if the choice is invalid

        if ch != 4:  # Execute only if not a select all query
            mycursor.execute(sql, rl)
            res = mycursor.fetchall()

        print("Details about Parking are as follows:")
        print("(Parking Id, ParkingName, Level, FreeSpace(Y/N), Vehicle No, No of days for parking, Payment)")
        for x in res:
            print(x)
        print('Task completed')

    except ValueError:
        print("Invalid input. Please enter a number for your choice and search criteria (where applicable).")
    except mysql.connector.Error as err:
        print(f"Database error: {err}")


def Vehicle_Detail():
    L = []
    try:
        vid1 = int(input("Enter Vehicle No: "))
        L.append(vid1)
        vnm1 = input("Enter Vehicle Name/Model Name: ")
        L.append(vnm1)
        dateofpur1 = input("Enter Year-Month-date of purchase (YYYY-MM-DD): ") #Correct date format
        L.append(dateofpur1)
        vdt = tuple(L)  # Convert to tuple

        sql = "insert into vehicle(pid, vnm, dateofpur) values(%s,%s,%s)"
        mycursor.execute(sql, vdt)
        mydb.commit()
        print("Vehicle details added successfully!")

    except ValueError:
        print("Invalid input. Please enter a valid vehicle number.")
    except mysql.connector.Error as err:
        print(f"Database error: {err}")



def Vehicle_View():
    try:
        vid1 = int(input("Enter the vehicle number of the vehicle whose details is to be viewed: "))
        sql = 'select parkmaster12.pid, parkmaster12.pnm, parkmaster12.vehicleno, vehicle.pid, vehicle.vnm from parkmaster12 INNER JOIN vehicle ON parkmaster12.pid=vehicle.pid and vehicle.vehicleno=%s'
        rl = (vid1,)
        print('The following are the details you wanted:')
        mycursor.execute(sql, rl)
        res = mycursor.fetchall()
        for x in res:
            print(x)
        print('Task completed')

    except ValueError:
        print("Invalid input. Please enter a valid vehicle number.")
    except mysql.connector.Error as err:
        print(f"Database error: {err}")

def remove():
    try:
        vid1 = int(input("Enter the vehicle number of the vehicle to be deleted: "))
        rl = (vid1,)
        sql = "Delete from vehicle where vehicleno=%s"  # Use vehicleno for deletion
        mycursor.execute(sql, rl)
        mydb.commit()
        print('Removed as per the command')

    except ValueError:
        print("Invalid input. Please enter a valid vehicle number.")
    except mysql.connector.Error as err:
        print(f"Database error: {err}")

def Menu():
    while True: #Loop to keep the menu running
        print("Enter 1 : To Add Parking Detail")
        print("Enter 2 : To View Parking Detail ")
        print("Enter 3 : To Add Vehicle Detail ")
        print("Enter 4 : To Remove Vehicle Record")
        print("Enter 5 : To see the details of Vehicle")
        print("Enter 6 : To Exit") #Option to exit the menu

        try:
            input_dt = int(input("Please Select An Above Option: "))

            if input_dt == 1:
                Add_Record()
            elif input_dt == 2:
                Rec_View()
            elif input_dt == 3:
                Vehicle_Detail()
            elif input_dt == 4:
                remove()
            elif input_dt == 5:
                Vehicle_View()
            elif input_dt == 6:
                break #Exit the loop and the program
            else:
                print("Enter correct choice....")
        except ValueError:
            print("Invalid input. Please enter a number.")



def runAgain(): #No longer needed as the menu is in a loop
   pass #Just pass, as the loop is handled in Menu()

Menu() #Start the menu
