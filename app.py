from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/')
def index():
  return "<h1>Welcome to flask tutorial</h1>"


@app.route('/home', methods=['GET', 'POST'])
def home():
  return "<h1>Welcome to Home page</h1>"


@app.route('/json', methods=['GET'])
def json():
  return jsonify({'key1':'value1', 'key2':[10,20,30]})



@app.route('/person', methods=['GET', 'POST'], defaults={'name':'shubham'})
@app.route('/person/<int:name>', methods=['GET', 'POST'])
def person(name):
  return "<h1> hi {} welcome to person page </h1>".format(name)


@app.route('/query')
def query():
  name = request.args.get('name')
  location = request.args.get('location')
  return "<h1>hi {} You are from {} Welcome to query page</h1>".format(name,location)


@app.route('/theform')
def theform():
    return '''<form method = "POST" action="/process">
               <input type="text" name="name"> 
               <input type="text" name="location">
               <input type="submit" value="Submit">
              </form>'''

@app.route('/process', methods =['POST','GET'])
def process():
    name = request.form['name']
    location = request.form['location']
    return '<h1>Hi, {}. you are from {}. form submited sussesfully!!!!.</h1>'.format(name, location)






if __name__ == '__main__':
  app.run(debug=True)

