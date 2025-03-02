import mysql.connector
conn=mysql.connector.connect(user='root',password='password',host='localhost',database='store')
myc=conn.cursor()
#details given by manager
o="y"
while(o=="y" or o=="Y"):
   m="""    ,,,,*shop bill management receipt*,,,, 
           ,,,,*tax invoice*,,,, 
            ,,,,*AR Mart*,,,, 
  ,,,,*shop no. 4 laxmi colony*,,,, 
        ,,,,*laxmi Nagar 110092*,,,,
    ,,,,*mobile number-8421468850*,,,,"""   
   print(m)
   c=str(input("enter your choice(S\C\E\G\X):"))
   #press S for generating stationary bill
   #press C for generating clothing bill
   #press E for generating electrical appliances bill
   #press G for generating grocery bill
   #press X to exit from program
   if(c=="S" or c=="s"):
      print("STATIONARY BILL")
      date=input("invoice date:")
      impt=int(input("no. of item purchase:"))
      print("details of customer")
      customer=str(input("customer's name:Mr./Miss:"))
      address=str(input("customer's adress:"))
      city=str(input("customer's city:"))
      state=str(input("customer's state:"))
      mobilenumber=int(input("customer's mobile number:"))
      total=0
      maxitem=41 # maximum  number of items can be purchased at a time 
      if(impt<=maxitem):
         for a in range(1,impt+1):
            print("serial no:",a)
            i=str(input("item:"))
            rate=float(input("price of item in rupees:"))
            qty=int(input("quantity of item purchased:"))
            value=qty*rate # total  price of product with no. of quantity 
            print("Total price:",value)  # total  amount of particular product
            total=total+value # total  amount of all products
            sql="insert into item (serial_no,item_name,price,quantity) values({},'{}',{},{})".format(a,i,rate,qty)
            myc.execute(sql)
            conn.commit()
         print("Items Purchased Till Now:")
         myc.execute('select * from item')
         data=myc.fetchall()
         for row in data:
            print(row)
         print("Total Amount:",total)
         gst=28/100
         gtax=total*gst #gst taxed amount
         price=total+gtax # total amount of all products after adding gst 
         if(total<100):
            print("Final price:",price)
         elif(total>=100 and total<=800):
            discount=5/100
            dprice=total*discount # discount amount
            print("Final price:",price-dprice)
         elif(total>800 and total<=5000):
            discount=15/100
            dprice=total*discount
            print("Final price:",price-dprice)
         elif(total>5000 and total<=14000):
            discount=20/100
            dprice=total*discount
            print("Final price:",price-dprice)
         elif(total>14000):
            discount=25/100
            dprice=total*discount
            print("Final price:",price-dprice)
      else:
         print(" Sorry You Can Only Buy 41 Items At A Time")
      print("STATIONARY BILL")
   elif(c=="C" or c=="c"):
      print("CLOTHING BILL")
      date=input("invoice date:")
      impt=int(input("no. of item purchase:"))
      print("details of customer")
      customer=str(input("customer's name:Mr./Miss:"))
      adress=str(input("customer's adress:"))
      city=str(input("customer's city:"))
      state=str(input("customer's state:"))
      mobilenumber=int(input("customer's mobile number:"))
      total=0 
      maxitem=41 # maximum  number of items can be purchased at a time 
      if(impt<=maxitem):
         for a in range(1,impt+1):
            print("serial no:",a)
            i=str(input("item:"))
            rate=float(input("price of item in rupees:"))
            qty=int(input("quantity of item purchased:"))
            value=qty*rate # total  price of product with no. of quantity 
            print("Total price:",value)  # total  amount of particular product
            total=total+value # total  amount of all products
            sql="insert into item (serial_no,item_name,price,quantity) values({},'{}',{},{})".format(a,i,rate,qty)
            myc.execute(sql)
            conn.commit()
         print("Items Purchased Till Now:")
         myc.execute('select * from item')
         data=myc.fetchall()
         for row in data:
            print(row)
         print("Total Amount:",total)
         gst=8/100
         gtax=total*gst #gst taxed amount
         price=total+gtax # total amount of all products after adding gst 
         if(total<800):
            print("Final price:",price)
         elif(total>=800 and total<=6000):
            discount=5/100
            dprice=total*discount # discount amount
            print("Final price:",price-dprice)
         elif(total>6000 and total<=11000):
            discount=15/100
            dprice=total*discount
            print("Final price:",price-dprice)
         elif(total>11000 and total<=15000):
            discount=20/100
            dprice=total*discount
            print("Final price:",price-dprice)
         elif(total>15000):
            discount=25/100
            dprice=total*discount
            print("Final price:",price-dprice)
      else:
         print(" Sorry You Can Only Buy 41 Items At A Time")
      print("CLOTHING BILL")
   elif(c=="E" or c=="e"):
      print("ELECTRICAL APPLIANCES BILL")
      date=input("invoice date:")
      impt=int(input("no. of item purchase:"))
      print("details of customer")
      customer=str(input("customer's name:Mr./Miss:"))
      address=str(input("customer's adress:"))
      city=str(input("customer's city:"))
      state=str(input("customer's state:"))
      mobilenumber=int(input("customer's mobile number:"))
      total=0 
      maxitem=41 # maximum  number of items can be purchased at a time 
      if(impt<=maxitem):
         for a in range(1,impt+1):
            print("serial no:",a)
            i=str(input("item:"))
            rate=float(input("price of item in rupees:"))
            qty=int(input("quantity of item purchased:"))
            value=qty*rate # total  price of product with no. of quantity 
            print("Total price:",value)  # total  amount of particular product
            total=total+value # total  amount of all products
            sql="insert into item (serial_no,item_name,price,quantity) values({},'{}',{},{})".format(a,i,rate,qty)
            myc.execute(sql)
            conn.commit()
         print("Items Purchased Till Now:")
         myc.execute('select * from item')
         data=myc.fetchall()
         for row in data:
            print(row)
         print("Total Amount:",total)
         gst=18/100
         gtax=total*gst #gst taxed amount
         price=total+gtax # total amount of all products after adding gst 
         if(total<1200):
            print("Final price:",price)
         elif(total>=1200 and total<=4000):
            discount=5/100
            dprice=total*discount # discount amount
            print("Final price:",price-dprice)
         elif(total>4000 and total<=7000):
            discount=15/100
            dprice=total*discount
            print("Final price:",price-dprice)
         elif(total>7000 and total<=12000):
            discount=20/100
            dprice=total*discount
            print("Final price:",price-dprice)
         elif(total>12000):
            discount=25/100
            dprice=total*discount
            print("Final price:",price-dprice)
      else:
         print(" Sorry You Can Only Buy 41 Items At A Time")
      print("ELECTRICAL APPLINCES BILL")
   elif(c=="G" or c=="g"):
      print("GROCERY BILL")
      date=input("invoice date:")
      impt=int(input("no. of item purchase:"))
      print("details of customer")
      customer=str(input("customer's name:Mr./Miss:"))
      address=str(input("customer's adress:"))
      city=str(input("customer's city:"))
      state=str(input("customer's state:"))
      mobilenumber=int(input("customer's mobile number:"))
      total=0 
      maxitem=41 # maximum  number of items can be purchased at a time 
      if(impt<=maxitem):
         for a in range(1,impt+1):
            print("serial no:",a)
            i=str(input("item:"))
            rate=float(input("price of item in rupees:"))
            qty=int(input("quantity of item purchased:"))
            value=qty*rate # total  price of product with no. of quantity 
            print("Total price:",value)  # total  amount of particular product
            total=total+value # total  amount of all products
            sql="insert into item (serial_no,item_name,price,quantity) values({},'{}',{},{})".format(a,i,rate,qty)
            myc.execute(sql)
            conn.commit()
         print("Items Purchased Till Now:")
         myc.execute('select * from item')
         data=myc.fetchall()
         for row in data:
            print(row)
         print("Total Amount:",total)
         gst=4/100
         gtax=total*gst #gst taxed amount
         price=total+gtax # total amount of all products after adding gst 
         if(total<200):
            print("Final price",price)
         elif(total>=200 and total<=500):
            discount=5/100
            dprice=total*discount # discount amount
            print("Final price:",price-dprice)
         elif(total>500 and total<=900):
            discount=15/100
            dprice=total*discount
            print("Final price:",price-dprice)
         elif(total>900 and total<=15000):
            discount=20/100
            dprice=total*discount
            print("Final price:",price-dprice)
         elif(total>15000):
            discount=25/100
            dprice=total*discount
            print("Final price:",price-dprice)#final price is calculated after adding gst
      else:
         print(" Sorry You Can Only Buy 41 Items At A Time")
      print("GROCERY BILL")
   elif(c=="x" or c=="X"):
      exit()
   else:
      print("PLEASE ENTER A VALID PRODUCT CATEGORY")
      print("  S for generating stationary bill")
      print("  C for generating clothing bill")
      print("  E for generating electrical appliances bill")
      print("  G for generating grocery bill")
   t="""     ,,,,,,,THANK YOU,,,,,,,
        ,,,,VISIT US AGAIN,,,,
         ,ARMart@modernworld.in,"""
   print(t)
   o=input("want to run again y/n or Y/N")
