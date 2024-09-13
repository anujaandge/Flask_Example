from flask import Flask, render_template,request, flash, redirect, url_for, session
import formsubmission


app=Flask(__name__)
app.secret_key="private_key"

#home page
@app.route('/')
def defaultHome():
    return render_template('index.html')


@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

#login page
@app.route('/login',methods=['POST','GET'])
def login():
    if request.method=='POST':
        userName= request.form['name']
        userPassword=request.form['password']
        if userName=='admin' and userPassword=='admin123':
            return render_template('dashboard.html',name=userName)
        else:
            return render_template('index.html')
    else:
        userName=request.args.get('name')
        return render_template('login.html',name=userName)     

#registrationForm
@app.route('/registrationForm',methods=['POST','GET'])
def registrationForm():
    mayinsoftRegistarionForm = formsubmission.MayinsoftRegistarionForm()
    if request.method == 'POST':
        session['name'] = mayinsoftRegistarionForm.name.data
        if not mayinsoftRegistarionForm.validate():
            flash("Please fill out this field", "error")
            return render_template('register.html', Form=mayinsoftRegistarionForm)
        return redirect(url_for('sucessformsubmission'))  # Redirect after form submission
    return render_template('register.html', Form=mayinsoftRegistarionForm)  # Pass form in GET request
   
@app.route('/sucessformsubmission')
def sucessformsubmission():
    name=session.get('name',None)
    return render_template('sucessformsubmission.html')        
    

if __name__=="__main__":
    app.run(debug=True)
