from flask import Flask,render_template,redirect,request
import pickle
import numpy as np

model=pickle.load(open('auto_mpg.pkl','rb'))


app=Flask(__name__)

@app.route('/')
def home():

    return render_template('home.html')

@app.route('/predict',methods=['POST'])
def predict():
    if request.method =='POST':
        cy=int(request.form['cy'])
        dis = float(request.form['dis'])
        ho = float(request.form['ho'])
        we = float(request.form['we'])
        acc = float(request.form['acc'])
        mo = float(request.form['mo'])
        origin = str(request.form['origin'])

        if origin == 'a':
            m=0
            n=1
            o=0
        elif origin =='b':
            m = 0
            n = 0
            o = 1

        else:
            m=1
            n=0
            o=0
        int_features = []

        int_features.append(cy)
        int_features.append(dis)
        int_features.append(ho)
        int_features.append(we)
        int_features.append(acc)
        int_features.append(mo)
        int_features.append(m)
        int_features.append(n)
        int_features.append(o)
        final_features = [np.array(int_features)]
        prediction = model.predict(final_features)
        prediction=round(prediction[0][0],2)

        return render_template('home.html',pred="The mileage of the car will be :{0} ".format(prediction))



















if __name__=='__main__':
    app.run(debug=True)
