# Script to check the connection to the database we created earlier airflowdb

# importing the connector from mysqlclient
import mysql.connector as mysql

# connecting to the database using the connect() method
# it takes 3 parameters: user, host, and password

dbconnect = mysql.connect(host="localhost", 
                          user="airflow", 
                          password="python2019", 
                          db="airflowdb")

# print the connection object
print(dbconnect)

# do not forget to close the connection
dbconnect.close()