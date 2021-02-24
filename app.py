from flask import Flask,render_template,redirect,request
import pickle
import numpy as np

model=pickle.load(open('auto_mpg.pkl','rb'))


app=Flask(__name__)

@app.route('/')
def home():

    return render_template('home.html')

















if __name__=='__main__':
    app.run(debug=True)
