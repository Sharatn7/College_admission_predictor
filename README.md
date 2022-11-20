# College_admission_predictor
An simple application that displays the chance of admit to a university based on your scores

# To run this project, you will need to download a couple of datasets
1. Admission_Predict_Ver1.1.csv ---> https://www.kaggle.com/code/suneelpatel/graduate-admission-analysis-and-prediction/data?select=Admission_Predict_Ver1.1.csv
2. qs-world-university-rankings-2017-to-2022-V2.csv ----> https://www.kaggle.com/datasets/padhmam/qs-world-university-rankings-2017-2022

# First create a python virtual env 
  - conda create -n myvenv python=3.9
  - conda activate myvenv

If you dont have conda then follow https://docs.python.org/3/library/venv.html to create the virtual environment.

Now install the required libraries inside the virtual environment
click==8.1.3,
Flask==2.2.2,
itsdangerous==2.1.2,
Jinja2==3.1.2,
joblib==1.2.0,
MarkupSafe==2.1.1,
numpy==1.23.4,
pandas==1.5.1,
python-dateutil==2.8.2,
pytz==2022.6,
scikit-learn==1.1.3,
scipy==1.9.3,
six==1.16.0,
sklearn==0.0,
threadpoolctl==3.1.0,
Werkzeug==2.2.2

Now execute the jupyter notebook (Admission_predictor.ipynb) and download the model.pkl file.
Add this pkl file in the main directory of the project file.

# To run Flask Server

Open up your command prompt and enter the command  ----> python app.py or flask run
This is start up your server, follow the URL and make your predictions


