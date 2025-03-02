import os
import platform
import mysql.connector
import pandas as pd

mydb = mysql.connector.connect(host='localhost',
                             user='root',
                             passwd='root',
                             database='School')
mycursor = mydb.cursor()

def stuInsert():
    try:
        L = []
        roll = int(input("Enter the roll number: "))
        L.append(roll)
        name = input("Enter the Name: ")
        L.append(name)
        age = int(input("Enter Age of Student: "))
        L.append(age)
        classs = input("Enter the Class: ")
        L.append(classs)
        city = input("Enter the City of the Student: ")
        L.append(city)
        stud = tuple(L)  # Convert to tuple for SQL execution
        sql = "INSERT INTO student (roll, name, age, class, city) VALUES (%s, %s, %s, %s, %s)"
        mycursor.execute(sql, stud)
        mydb.commit()
        print("Student record inserted successfully.")
    except mysql.connector.Error as err:
        print(f"Error inserting student record: {err}")
        mydb.rollback() # Important: Rollback on error

def stuView():
    try:
        print("Select the search criteria:")
        print("1. Roll")
        print("2. Name")
        print("3. Age")
        print("4. City")
        print("5. All")
        ch = int(input("Enter the choice: "))
        sql = "SELECT * FROM student"  # Default query
        rl = None  # Initialize rl

        if ch == 1:
            s = int(input("Enter roll no: "))
            sql = "SELECT * FROM student WHERE roll = %s"
            rl = (s,)
        elif ch == 2:
            s = input("Enter Name: ")
            sql = "SELECT * FROM student WHERE name = %s"
            rl = (s,)
        elif ch == 3:
            s = int(input("Enter age: "))
            sql = "SELECT * FROM student WHERE age = %s"
            rl = (s,)
        elif ch == 4:
            s = input("Enter City: ")
            sql = "SELECT * FROM student WHERE city = %s"  # Corrected column name
            rl = (s,)
        elif ch != 5: #Handles cases where the input is not between 1-5
            print("Invalid Choice")
            return

        mycursor.execute(sql, rl) if rl else mycursor.execute(sql) #Conditional execution of parameters
        res = mycursor.fetchall()

        if res: #Checks if the result set is not empty before printing
            print("The Students details are as follows:")
            print("(Roll, Name, Age, Class, City)")
            for x in res:
                print(x)
        else:
            print("No matching records found.")

    except mysql.connector.Error as err:
        print(f"Error viewing student records: {err}")

def feeDeposit():
    try:
        L = []
        roll = int(input("Enter the roll number: "))
        L.append(roll)
        feedeposit = int(input("Enter the Fee to be deposited: "))
        L.append(feedeposit)
        month = input("Enter month of fee: ")
        L.append(month)
        fee = tuple(L)  # Convert to tuple
        sql = "INSERT INTO fee (roll, feeDeposit, month) VALUES (%s, %s, %s)" #Corrected column name
        mycursor.execute(sql, fee)
        mydb.commit()
        print("Fee deposited successfully.")
    except mysql.connector.Error as err:
        print(f"Error depositing fee: {err}")
        mydb.rollback()

def feeView():
    try:
        roll = int(input("Enter the roll number of the student whose fee is to be viewed: "))
        sql = """
            SELECT s.roll, s.name, s.class, SUM(f.feeDeposit), f.month
            FROM student s
            INNER JOIN fee f ON s.roll = f.roll
            WHERE f.roll = %s
            GROUP BY f.month;  -- Group by month to show fee details for each month
        """
        rl = (roll,)
        mycursor.execute(sql, rl)
        res = mycursor.fetchall()
        if res:
            print("Fee details:")
            print("(Roll, Name, Class, Total Fee, Month)")
            for x in res:
                print(x)
        else:
            print("No fee records found for this student.")
    except mysql.connector.Error as err:
        print(f"Error viewing fee details: {err}")

def removeStu():
    try:
        roll = int(input("Enter the roll number of the student to be deleted: "))
        rl = (roll,)

        # It's good practice to check if the student exists before deleting
        check_sql = "SELECT 1 FROM student WHERE roll = %s"
        mycursor.execute(check_sql, rl)
        if mycursor.fetchone():  # Student exists
            sql_fee = "DELETE FROM fee WHERE roll = %s"
            mycursor.execute(sql_fee, rl)

            sql_student = "DELETE FROM student WHERE roll = %s"
            mycursor.execute(sql_student, rl)

            mydb.commit()
            print("Student and related fee records deleted successfully.")
        else:
            print("Student with this roll number does not exist.")

    except mysql.connector.Error as err:
        print(f"Error removing student: {err}")
        mydb.rollback()

def MenuSet():
    while True: #Keeps the menu running until a valid choice is entered
        print("Enter 1 : To Add Student")
        print("Enter 2 : To View Student ")
        print("Enter 3 : To Deposit Fee ")
        print("Enter 4 : To Remove Student")
        print("Enter 5 : To View Fee of Any Student")
        print("Enter 6 : To Exit")

        try:
            userInput = int(input("Please Select An Option: "))
        except ValueError:
            print("\nInvalid input. Please enter a number.")
            continue #Go back to the beginning of the loop

        print("\n")

        if userInput == 1:
            stuInsert()
        elif userInput == 2:
            stuView()
        elif userInput == 3:
            feeDeposit()
        elif userInput == 4:
            removeStu()
        elif userInput == 5:
            feeView()
        elif userInput == 6:
            break #Exit the loop and the program
        else:
            print("Invalid choice. Please select a valid option.")

MenuSet()
