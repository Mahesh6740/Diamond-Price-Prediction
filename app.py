'''import flask
from flask import request,render_template
import pickle
app = flask.Flask(name,static_url_path='')

model = pickle.load(open('model.pkl','rb'))

@app.route('/',methods= ['GET'])

def sendhomepage():
    return render_template('index.html')

@app.route('/predict',methods= ['POST'])

def predictspecies():
    ct = float(request.form['ca'])
    cu = int(request.form['sw'])
    co = int(request.form['pl'])
    cl = int(request.form['pw'])
    dp = float(request.form['dp'])
    tb = float(request.form['tb'])
    x = float(request.form['x'])
    y = float(request.form['y'])
    z = float(request.form['z'])
    X = [[ca,sw,pl,pw,dp,tb,x,y,z]]
    price = model.predict(x)[0]
    return render_template('index.html',predict = price)

if name == 'main' :
    app.run(debug = True)'''
import flask
from flask import request, render_template
import pickle

app = flask.Flask(__name__)

model = pickle.load(open('model.pkl', 'rb'))

@app.route('/', methods=['GET'])
def send_homepage():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict_species():
    # Extracting form data
    ct = float(request.form['ct'])
    cu = int(request.form['cu'])
    co = int(request.form['co'])
    cl = int(request.form['cl'])
    dp = float(request.form['dp'])
    tb = float(request.form['tb'])
    x = float(request.form['x'])
    y = float(request.form['y'])
    z = float(request.form['z'])
    
    # Preparing data for prediction
    X = [[ct, cu, co, cl, dp, tb, x, y, z]]
    
    # Predicting
    price = model.predict(X)[0]
    
    # Rendering the result
    return render_template('index.html', predict=price)

if __name__ == '__main__':
    app.run(debug=True)

