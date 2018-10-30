from flask import Flask
app = Flask(__name__)
@app.route("/")
def index():
     return "Hello World!"
@app.route('/hi/<name>')
    return 'Hello  %s'  %name
@app.route('/num/<ans>')
def hello_name(ans):
    return 'Hello  %f'  %ans
@app.route('/sum/<value>')
def The_name(value):
    return 'The sum  %d'  %value
if __name__ == '__main__':
    app.run(debug=True)
