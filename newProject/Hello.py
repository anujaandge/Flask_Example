from flask import Flask

app=Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World"

@app.route('/hi')
def hi():
    return "Hi, How are you?"
  

if __name__=='__main__':
    app.debug=True
    app.run()
    app.run(debug=True)
    