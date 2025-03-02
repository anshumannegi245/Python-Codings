import os
import platform
import mysql.connector
import pandas as pd
import datetime

mydb = mysql.connector.connect(user='root', password='password',
                                host='localhost',
                                database='air')
mycursor = mydb.cursor()

def registercust():
    L = []
    name = input("enter name:")
    L.append(name)
    addr = input("enter address:")
    L.append(addr)
    jr_date = input("enter date of journey:")
    L.append(jr_date)
    source = input("enter source:")
    L.append(source)
    destination = input("enter destination:")
    L.append(destination)
    cust = tuple(L)  # Important: Convert to tuple for SQL
    sql = "insert into pdata(custname,addr,jrdate,source,destination)values(%s,%s,%s,%s,%s)"
    try:
        mycursor.execute(sql, cust)
        mydb.commit()
        print("Customer registered successfully!")
    except mysql.connector.Error as err:
        print(f"Error registering customer: {err}")


def classtypeview():
    print("Do you want to see class type available : Enter 1 for yes :")
    ch = int(input("enter your choice:"))
    if ch == 1:
        sql = "select * from classtype"
        mycursor.execute(sql)
        rows = mycursor.fetchall()
        for x in rows:
            print(x)


def ticketprice():
    print("We have the following rooms for you:-")
    print("1.  type First class---->rs 6000 PN\\-")
    print("2.  type Business class---->rs 4000 PN\\-")
    print("3.  type Economy class---->rs 2000 PN\\-")
    x = int(input("Enter Your Choice Please->"))
    n = int(input("No of passenger:"))
    s = 0  # Initialize s!
    if x == 1:
        print("you have opted First class")
        s = 6000 * n
    elif x == 2:
        print("you have opted Business class")
        s = 4000 * n
    elif x == 3:
        print("you have opted Economy class")
        s = 2000 * n
    else:
        print("please choose a class type")
    print("your room rent is =", s, "\n")
    return s  # Return the price


def menuview():
    print("Do you want to see menu available : Enter 1 for yes :")
    ch = int(input("enter your choice:"))
    if ch == 1:
        sql = "select * from food"
        mycursor.execute(sql)
        rows = mycursor.fetchall()
        for x in rows:
            print(x)


def orderitem():
    global food_bill  # Make food_bill global
    food_bill = 0  # Initialize food_bill
    print("Do you want to see menu available : Enter 1 for yes :")
    ch = int(input("enter your choice:"))
    if ch == 1:
        sql = "select * from food"
        mycursor.execute(sql)
        rows = mycursor.fetchall()
        for x in rows:
            print(x)

        print("do you want to purchase from above list:enter your choice:")
        d = int(input("enter your choice:"))
        if 1 <= d <= 10:  # Simplified conditional
            a = int(input("enter quantity"))
            prices = [10, 10, 20, 10, 50, 30, 10, 20, 50, 50] # Price list
            items = ["tea", "coffee", "colddrink", "samosa", "sandwich", "dhokla", "kachori", "milk", "noodles", "pasta"]
            food_bill = prices[d-1] * a
            print(f"You have ordered {items[d-1]}. Your amount is: {food_bill}\n")
        else:
            print("please enter your choice from the menu")
    return food_bill  # Return food bill


def lugagebill():
    global luggage_bill
    luggage_bill = 0
    print("Do you want to see rate for lugage : Enter 1 for yes :")
    ch = int(input("enter your choice:"))
    if ch == 1:
        sql = "select * from lugage"
        mycursor.execute(sql)
        rows = mycursor.fetchall()
        for x in rows:
            print(x)
        y = int(input("Enter Your weight of extra lugage->"))
        luggage_bill = y * 1000
        print("your lugage bill:", luggage_bill, "\n")
        return luggage_bill

def lb():
    print(luggage_bill)

def res():
    print(food_bill)

def ticketamount():
    a = input("enter customer name:")
    print("customer name :", a, "\n")
    room_rent = ticketprice()  # Get the room rent
    print("room rent:", room_rent, "\n")
    luggage_bill = lugagebill()
    print("lugage bill:", luggage_bill, "\n")
    food_bill = orderitem()
    print("food bill:", food_bill, "\n")
    total_amount = room_rent + luggage_bill + food_bill
    print("total amount:", total_amount, "\n")


def Menuset():
    print("AIR TICKET RESERVATION")
    print("enter 1: To enter customer data")
    print("enter 2 : To view class")
    print("enter 3 : for ticket price")  # Corrected
    print("enter 4 : for viewing food menu")
    print("enter 5 : for food bill")
    print("enter 6 : for lugage bill")
    print("enter 7 : for complete amount")
    print("enter 8 : for exit")

    try:
        userinput = int(input("enter your choice"))
        if userinput == 1:
            registercust()
        elif userinput == 2:
            classtypeview()
        elif userinput == 3:
            ticketprice()
        elif userinput == 4:
            menuview()
        elif userinput == 5:
            orderitem()
        elif userinput == 6:
            lugagebill()
        elif userinput == 7:
            ticketamount()
        elif userinput == 8:
            quit()
        else:
            print("enter correct choice")
        Menuset()  # Loop back to menu
    except ValueError:
        print("\nInvalid input. Please enter a number.")
        Menuset()


def runagain():
    while True: # Simplified loop
        runagn = input("\n want to run again y/n:")
        if runagn.lower() == 'y':
            if platform.system() == "Windows":
                os.system('cls')
            else:
                os.system('clear')
            Menuset()
        else:
            break # Exit the loop


Menuset()  # Start the program
runagain()
