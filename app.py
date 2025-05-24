from flask import Flask, render_template, request
import pickle
import os
import numpy as np

app = Flask(__name__)

# Load the trained model with error handling
try:
    if os.path.exists('model.pkl'):
        model = pickle.load(open('model.pkl', 'rb'))
        print("Model loaded successfully!")
    else:
        model = None
        print("Warning: model.pkl not found!")
except Exception as e:
    model = None
    print(f"Error loading model: {e}")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        try:
            # Check if model is loaded
            if model is None:
                return render_template('result.html', prediction_text='Error: Model not available. Please ensure model.pkl exists.')
            # Get the input values from the form
            gender = request.form['gender']
            married = request.form['married']
            dependents = request.form['dependents']
            education = request.form['education']
            self_employed = request.form['self_employed']
            applicant_income = float(request.form['applicant_income'])
            coapplicant_income = float(request.form['coapplicant_income'])
            loan_amount = float(request.form['loan_amount'])
            loan_amount_term = float(request.form['loan_amount_term'])
            credit_history = float(request.form['credit_history'])
            property_area = request.form['property_area']

            # Preprocess the input values
            if gender == 'Male':
                gender = 1
            else:
                gender = 0

            if married == 'Yes':
                married = 1
            else:
                married = 0

            if dependents == '0':
                dependents = 0
            elif dependents == '1':
                dependents = 1
            elif dependents == '2':
                dependents = 2
            else:
                dependents = 3

            if education == 'Graduate':
                education = 1
            else:
                education = 0

            if self_employed == 'Yes':
                self_employed = 1
            else:
                self_employed = 0

            # First calculate Total_Income from original values
            total_income = applicant_income + coapplicant_income

            # Apply log1p transformation to all income features (matching notebook preprocessing)
            applicant_income = np.log1p(applicant_income)
            coapplicant_income = np.log1p(coapplicant_income)
            loan_amount = np.log1p(loan_amount)
            total_income = np.log1p(total_income)

            # One-hot encode dependents (1, 2, 3+)
            dep_1 = 1 if dependents == 1 else 0
            dep_2 = 1 if dependents == 2 else 0
            dep_3_plus = 1 if dependents == 3 else 0

            # One-hot encode property area (Semiurban, Urban) - Rural is baseline (0,0)
            semiurban = 1 if property_area == 'Semiurban' else 0
            urban = 1 if property_area == 'Urban' else 0

            # Make the prediction with all 15 features in correct order
            prediction = model.predict([[gender, married, education, self_employed, applicant_income,
                                        coapplicant_income, loan_amount, loan_amount_term, credit_history,
                                        total_income, dep_1, dep_2, dep_3_plus, semiurban, urban]])

            # Render the prediction result
            if prediction[0] == 1:
                return render_template('result.html', prediction_text='Congratulations! You are eligible for a loan.')
            else:
                return render_template('result.html', prediction_text='Sorry, you are not eligible for a loan.')

        except Exception as e:
            return render_template('result.html', prediction_text=f'Error: {str(e)}')

    else:
        return render_template('prediction.html')

if __name__ == '__main__':
    app.run(debug=True)

