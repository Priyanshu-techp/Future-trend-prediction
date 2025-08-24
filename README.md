# Predicting Future Trends for E-Commerce Products

# Project Overview
This project analyzes Amazon product sales data to predict future product trends using machine learning. It helps identify which products are likely to be in demand next month based on historical sales data.

# Problem Statement
E-commerce companies often struggle to forecast which products will trend next. This project uses past sales data to build a model that predicts future trends and helps in inventory planning and marketing strategies.

# Dataset
- Dataset: Amazon sales data
- Fields include: ASIN, Title, Category, Price, Ratings, Reviews, boughtInLastMonth, etc.
- Target Column: `Bought in last month`

# Technologies Used
- Python
- Pandas, NumPy
- Scikit-learn
- Matplotlib, Seaborn
- Joblib (for model saving)
- Streamlit (for web app)

# Model Used
- Linear Regression
- Decision Tree Regressor
- Random Forest Regressor
- XGB Regressor
- Gradient Boosting Regressor
- Accuracy, F1-Score, Confusion Matrix used for evaluation

# Folder Structure

Predict future trend for E-Commerce/
├── Data/
│   ├── Amazone_sales_data.csv
│   └── Cleanded_data.csv
│
├── Model_Deploying/
│   ├── app.py
│   ├── cat_encoder.pkl
│   ├── columns.pkl  
│   ├── cost_encoder.pkl
│   ├── dem_encoder.pkl
│   ├── GB_regressor.pkl
│   ├── pop_encoder.pkl
│   └── scaler.pkl
│
├── Notebooks/
│   ├── Cleaning.ipynb
│   └── Model_evaluation.ipynb
│ 
├── .gitignore
├── requirements.txt
└── README.md


# How to Run
1. Clone the repo:
   `git clone https://github.com/PriyanshPandey/Predict future trend for E-Commerce.git`

2. Navigate to folder:
   `cd Predict future trend for E-Commerce `

3. Install dependencies:
   `pip install -r requirements.txt`

4. Run the app:
   `streamlit run app.py`

# Deploy link:
[Streamlit](https://future-trend-prediction.streamlit.app/)

# Author
- Name: Priyanshu Pandey
- Diploma in Automation & Robotics, Govt. Polytechnic Dawahat (Almora)
- LinkedIn: [linkedin.com/in/yourprofile](https://www.linkedin.com/in/priyanshu-pandey67)
