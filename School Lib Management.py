#Library Management System
import mysql.connector as mysql
mydb=mysql.connect(host='localhost',user='root',passwd='rimi@2006')
mycursor=mydb.cursor()
print('''
----------------------------------------

Welcome To Library Management System!!!

----------------------------------------
''')
#Creating Database
mycursor.execute("CREATE DATABASE IF NOT EXISTS library_1")
mycursor.execute("USE library_1")
mycursor.execute("CREATE TABLE IF NOT EXISTS available_books(b_id INT, b_name VARCHAR(50), subject VARCHAR(50),quantity INT)")
mycursor.execute("CREATE TABLE IF NOT EXISTS issued(id INT, b_name VARCHAR(50), s_name VARCHAR(50),s_class VARCHAR(10))")
mycursor.execute("CREATE TABLE IF NOT EXISTS login(user VARCHAR(25), password VARCHAR(25))")
mydb.commit()
login_table_empty_or_not=0
mycursor.execute("SELECT * FROM login")
for i in mycursor:
    login_table_empty_or_not=1
if login_table_empty_or_not==0:
    mycursor.execute("INSERT INTO login VALUES('user','123')")
    mydb.commit()
#  Main Loop
#starts HeReEe!!
while True:
    print('''
1. Login
2. Exit
''')
    choice=input("Enter your choice (1/2): ")
    if ((choice!="1") and (choice!="2")):
        while choice not in ["1","2"]:
            choice=input("Enter 1/2: ")
    if choice=="1":
        passwd=input("\n\n------------------------------\n\nEnter Password:")
        mycursor.execute("SELECT * FROM login")
        logn="logout"
        for i in mycursor:
            t_user,t_pass=i
            if passwd==t_pass:
                logn="n"
        if logn=='n':
            print('''
------------------------------


Login Successful!!!
''')
        while logn=='n':
            print('''
------------------------------
1. Add New Books
2. Remove Any Book
3. Issue Book To Student
4. Return Book
5. View Available Books
6. View Issued Books
7. Logout
------------------------------
''')
            ch=input("Enter your choice:")
            while ch not in ['1','2','3','4','5','6','7']:
                ch=input("Enter 1/2/3/4/5/6/7:")
            if ch=="1":
                loop1='y'
                while loop1=='y':
                    print("\n------------------------------\n\n")
                    print("All Informations Are Mandatory To Be Filled!!!\n\n")
                    b_id=input("Enter Book ID:")
                    while not b_id.isnumeric():
                        b_id=input("Enter a numeric value for Book ID:")
                    mycursor.execute("SELECT * FROM available_books")
                    all_ids=[]
                    for i in mycursor:
                        t_id,b,c,d=i
                        all_ids.append(t_id)
                    while int(b_id) in all_ids:
                        print("\nBook with this ID already exists!!!\n")
                        b_id=input("Enter another Book ID:")
                        while not b_id.isnumeric():
                            b_id=input("Enter a numeric value for Book ID:")
                    b_name=input("Enter Book Name:")
                    subject=input("Enter Subject:")
                    qty=input("Enter Book Quantity:")
                    while not qty.isnumeric():
                        qty=input("Enter a numeric value for Quantity:")
                    sql_q=("INSERT INTO available_books(b_id,b_name,subject,quantity) VALUES({},'{}','{}',{})".format(int(b_id),b_name,subject,int(qty)))
                    mycursor.execute(sql_q)
                    mydb.commit()
                    print("\n------------------------------\n\nData Entered Successfully!!!\n\n------------------------------")
                    loop1=input("\nDo you want to add another book?(y/n):").lower()
                    while loop1 not in ['y','n']:
                        loop1=input("\nEnter(y/n):")    
