from flask import Flask, request, render_template
from flask_mysqldb import MySQL

app = Flask(__name__)
mysql = MySQL(app)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Metapi'
app.config['MYSQL_DB'] = 'mydb'


@app.route("/", methods = ["GET", "POST"])
def index():
    if request.method =='POST':
        username = request.form['username']
        email = request.form['email']

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (username, email))
        cur.connection.commit()
        cur.close()

        return 'Successfully updated record in database'
    return render_template("index.html")

@app.route("/users")
def getusers():
    cur = mysql.connection.cursor()
    users = cur.execute("SELECT * FROM users")
    if users >0:
        userDetails = cur.fetchall()
        
    return render_template('users.html', users = userDetails)



if __name__ =="__main__":
    app.run(debug=True)