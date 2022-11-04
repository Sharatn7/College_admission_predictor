from flask import Flask,request, url_for, redirect, render_template
import pickle
import pandas as pd
import numpy as np

app = Flask(__name__)

model=pickle.load(open('model.pkl','rb'))


@app.route('/')
def index():
    column=pd.read_csv("qs-world-university-rankings-2017-to-2022-V2.csv")
    universities=column['university'].unique()
    return render_template("home.html",universities=sorted(universities))

@app.route('/predict', methods=['GET','post'])
def predict():
	GRE_Score = int(request.form['gre'])
	TOEFL_Score = int(request.form['toefl'])
	University_Rating = int(request.form['univ'])
	SOP = float(request.form['sop'])
	LOR = float(request.form['lor'])
	CGPA = float(request.form['cgpa'])
	Research = int(request.form['research'])
	
    # column=pd.read_csv("qs-world-university-rankings-2017-to-2022-V2.csv")

	final_features = pd.DataFrame([[GRE_Score, TOEFL_Score, University_Rating, SOP, LOR, CGPA, Research]])
	
	predict = model.predict(final_features)
	
	output = predict[0]
        
	return render_template('home.html', prediction_text='Admission chances are {}'.format(output))

    # if output<str(0.5):
    #     return render_template('home.html',pred='Your chances are low.\nProbability of you getting admission is {}'.format(output))
    # else:
    #     return render_template('home.html',pred='Your chances are high.\n Probability of fire occuring is {}'.format(output))

if __name__ == '__main__':
    app.run(debug=True)
