import mysql.connector as mysql
cnx = mysql.MySQLConnection(
    host = "db-server-evergreen-d.mysql.database.azure.com",
    port = 3306,
    user = "evergreenadmin@db-server-evergreen-d",
    password="Integrador19",
    database="evergreen"
)
