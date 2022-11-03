from flask import Flask,request, url_for, redirect, render_template
import pickle
import pandas as pd

app = Flask(__name__)

model=pickle.load(open('model.pkl','rb'))


@app.route('/')
def index():
    column=pd.read_csv("qs-world-university-rankings-2017-to-2022-V2.csv")
    universities=column['university'].unique()
    return render_template("home.html",universities=sorted(universities))


if __name__ == '__main__':
    app.run(debug=True)
