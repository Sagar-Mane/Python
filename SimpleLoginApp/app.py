from flask import Flask, render_template, request, send_file
from flaskext.mysql import MySQL
mysql = MySQL()
app = Flask(__name__)

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'sagar123'
app.config['MYSQL_DATABASE_DB'] = 'user_data_python_login'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)
conn = mysql.connect()
cursor = conn.cursor()
numrows = cursor.execute("SELECT * FROM user")
print numrows

@app.route("/")
def main():
    return send_file("templates/index.html")

@app.route("/signIn", methods=['POST'])
def signIn():
    print "Reporting form python backend signin function"
    print request.data
    return send_file("templates/signup.html")


if __name__ == "__main__":
    print "Python Server Running at port 5000"
    app.run()


