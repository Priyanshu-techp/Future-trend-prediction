# To run this file:
# streamlit run "Model_Deploying/app.py"
import streamlit as st
import pandas as pd
import numpy as np
import joblib

model = joblib.load('Model_Deploying/model.pkl')

df = pd.read_csv('Data/Cleanded_data.csv')
# UI Setup
st.title("E-Commerce Product Sales Predictor")
st.markdown("Predict product trend based on last month's sales")

# Sidebar inputs
with st.sidebar:
    st.header("Product Features")
    st.subheader("Categorical Features")

    stars = st.slider("star", 0.0, 5.0, 3.5, step=0.1)
    reviews = st.number_input("reviews", min_value=0, value=100)
    price = st.number_input("price", min_value=0.0, value=999.0)
    category = st.selectbox("categoryName", df['categoryName'].unique())
    product_name = st.selectbox('product_name', df['product_name'].unique())
    is_best_seller = st.radio("Best Seller", ['True', 'False'])

    def popularity(x):
        if x >= 0 and x < 2:
            return 'Not Popular'
        elif x >= 2 and x < 4:
            return 'Average Product'
        elif x >= 4 and x <= 5:
            return 'Popular Product'
        else:
            return 'unknown'
    product_popularity = popularity(stars)

    def cost_range(x):
        if x >= 99 and x < 5000:
            return 'Low cost '
        if x >= 5000 and x < 20000:
            return 'Low midrange cost'
        if x >= 20000 and x <= 40000:
            return 'Midrange cost'
        if x >= 40000 and x <= 50000:
            return 'Premium cost'
    Product_cost_range = cost_range(price)
    
    product_demand = st.selectbox('DemandOfTheProduct', df['DemandOfTheProduct'].unique())
    

input_dict = {
    'stars' : [stars],
    'reviews' : [reviews],
    'price' : [price],
    'categoryName' : [category],
    'product_name' : [product_name],
    'Product_popularity' : [product_popularity],
    'isBestSeller' : [is_best_seller],
    'Product_cost_range' : [Product_cost_range],
    'DemandOfTheProduct' : [product_demand],
}

input_df = pd.DataFrame(input_dict)
st.write(input_df)

if st.button("Predict Sales Trend", type="primary"):
    prediction = model.predict(input_df)
    if prediction[0] >= 400:
        st.success(f"Yes! Product is trending in future (Future sales is: {prediction[0]:,.0f} units)")
    elif prediction[0] >= 300:
        st.warning(f"Yes, product has potential (Sales is: {prediction[0]:,.0f} units)")
    else:
        st.error(f"No, Product is not trend in future (Expected sales only {prediction[0]:,.0f} units)")
