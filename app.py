from tkinter.ttk import Style
from flask import Flask,render_template,request,Markup
import pickle
import numpy as np

model = pickle.load(open('model.pkl','rb'))

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict_heart_attack():
    age = int(request.form.get('age'))
    sex = int(request.form.get('sex'))
    cp = int(request.form.get('cp'))
    thalach = int(request.form.get('thalach'))
    exang = int(request.form.get('exang'))
    slope = int(request.form.get('slope'))
    ca = int(request.form.get('ca'))
    thal = int(request.form.get('thal'))
    trtbps = int(request.form.get('trtbps'))
    oldpeak = int(float(request.form.get('oldpeak')))

    #prediction
    result = model.predict(np.array([age,sex,cp,thalach,exang,slope,ca,thal,trtbps,oldpeak]).reshape(1,10))

    if result[0] == 1:
        result = Markup('There is a chance of getting a heart attack.<br><br>Use Statins, these are medicines that reduce the risk of heart attack and stroke by helping to lower the amount of cholesterol and other fats in the blood.')
        
    else:
        result = Markup('There is no chance of getting a heart attack.<br><br>But, take preventive steps to avoid getting a heart attack in the future.')

    return render_template('result.html',prediction=result)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080)
