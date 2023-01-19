from flask import Flask, render_template, request, redirect,url_for, session, flash
from clientform import ClientForm, LoginUser, Register
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
from flask_login import LoginManager, UserMixin, login_user,  login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
import os
import requests

# from flask_ngrok import run_with_ngrok
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'zip'}
# Setting up the application
app = Flask(__name__)
app.config['SECRET_KEY'] = "secretkey"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///clients.db'
app.config['UPLOAD_FOLDER'] = 'static'



db = SQLAlchemy(app)
app.app_context().push()

loginmanager= LoginManager(app)

@loginmanager.user_loader
def load_user(user_id):
    return Client.query.get(int(user_id))

class Client(UserMixin, db.Model):
    id = db.Column(db.Integer, unique=True, primary_key=True, nullable=False)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(20), unique=False, nullable=False)
    name = db.Column(db.String, unique=False, nullable=True)
    email = db.Column(db.String, unique=False, nullable=True)
    address = db.Column(db.String, unique=False, nullable=True)
    phone = db.Column(db.String, unique=False, nullable=True)
    date = db.Column(db.String, unique=False, nullable=True)
    time = db.Column(db.String, unique=False, nullable=True)
    file = db.Column(db.String, unique=False, nullable=True)
    service = db.Column(db.String)
    package = db.Column(db.String)
    col13 = db.Column(db.String)
    col14 = db.Column(db.String)

    def __repr__(self):
        return '<Username: {}>'.format(self.username)

db.create_all()


# run_with_ngrok(app)

url = 'https://api.npoint.io/e21406b80f9016c674e8'
response = requests.get(url).json()

# making route

@app.route('/')
def home():
    return render_template('main.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = Register()
    if request.method == 'POST':
        email = request.form.get('email')
        username = request.form.get('username').lower()
        name = request.form.get('name')
        hashed_password = generate_password_hash(request.form.get('password'), method='pbkdf2:sha256', salt_length=8)
        password = hashed_password
        print(email, username, password)
        new_client = Client(email=email, username=username, password=password, name=name)
        db.session.add(new_client)
        db.session.commit()
        client = Client.query.all()
        print('client{}'.format(client))
        user = Client.query.filter_by(username=username).first()
        print(user.username)
        login_user(user)
        flash('halo {}, you are registered, please login'.format(user.username))
        return redirect(url_for('home'))
    return render_template('registers.html', form=form)



@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginUser()
    if request.method == 'POST':
        password = request.form.get('password')
        user = Client.query.filter_by(username=request.form['username']).scalar()
        if user == None:
            flash('user does no t exist')
        else:
            if check_password_hash(user.password, password):
                login_user(user)
                session['username'] = user.username
                flash(f"you are logged in, welcome {user.username}")
                return redirect(url_for('home'))
            # if not request.form['password'] == user.password:
            #     flash('wrong password', 'error')
            # else:
            #     session['username'] = user.username
            #     flash(f"you are logged in, welcome {session['username']}")
            #     return redirect(url_for('home'))
        return render_template('logins.html', form=form)
    return render_template('logins.html', form=form)

@app.route('/logout')
def logout():
    if 'username' in session:
        session.pop('username')
        logout_user()
        flash('you are logged out')
    else:
        flash('you are already logged out, please login again')
    return redirect(url_for('home'))

@app.route('/cliendata', methods=['GET', 'POST'])
def wtform():
    name = None
    form = ClientForm()
    if 'username' in session:
        if request.method == 'POST':
            name = form.fullname.data
            email = form.email.data
            address = form.address.data
            phone = form.phone.data
            date = form.date.data
            time = form.time.data
            file = form.payment.data
            print(type(date))
            print(file.filename)
            client_to_update = Client.query.filter_by(username=session['username']).first()
            print(client_to_update.email)
            client_to_update.email = email
            client_to_update.name = name
            client_to_update.address = address
            client_to_update.phone = phone
            client_to_update.date = date.strftime("%Y %m %d")
            client_to_update.time = time.strftime("%H:%M:%S")
            client_to_update.service = request.form.get('service')
            client_to_update.package = request.form.get('package')
            client_to_update.file = file.filename
            db.session.commit()
            file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)), app.config['UPLOAD_FOLDER'], secure_filename(file.filename)))

            return redirect(url_for('userpage'))
        return render_template("wtform.html", name=name, form=form)
    else:
        flash('you need to login')
        return redirect(url_for('home'))

@app.route('/user')
@login_required
def user():
    if 'username' in session and current_user.is_authenticated:

        user = Client.query.filter_by(username=session['username']).first()
        username = user.username
        name = user.name
        email = user.email
        address = user.address
        phone = user.phone
        date = user.date
        time = user.time
        if user.file == None:
            payment = 'kosong'
        else:

            payment = user.file
        return render_template('user.html', username=username, user=name, email=email, address=address, phone=phone, date=date, time=time, payment=payment)
    else:
        flash('you need to log in')
        return redirect(url_for('home'))
@app.route('/userpage')
def userpage():
    if 'username' in session and current_user.is_authenticated:

        user = Client.query.filter_by(username=session['username']).first()
        username = user.username
        name = user.name
        email = user.email
        address = user.address
        phone = user.phone
        date = user.date
        time = user.time
        service = user.service
        package = user.package
        if user.file == None:
            print(user.file)
            payment = 'kosong'
        else:

            payment = user.file
            print(user.file)
        return render_template('userpage.html', username=username, name=name, email=email, address=address, phone=phone, date=date, time=time, service=service, package=package, payment=payment)
    else:
        flash('you need to log in')
        return redirect(url_for('home'))



# running application
if __name__ == '__main__':
   app.run(host='0.0.0.0', debug=True)