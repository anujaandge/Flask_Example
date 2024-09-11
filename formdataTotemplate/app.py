from flask import Flask, render_template, request
app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('index.html')

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

if __name__=='__main__':
    app.run(debug=True)