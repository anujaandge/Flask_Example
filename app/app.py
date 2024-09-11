from flask import Flask, render_template

app=Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('Home.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    list={'Anu':23,'Nitin':28,'sonal':25}
    return render_template('dashboard.html',dashboard=list)

if __name__=="__main__":
    app.run(debug=True)