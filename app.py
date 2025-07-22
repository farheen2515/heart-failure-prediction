from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load the trained model
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

@app.route('/', methods=['GET', 'POST'])
def home():
    prediction = None
    if request.method == 'POST':
        # Get form data (all features used in your RandomForestClassifier)
        features = [
            float(request.form['age']),
            float(request.form['anaemia']),
            float(request.form['creatinine_phosphokinase']),
            float(request.form['diabetes']),
            float(request.form['ejection_fraction']),
            float(request.form['high_blood_pressure']),
            float(request.form['platelets']),
            float(request.form['serum_creatinine']),
            float(request.form['serum_sodium']),
            float(request.form['sex']),
            float(request.form['smoking']),
            float(request.form['time'])
        ]
        
        # Make prediction
        pred = model.predict([features])[0]
        prediction = "Death Event" if pred == 1 else "Survived"

    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)