import mysql.connector
import random
mydb = mysql.connector.connect(
   user='root', 
   password='Rahib@786',
   host='localhost',
   auth_plugin='mysql_native_password',
   database='Hospital')

mycursor = mydb.cursor()

def Entry():
	print("\n")
	Name=input("Name: ")
	while True:
		if Name:
			break
		else:
			Name= input("Name: ")
	Age=input("Age: ")
	Address=input("Address: ")
	Sex=input("Sex: ")
	mycursor.execute("SELECT Employee_ID FROM Doctor")

	myresult = mycursor.fetchall()

	Doctor_ID=random.choice(myresult)
	Doctor_ID=[x for x in Doctor_ID]	
	sql = "INSERT INTO Patient (Name, Age, Address,Doctor_ID, Sex) VALUES (%s, %s,%s,%s,%s)"
	val = (Name, Age, Address, Doctor_ID[0], Sex)
	mycursor.execute(sql, val)
	
	
	mydb.commit()
	Contact_Number=input("Enter Contact Number: ")
	while True:
		if len(Contact_Number) != 9:
			Contact_Number=input("Enter exact 9 digit Contact Number: ")
		else:
			break
	
	
	mycursor.execute("SELECT ID FROM Patient order by ID")
	Pat_ID = mycursor.fetchall()
	Pat_ID=[x for x in Pat_ID]
	Pat_ID.reverse()
	Pat_ID=Pat_ID[0][0]
	print("Patient ID assigned is :")
	print(Pat_ID)
	sql ="INSERT INTO Patient_Contact VALUES (%s, %s)"
	val = (Contact_Number, Pat_ID)
	mycursor.execute(sql,val)
	mydb.commit()
	
	sql="INSERT INTO COSTS VALUES (%s, %s)"
	val=( "500", Pat_ID)
	mycursor.execute(sql,val)
	mydb.commit()
	
	mycursor.execute("SELECT ID FROM Room")
	myresult = mycursor.fetchall()
	Room_ID=random.choice(myresult)
	Room_ID=[x for x in Doctor_ID]
	Room_ID=Room_ID[0]
	sql ="INSERT INTO Room_Assign VALUES (%s, %s)"
	val= (Pat_ID, Room_ID)
	mycursor.execute(sql,val)
	mydb.commit()
	print("\n")
def Display():
	print("\n")
	print("Enter appropraite option you want to search accordingly:")
	print("\n")
	print(" 1: Display all patients and details, 2: Search a particular name, 3: Display Nurses Assigned, 4: Display Room_Assigned 5: Display Expenses 6: Display Patient_Contact Details 7: Employee-Details 8:Doctors")
	print("\n")
	while True:
		option=input("")
		if option:
			break
		else:
			print("Enter Valid Option:")
	if option == '1':
		mycursor.execute("SELECT * FROM Patient")
		myresult = mycursor.fetchall()
		print("Pat_ID, Name, Age, Address, Doctor_ID, Sex")
		print("------------------------------------------")
		for item in myresult:
			print(item)
		print("\n\n")		
		mycursor.execute("SELECT * FROM Room_Assign")
		myresult = mycursor.fetchall()
		print("Room_ID, Pat_ID")
		print("---------------")
		for item in myresult:
			print(item)
		print("================")
		print("\n\n")
	elif option=='2':
		string=input("Enter Name")
		sql = "SELECT * FROM Patient WHERE Name= %s"
		val=(string,)
		mycursor.execute(sql,val)
		myresult = mycursor.fetchall()
		print("Pat_ID, Name, Age, Address, Doctor_ID, Sex")
		print("------------------------------------------")
		
		for item in myresult:
			print(item)	
		print("===========================================")
	elif option == '3':
		mycursor.execute("SELECT * FROM Nurse")
		myresult= mycursor.fetchall()
		print("Employee_ID, Room_ID")
		print("--------------------")
		for item in myresult:
			print(item)
		print("====================")
	elif option == '4':
		mycursor.execute("SELECT * FROM Room_Assign")
		myresult= mycursor.fetchall()
		print("Patient_ID, Room_ID")
		print("-------------------")
		for item in myresult:
			print(item)	
		print("===================")
	elif option == '5':
		mycursor.execute("Select * from COSTS")
		myresult = mycursor.fetchall()
		print("Price, Patient_ID")
		print("-----------------")
		for item in myresult:
			print(item)
		print("=================")
	elif option == '6':
		mycursor.execute("Select * from Patient_Contact")
		myresult= mycursor.fetchall()
		print("Contact_Number,Patient_ID")
		print("-------------------------")
		for item in myresult:
			print(item)	
		print("=========================")
	elif option == '7':
		mycursor.execute("select * from Employee")
		myresult= mycursor.fetchall()
		print("Employee_ID, Name, Sex, Salary, Address, Experience")
		print("---------------------------------------------------")
		for item in myresult:
			print(item)	
		print("===================================================\n")
	elif option == '8':
		mycursor.execute("select * from Doctor")
		myresult= mycursor.fetchall()
		print("Employee_ID, Status")
		print("-------------------")
		for item in myresult:
			print(item)	
		print("===================\n")
		
	else:
		print("\nNot a valid option\n")
	print("\n")
def Update_Expenses():
	print("\n")
	pat_id=input("Enter patient id: ")
	expense=int(input("Cost to be added: "))
	sql="SELECT Price FROM COSTS where Patient_ID= %s"
	val=(pat_id,)
	mycursor.execute(sql,val)
	cost=mycursor.fetchall()
	expense=expense+cost[0][0]
	sql = "UPDATE COSTS SET Price = %s WHERE Patient_ID = %s"
	val = (expense, pat_id)
	mycursor.execute(sql, val)
	mydb.commit()
		
	print(expense)
	print("\n")
while True:
	print(" 1: NewEntry || 2: Display_Details || 3: Update_Expenses\n\n")
	option=input("")
	while True:
		if option in ['1','2','3']:
			break
		else:
			option=input("Enter Valid Option")
	if option == '1':
		Entry()
	elif option == '2':
		Display()
	else:
		Update_Expenses()
	print("\n\n")
	print("Do you wish to stop? Press Q then.\n")
	ans= input('')
	if ans == 'Q':
		break
	else:
		continue
	print("\n\n")
	

		

