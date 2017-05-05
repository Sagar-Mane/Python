from flask import Flask, jsonify
from flaskext.mysql import MySQL


app = Flask(__name__)

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = ''
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = ''
app.config['MYSQL_DATABASE_HOST'] = ''
app.config['MYSQL_DATABASE_PORT'] = ''
mysql.init_app(app)


def mySQL():
    print ("Returning successful login")
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * from TENANT_TABLE")
    data = cursor.fetchall();
    print (data)
    query = "INSERT INTO TENANT_TABLE (Tenant_id, Tenant_Name, Description) VALUES ('1','Kaushik','Legend_101')"
    cursor.execute(query)
    conn.commit()

mySQL()
