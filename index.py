from flask import Flask,request,render_template,redirect,url_for,flash
import sqlite3

app = Flask(__name__)
app.secret_key='123'

username = "srinath"
passwd = "1231"

all_username=[]
all_password=[]
all_mail = []
all_contact = []
list_name=[]

@app.route("/")
def home():
    return render_template("home_page.html")

@app.route("/home")
def html_home():
    return render_template("project_web.html")

@app.route('/intro')
def intro():
    return render_template("html_intro.html")

@app.route('/heading')
def heading():
    return render_template("html_heading.html")

@app.route('/css_home')
def css_home():
    return render_template("project_css.html")

@app.route('/css_intro')
def css_intro():
    return render_template("css_intro.html")

@app.route('/login1')
def login1():
    return render_template("login.html")

@app.route('/login', methods=['POST','GET'])
def login():
    if request.method=='POST':
        name = request.form.get("uname")
        password = request.form.get("password")
        list_name.clear()
        list_name.append(name)
        if name == username and password == passwd:
            return redirect(url_for('user'))
        elif name in all_username:
            where = all_username.index(name)
            if name == all_username[where]  and password == all_password[where]:
                return redirect(url_for('user'))
            elif name == all_username[where]  and password != all_password[where]:
                flash("Wrong username and password", "danger")
                return redirect(url_for('login1'))
        elif name in all_mail:
            where = all_mail.index(name)
            if name==all_mail[where] and password == all_password[where]:
                return redirect(url_for('user'))
            elif name==all_mail[where] and password != all_password[where]:
                flash("Wrong username and password", "danger")
                return redirect(url_for('login1'))

        elif name in all_contact:
            where = all_contact.index(name)
            if name==all_contact[where] and password == all_password[where]:
                return redirect(url_for('user'))
            elif name == all_contact[where] and password != all_password[where]:
                flash("Wrong username and password", "danger")
                return redirect(url_for('login1'))
        else:
            flash("Wrong username and password", "danger")
            return redirect(url_for('login1'))

@app.route('/user')
def user():
    return render_template("p1_h_home.html",name2 = list_name[0])

@app.route('/signup')
def signup():
    return render_template("signup.html")

@app.route('/account',methods=['POST','GET'])
def account():
    if request.method=='POST':
        name = request.form.get("uname")
        mail = request.form.get("mail")
        contact = request.form.get("contact")
        password = request.form.get("password")
        if name in all_username:
            flash("Username already exists", "danger")
            return redirect(url_for('signup'))
        elif mail in all_mail:
            flash("Email already exists", "danger")
            return redirect(url_for('signup'))
        elif contact in all_contact:
            flash("contact already exists", "danger")
            return redirect(url_for('signup'))
        else:
            all_username.append(name)
            all_mail.append(mail)
            all_contact.append(contact)
            all_password.append(password)

    flash("Account created successfully", "success")
    return redirect(url_for('login1'))

@app.route('/l_home')
def l_home():
    return render_template("p1_hh.html",name2 = list_name[0])

@app.route('/l_intro')
def l_intro():
    return render_template("p1_h_intro.html",name2 = list_name[0])

@app.route('/l_heading')
def l_heading():
    return render_template("p1_h_heading.html",name2 = list_name[0])

@app.route('/lc_home')
def lc_home():
    return render_template("p1_c_home.html",name2 = list_name[0])

@app.route('/lc_intro')
def lc_intro():
    return render_template("p1_c_intro.html",name2 = list_name[0])


if __name__ == ("__main__"):
    app.run(debug=True)
