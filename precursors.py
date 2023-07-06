import mysql.connector
mycon=mysql.connector.connect(host="localhost",user="root",
                                  passwd="kimaya",port='3306')
mycur=mycon.cursor()
mycur.execute("create database if not exists CITIZENS;")
mycur.execute("use citizens")

# GOVT TABLE WITH EMP NO. AS PRIMARY KEY
mycur.execute("CREATE TABLE if not exists GOVT (name varchar(25),STATE varchar(20),POST varchar(40),CONTACT_NUMBER varchar(20), EMP_NO varchar(10) NOT NULL PRIMARY KEY);")
add_officer=("INSERT INTO GOVT(name,STATE,POST,CONTACT_NUMBER, emp_no) VALUES ('SAMPLEOFFICER1', 'UTTAR PRADESH', 'HEAD-CONTR' , 0982222, 'SU140');")
mycur.execute(add_officer)
add_officer1=("INSERT INTO GOVT(name,STATE,POST,CONTACT_NUMBER,EMP_NO) VALUES ('SAMPLEOFFICER2', 'MAHARASHTRA', 'HEAD-CONTR' , 0989822, 'SM190');") 
mycur.execute(add_officer1)
#similar queries for other GOVT
mycon.commit()

#NATION TABLE WITH CITIZEN NUMBER AS PRIMARY KEY
mycur.execute("CREATE TABLE if not exists NATION (NAME varchar(25),AADHAR_CARD varchar(14),STATE varchar(20),BLOOD_GROUP varchar(21), CONTACT_NUMBER int, DOB date, CNUMBER varchar(10) NOT NULL PRIMARY KEY);")
add_officer=("INSERT INTO NATION(NAME,AADHAR_CARD,STATE,BLOOD_GROUP,CONTACT_NUMBER, DOB, CNUMBER) VALUES ('SAMPLE1', '123456789012', 'MAHARASHTRA', 'A+' , 0982222, '2000-12-12',  'SU221');")
mycur.execute(add_officer)
add_officer1=("INSERT INTO NATION(NAME,AADHAR_CARD,STATE,BLOOD_GROUP,CONTACT_NUMBER,DOB, CNUMBER) VALUES ('SAMPLE2', '123456789019' , 'GOA', 'B+' , 0989822, '2003-03-09' ,  'SM890');") 
mycur.execute(add_officer1)
mycon.commit()

print("All the prerequisites data has been created.")
