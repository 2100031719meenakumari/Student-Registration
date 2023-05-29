from flask import  *
import mysql.connector
app = Flask(__name__)

mydb = mysql.connector.connect(
  host="localhost",  user="root",  password="@jeevana123",   database="endsem")

@app.route('/',methods=['GET','POST'])
def homepage():
    return render_template("homepage.html")

@app.route('/java',methods=['GET','POST'])
def java():
    return render_template("java.html")
@app.route('/delete',methods=['GET','POST'])
@app.route('/register',methods=['GET','POST'])
def register():
    return render_template("register.html")
def delete():
    return render_template("delete.html")
@app.route('/admin',methods=['GET','POST'])
def location():
    return render_template("add.html")
@app.route('/clanguage',methods=['GET','POST'])
def clanguage():
    return render_template("c.html")
@app.route('/python',methods=['GET','POST'])
def python():
    return render_template("python.html")
@app.route('/home',methods=['GET','POST'])
def home():
    return render_template("head.html")



@app.route('/login',methods=['GET','POST'])
def login():
    return render_template("login.html")
@app.route('/save_login',methods=['GET','POST'])
def save_login():
    if(request.method=="POST"):
        email=request.form.get("Email")
        password=request.form.get("psw")
        mycursor = mydb.cursor()
        sql="select email,password from signup where email=%s and password=%s"
        data=(email,password,)
        mycursor.execute(sql,data)
        result = mycursor.fetchall()
        if(len(result)==1):
            return render_template("head.html")

        else:
            result = -1
            if result == -1:
                m = "check your email and password"
                l = "/login"
                ms = '<script type="text/javascript">alert("' + m + '");location="' + l + '";</script>'
                return ms
            return render_template("login.html")




@app.route('/save_add',methods=['GET','POST'])
def save_add():
    if (request.method == "POST"):
        Name = request.form.get("Name")
        email = request.form.get("email")
        password = request.form.get("psw")
        psw_repeat = request.form.get("psw_repeat")
        mycursor = mydb.cursor()
        mycursor.execute("SELECT email from signup where email='" + email + "'")
        result = mycursor.fetchall()
        if (len(result) == 0):
            mycursor.execute("INSERT INTO signup VALUES(%s,%s,%s,%s)", (Name, email, password, psw_repeat))
            mydb.commit()
            return render_template("login.html")
        else:
            result = -1
            if result == -1:
                m = "This email has already exists"
                l = "/signup"
                ms = '<script type="text/javascript">alert("' + m + '");location="' + l + '";</script>'
                return ms
            return render_template("signup.html")


@app.route('/save_register',methods=['GET','POST'])
def save_register():
    if (request.method == "POST"):
        Name = request.form.get("Name")
        email = request.form.get("email")
        course = request.form.get("course")

        mycursor = mydb.cursor()
        mycursor.execute("SELECT email from register where email='" + email + "'")
        result = mycursor.fetchall()
        if (len(result) == 0):
            mycursor.execute("INSERT INTO register VALUES(%s,%s,%s)", (Name, email, course))
            mydb.commit()
            return render_template("thankyou.html")
        else:
            result = -1
            if result == -1:
                m = "This email has already exists"
                l = "/signup"
                ms = '<script type="text/javascript">alert("' + m + '");location="' + l + '";</script>'
                return ms
            return render_template("signup.html")






if __name__ == "__main__":
    app.run(debug=True)