#Loop1 completed!!
            elif ch=="2":
                loop2="y"
                while loop2=="y":
                    print("\n------------------------------\n\n")
                    print("All Informations Are Mandatory To Be Filled!!!\n\n")
                    b_id=int(input("Enter ID of the Book to be removed:"))
                    mycursor.execute("SELECT * FROM available_books")
                    book_found=False
                    for i in mycursor:
                        t_id,b_name,b_subject,b_qty=i
                        if t_id==b_id:
                            book_found=True
                    if book_found:
                        mycursor.execute("DELETE FROM available_books WHERE b_id={}".format(b_id))
                        mycursor.execute("DELETE FROM issued WHERE ID={}".format(b_id))
                        mydb.commit()
                        print("\n\nData Removed Successfully!!!")
                    else:
                        print("\n\nBook Not Found!!!")
                    loop2=input("\nDo you want to remove another book?(y/n):").lower()
                    while loop2 not in ['y','n']:
                        loop2=input("\nEnter(y/n):")    
#Loop2 completed!!
            elif ch=="3":
                loop3="y"
                while loop3=="y":
                    print("\n------------------------------\n\n")
                    print("All Informations Are Mandatory To Be Filled!!!\n\n")
                    b_id=int(input("Enter Book ID:"))
                    s_name=input("Enter student's name:")
                    s_class=input("Enter student's class:")
                    mycursor.execute("SELECT * FROM available_books WHERE b_id='{}'".format(b_id))
                    book_found=False
                    for i in mycursor:
                        t_id,b_name,b_subject,b_qty=i
                        if t_id==b_id:
                            book_found=True
                    if book_found:
                        if b_qty>0:
                            mycursor.execute("INSERT INTO issued VALUES({},'{}','{}','{}')".format(b_id,b_name,s_name,s_class))
                            mycursor.execute("UPDATE available_books SET quantity={} WHERE b_id={}".format((b_qty-1),b_id))
                            mydb.commit()
                            print("\n\nBook Issued Successfully!!!")
                        else:
                            print("\n\nBook Not Available...")
                    else:
                        print("\n\nBook Not Found!!!")
                    loop3=input("\nDo you want to issue another book?(y/n):").lower()
                    while loop3 not in ['y','n']:
                        loop3=input("\nEnter(y/n):")
#loop3 complete!!        
            elif ch=="4":
                loop4="y"
                while loop4=="y":
                    print("\n------------------------------\n\n")
                    print("All Informations Are Mandatory To Be Filled!!!\n\n")
                    b_id=int(input("Enter book ID:"))
                    s_name=input("Enter student's name:")
                    s_class=input("Enter student's class:")
                    mycursor.execute("SELECT * FROM issued")
                    book_issued=False
                    for i in mycursor:
                        t_id,t_b_name,t_s_name,t_s_class=i
                        if (t_id==b_id and t_s_name==s_name and t_s_class==s_class):
                            book_issued=True
                    if book_issued:
                        mycursor.execute("SELECT * FROM available_books WHERE b_id={}".format(b_id))
                        for i in mycursor:
                            t_id,t_name,t_subject,t_qty=i
                        mycursor.execute("DELETE FROM issued WHERE id={} and s_name='{}' and s_class='{}'".format(b_id,s_name,s_class))
                        mycursor.execute("UPDATE available_books SET quantity={} WHERE b_id={}".format((t_qty+1),b_id))
                        mydb.commit()
                        print("\n\nData Updated Successfully!!!")
                    else:
                        print("\n\nBook Is Not Issued Yet...")
                    loop4=input("\nDo you want to return another book?(y/n):").lower()
                    while loop4 not in ['y','n']:
                        loop4=input("\nEnter(y/n):")
#Loop4 complete!!
            elif ch=="5":
                print("\n------------------------------\n\n")
                mycursor.execute("SELECT * FROM available_books")
                print("ID\tBOOK NAME\t\tSUBJECT\t\t\tQUANTITY")
                for i in mycursor:
                    a,b,c,d=i
                    print(a,"\t",b,"\t\t",c,"\t\t",d)
            elif ch=="6":
                print("\n------------------------------\n\n")
                mycursor.execute("SELECT * FROM issued")
                print("ID\tBOOK NAME\tSTUDENT'S NAME\tSTUDENT'S CLASS")
                for i in mycursor:
                    a,b,c,d=i
                    print(a,"\t",b,"\t\t",c,"\t\t",d)
            elif ch=="7":
                logn="y"          
        if logn=="logout":
            print("\nWrong Password!!!\n------------------------------")
        elif logn=="y":
            print('''
Logged Out Successfully!!!
------------------------------
''')
    elif choice=="2":
        break
