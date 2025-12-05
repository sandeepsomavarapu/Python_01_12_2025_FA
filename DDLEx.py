#py -m pip install oracle
#py -m pip uninstall mysql-connector
#(latest version)
#py -m pip install  mysql-connector-python       
import mysql.connector

mydb=mysql.connector.connect(host="localhost",user="root",passwd="rpsconsulting",database="fai")

mycursor=mydb.cursor()

mycursor.execute("create table employees(eid int,ename varchar(10),esal int)");
print("Table Created")