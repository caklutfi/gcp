from flask import Flask, render_template, request, redirect,url_for, session, flash
from clientform import ClientForm, LoginUser, Register
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
from flask_login import LoginManager, UserMixin, login_user,  login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
import os
import requests
from mongo import fetchall, fetchone, create_user, find_user, get_package


ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'zip'}
# Setting up the application
app = Flask(__name__)
app.config['SECRET_KEY'] = "secretkey"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///clients.db'
app.config['UPLOAD_FOLDER'] = 'static'


db = SQLAlchemy(app)
app.app_context().push()

# loginmanager= LoginManager(app)

# @loginmanager.user_loader
# def load_user(user_id):
#     return Client.query.get(int(user_id))

# class Client(UserMixin, db.Model):
#     id = db.Column(db.Integer, unique=True, primary_key=True, nullable=False)
#     username = db.Column(db.String(20), unique=True, nullable=False)
#     password = db.Column(db.String(20), unique=False, nullable=False)
#     name = db.Column(db.String, unique=False, nullable=True)
#     email = db.Column(db.String, unique=False, nullable=True)
#     address = db.Column(db.String, unique=False, nullable=True)
#     phone = db.Column(db.String, unique=False, nullable=True)
#     date = db.Column(db.String, unique=False, nullable=True)
#     time = db.Column(db.String, unique=False, nullable=True)
#     file = db.Column(db.String, unique=False, nullable=True)
#     service = db.Column(db.String)
#     package = db.Column(db.String)
#     col13 = db.Column(db.String)
#     col14 = db.Column(db.String)
#
#     def __repr__(self):
#         return '<Username: {}>'.format(self.username)

# db.create_all()


url = 'https://api.npoint.io/e21406b80f9016c674e8'
response = requests.get(url).json()


jualan= []
dagangan = fetchall()
for i in dagangan:
    jualan.append(i)

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
        name = request.form.get('name').title()
        hashed_password = generate_password_hash(request.form.get('password'), method='pbkdf2:sha256', salt_length=8)
        password = hashed_password
        print(email, username, password)
        # new_client = Client(email=email, username=username, password=password, name=name)
        # db.session.add(new_client)
        # db.session.commit()
        # client = Client.query.all()
        # print('client{}'.format(client))
        # user = Client.query.filter_by(username=username).first()
        # print(user.username)
        create_user(email, username, password, name)

        # login_user(user)
        # flash('halo {}, you are registered, please login'.format(user.username))
        return redirect(url_for('home'))
    return render_template('registers.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    session.pop('username', None)
    form = LoginUser()
    if request.method == 'POST':
        password = request.form.get('password')
        # user = Client.query.filter_by(username=request.form['username']).scalar()
        username = request.form.get('username')
        print(username, type(username))
        query = find_user(username)
        if query is not None:

            print(type(query),query)
            print(query['email'])
            if check_password_hash(query['password'],password):
                session['username']= query['username']
                print("session username is:", session['username'])
                return redirect(url_for('home'))
            else:
                print('wrong password')
                flash('wrong password')
                return redirect(url_for('login'))

            # session['mongo'] = find_user(request.form.get('username'))
            # print(session['mongo']['username'])
            # username = session['mongo']['username']
            # mongo_pass = session['mongo']['password']
            # print(username, mongo_pass)

        else:
            print('user not exist')
            flash('user does not exist')
    return render_template("logins.html", form=form)

#not used
@app.route('/logins', methods=['GET', 'POST'])
def logins():
    form = LoginUser()
    if request.method == 'POST':
        password = request.form.get('password')
        # user = Client.query.filter_by(username=request.form['username']).scalar()
        if user == None:
            flash('user does no t exist')
        else:
            if check_password_hash(user.password, password):
                # login_user(user)
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
# @login_required
def logout():
    if 'username' in session:
        session.pop('username')
        # logout_user()
        # flash('you are logged out')
    else:
        flash('you are already logged out, please login again')
    return redirect(url_for('home'))

@app.route('/wtform', methods=['GET', 'POST'])
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
            # client_to_update = Client.query.filter_by(username=session['username']).first()
            # print(client_to_update.email)
            # client_to_update.email = email
            # client_to_update.name = name
            # client_to_update.address = address
            # client_to_update.phone = phone
            # client_to_update.date = date.strftime("%Y %m %d")
            # client_to_update.time = time.strftime("%H:%M:%S")
            # client_to_update.service = request.form.get('service')
            # client_to_update.package = request.form.get('package')
            # client_to_update.file = file.filename
            # db.session.commit()
            file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)), app.config['UPLOAD_FOLDER'], secure_filename(file.filename)))

            return redirect(url_for('userpage'))
        return render_template("wtform.html", name=name, form=form)
    else:
        flash('you need to login')
        return redirect(url_for('home'))

