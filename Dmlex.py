
import mysql.connector

mydb=mysql.connector.connect(host="localhost",user="root",passwd="rpsconsulting",database="fai")

mycursor=mydb.cursor()

mycursor.execute("update employees set esal=esal+7000");
mydb.commit();
print("1 Record Updated")