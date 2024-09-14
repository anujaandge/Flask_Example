from flask import Flask, render_template,request, flash, redirect, url_for, session
from flask_mysqldb import MySQL
import formsubmission
import bcrypt


app=Flask(__name__)
app.secret_key="private_key"

# MySQL configurations
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Nitin@0806'
app.config['MYSQL_DB'] = 'mydatabase'

# Initialize MySQL
mysql = MySQL(app)

#home page
@app.route('/')
def defaultHome():
    return render_template('index.html')


@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    userName = request.args.get('name', '')
    return render_template('dashboard.html',name=userName)

#login page
@app.route('/login',methods=['POST','GET'])
def login():
    if request.method=='POST':
        userName= request.form['name']
        userPassword=request.form['password']
        cur = mysql.connection.cursor()
        cur.execute(f"SELECT password FROM users WHERE name = '{userName}'")
        result = cur.fetchone()
        cur.close()
        
        if result and bcrypt.checkpw(userPassword.encode('utf-8'), result[0].encode('utf-8')):
            return redirect(url_for('dashboard', name=userName))
        else:
            return render_template('index.html', error="Invalid username or password")
        
    else:
        userName=request.args.get('name')
        return render_template('login.html',name=userName)     

#registrationForm
@app.route('/registrationForm',methods=['POST','GET'])
def registrationForm():
    mayinsoftRegistarionForm = formsubmission.MayinsoftRegistarionForm()
    if request.method=='POST':
        #validate form data
        if mayinsoftRegistarionForm.validate_on_submit():
            name=mayinsoftRegistarionForm.name.data
            password = mayinsoftRegistarionForm.password.data
            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
            phone_number = mayinsoftRegistarionForm.phoneNumber.data
            gender = mayinsoftRegistarionForm.gender.data
            age = mayinsoftRegistarionForm.age.data
            address = mayinsoftRegistarionForm.address.data
            
             # Create MySQL cursor
            cur = mysql.connection.cursor()
            
            # Check if the user already exists
            cur.execute("SELECT * FROM users WHERE name = %s OR mobile_number = %s", (name, phone_number))
            existing_user = cur.fetchone()
            
            if existing_user:
                # User already exists
                flash('User already exists. Please register again.', 'error')
                return render_template('register.html', Form=mayinsoftRegistarionForm)
            
            # If user does not exist, insert into the database
            cur.execute(
                "INSERT INTO users (name, password, mobile_number, gender, age, address) VALUES (%s, %s, %s, %s, %s, %s)",
                (name, hashed_password, phone_number, gender, age, address)
            )
            
             # Commit changes
            mysql.connection.commit()
            
            # Close cursor
            cur.close()
            
            # Redirect to success page
            session['name'] = name
            return redirect(url_for('sucessformsubmission'))
            
    # Render the registration form template
    return render_template('register.html', Form=mayinsoftRegistarionForm)

    
   
@app.route('/sucessformsubmission')
def sucessformsubmission():
    name=session.get('name',None)
    return render_template('sucessformsubmission.html')        
    

if __name__=="__main__":
    app.run(debug=True)
