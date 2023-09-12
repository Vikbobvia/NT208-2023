import mariadb


dataBase = mariadb.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Database123'
)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE first_dj_website ")

print("All done !")