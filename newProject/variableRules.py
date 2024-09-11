from flask import Flask

app=Flask(__name__)

@app.route('/blog/<int:postID>')
def show_blog(postID):
    return 'Blog Number %d' %postID

@app.route('/reg/<float:regNo>')
def registraion(regNo):
    return "Registration number %f" %regNo

@app.route('/flask')
def hello_flask():
    return "Hello Flask"

@app.route('/python/')
def hello_python():
    return "Hello Python"

if __name__=='__main__':
    app.run(debug=True)