@app.route('/form', methods=['GET', 'POST'])
# @login_required
def form():
    username = session['username']
    # nama = Client.query.filter_by(username=username).first()
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
            # print(file.filename)
            # client_to_update = Client.query.filter_by(username=session['username']).first()
            # print(client_to_update.email)
            # client_to_update.email = email
            # client_to_update.name = name
            # client_to_update.address = address
            # client_to_update.phone = phone
            # client_to_update.date = date.strftime("%Y %m %d")
            # client_to_update.time = time.strftime("%H:%M:%S")
            # client_to_update.service = request.form.get('service')
            # client_to_update.package = request.form.get('package')
            # client_to_update.file = file.filename
            db.session.commit()
            # file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)), app.config['UPLOAD_FOLDER'],
            #                        secure_filename(file.filename)))

            return redirect(url_for('userpage'))
        return render_template("form.html", name=nama.name, form=form)
    else:
        flash('you need to login')
        return redirect(url_for('home'))


#not used
@app.route('/user')
# @login_required
def user():
    if 'username' in session:

        # user = Client.query.filter_by(username=session['username']).first()
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
# @login_required
def userpage():
    if 'username' in session:
        print(request.args.get('booking_info'))


        # user = Client.query.filter_by(username=session['username']).first()
        query = find_user(session['username'])
        username = query['username']
        name = query.get('name')
        email = query.get('email')
        address = query.get('address')
        phone = query.get('phone')
        date = query.get('date')
        time = query.get('time')
        service = query.get('service')
        package = query.get('package')
        # if user.file == None:
        #     print(user.file)
        #     payment = 'kosong'
        # else:
        #
        #     payment = user.file
        #     print(user.file)
        return render_template('userpage.html', username=username, name=name, email=email, address=address, phone=phone, date=date, time=time, service=service, package=package)
    else:
        flash('you need to log in')
        return redirect(url_for('home'))

@app.route('/services')
def services():
    jualan = []
    dagangan = fetchall()
    for i in dagangan:
        jualan.append(i)

    return render_template('services.html', services=jualan)

@app.route('/product')
def product():

    img_pool = {'engagement': 'https://storage.googleapis.com/assets-caklutfi/engagement-lg.jpg',
                'wedding': 'https://storage.googleapis.com/assets-caklutfi/wedding-lg.jpg',
                'prewedding': 'https://storage.googleapis.com/assets-caklutfi/prewed-lg.jpg',
                'graduation': 'https://storage.googleapis.com/assets-caklutfi/wisuda-lg.jpg'}

    jualan = [x for x in fetchall()]
    print(jualan)


    product = fetchone(request.args.get('service'))

    img = img_pool[request.args.get('service')]
    dagangan =[x for x in get_package(request.args.get('service'))]
    print(dagangan)
    print(type(product))
    return render_template('product.html', dagangan=dagangan, services=jualan, image=img)

@app.errorhandler(401)
def custom_401(error):
    return redirect(url_for('home'))


# running application
if __name__ == '__main__':
   app.run(host='0.0.0.0', debug=True)