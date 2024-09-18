from flask import Flask, make_response,render_template,request

app=Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/set')
def setcookie():
    res=make_response('<h1>cookie is set</h1>')
    res.set_cookie('framework','flask')
    return res


@app.route('/get')
def getcookie():
    name=request.cookies.get('framework')
    return name

if __name__=='__main__':
    app.run(debug=True)