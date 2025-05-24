# Loan Prediction System

A machine learning-powered web application that predicts loan approval status based on applicant information. This project uses various classification algorithms to determine whether a loan application should be approved or rejected.

## 🚀 Features

- **Web Interface**: User-friendly form to input loan application details  
- **Machine Learning Models**: Multiple algorithms including Logistic Regression, Random Forest, SVM, and K-Nearest Neighbors  
- **Real-time Predictions**: Instant loan approval/rejection predictions  
- **Data Visualization**: Comprehensive data analysis and visualization in Jupyter notebook  
- **Responsive Design**: Modern UI built with Tailwind CSS  

## 📊 Dataset

The project uses a loan dataset with the following features:

- **Gender**: Male/Female  
- **Married**: Yes/No  
- **Dependents**: Number of dependents (0, 1, 2, 3+)  
- **Education**: Graduate/Not Graduate  
- **Self_Employed**: Yes/No  
- **ApplicantIncome**: Applicant's income  
- **CoapplicantIncome**: Co-applicant's income  
- **LoanAmount**: Loan amount requested  
- **Loan_Amount_Term**: Term of loan in months  
- **Credit_History**: Credit history (0/1)  
- **Property_Area**: Urban/Semiurban/Rural  

## 🛠️ Installation

### Prerequisites

- Python 3.7 or higher  
- pip package manager  

### Setup Instructions

1. **Clone the repository**

   ```bash
   git clone <repository-url>
   cd "Loan Prediction"
2. **Create a virtual environment**
   ```bash
   python -m venv loan_prediction_env

   # On Windows
   loan_prediction_env\Scripts\activate
   
   # On macOS/Linux
   source loan_prediction_env/bin/activate
3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   
## 🚀 Usage
### Running the Web Application
1. **Start the Flask server**
   ```bash
   python app.py
2. **Open your browser and go to:**
   ```bash
   http://localhost:5000
3. **Fill out the loan application form and click "Predict" to see the result.**
### Running the Jupyter Notebook
1. **Start Jupyter Notebook**
   ```bash
   jupyter notebook
2. Open **loanPrediction.ipynb** and explore:
   
   - Data analysis and visualization
   - Feature engineering
   - Model training and evaluation
   - Performance comparison
     
## 📁 Project Structure
   ```bash
   Loan Prediction/
   ├── app.py                 # Flask web application
   ├── loanPrediction.ipynb   # Jupyter notebook with ML analysis
   ├── model.pkl              # Trained machine learning model
   ├── loan_status.csv        # Dataset
   ├── requirements.txt       # Python dependencies
   ├── README.md              # Project documentation
   └── templates/             # HTML templates
       ├── index.html         # Home page
       └── prediction.html    # Prediction form page
```
## 🤖 Machine Learning Models
The project implements and compares multiple classification algorithms:

1. **Logistic Regression**
   - Accuracy: ~80%
   - Good baseline model with interpretable results

2. **Random Forest Classifier**
   - Accuracy: ~81%
   - Best performing model (saved as model.pkl)
   - Handles feature interactions well

3. **Support Vector Machine (SVM)**
   - Accuracy: ~79%
   - Linear kernel with feature scaling

4. **K-Nearest Neighbors (KNN)**
   - Accuracy: ~76%
   - Simple distance-based classification
  
## 📈 Model Performance
The Random Forest Classifier was selected as the final model based on:
   - Highest accuracy on test data
   - Good generalization performance
   - Robustness to outliers and missing values
     
### 🔧 Technical Details
#### Data Preprocessing
   - Missing value imputation using median/mode
   - Feature encoding for categorical variables
   - Log transformation for skewed numerical features
   - Feature scaling using StandardScaler

## Feature Engineering
   - Created Total_Income by combining applicant and co-applicant income
   - One-hot encoding for categorical variables
   - Log transformations with np.log1p()
   - Handled missing values appropriately

### 🌐 Web Interface
The web application includes:
- Home page with project introduction
- Prediction form with input validation
- Results page showing approval/rejection status
- Responsive design for mobile and desktop

### 📋 API Endpoints
- GET / - Home page
- POST /predict - Loan prediction endpoint

### 🤝 Contributing
- Fork the repository
- Create a feature branch (git checkout -b feature/AmazingFeature)
- Commit your changes (git commit -m 'Add some AmazingFeature'
- Push to the branch (git push origin feature/AmazingFeature)
- Open a Pull Request

### 📄 License
This project is licensed under the MIT License - see the LICENSE file for details.

### 🙏 Acknowledgments
- Dataset source: [Loan Prediction Dataset]
- Built with Flask, scikit-learn, and Tailwind CSS

### 📞 Contact
For questions or suggestions, please open an issue in the repository
