from flask import Flask,request, url_for, redirect, render_template
import pickle
import pandas as pd

app = Flask(__name__)

model=pickle.load(open('model.pkl','rb'))

column=pd.read_csv("qs-world-university-rankings-2017-to-2022-V2.csv")
universities=column['university'].unique()


@app.route('/')
def index():
    return render_template("home.html",universities=sorted(universities))

@app.route('/', methods=['GET','post'])
def predict():

	# form data
	GRE_Score = int(request.form['gre'])
	TOEFL_Score = int(request.form['toefl'])
	University= request.form['univ']
	SOP = float(request.form['sop'])
	LOR = float(request.form['lor'])
	CGPA = float(request.form['cgpa'])
	Research = int(request.form['research'])

	#fetching university rating based on university seleced 
	result = column.loc[column['university'] == University].iloc[0]
	University_Rating = int(result['score'])//20

	#model prediction 
	final_features = pd.DataFrame([[GRE_Score, TOEFL_Score, University_Rating, SOP, LOR, CGPA, Research]])
	predict = model.predict(final_features)
	output = predict[0]
    
	# rendering output
	return render_template('home.html', prediction_text='Admission chances are {}'.format(output),universities=sorted(universities))

if __name__ == '__main__':
    app.run(debug=True)
