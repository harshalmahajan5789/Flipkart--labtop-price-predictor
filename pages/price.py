import streamlit as st
import pandas as pd
import os
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import OrdinalEncoder
from sklearn.model_selection import train_test_split

#Page Heading
st.header(":blue[Laptop Price Prediction]")

#resoures path
FILE_DIR1 = os.path.dirname(os.path.abspath(__file__))
FILE_DIR = os.path.join(FILE_DIR1,os.pardir)
dir_of_interest = os.path.join(FILE_DIR, "resources")
DATA_PATH = os.path.join(dir_of_interest, "data")

#Load data
DATA_PATH1=os.path.join(DATA_PATH, "laptop_price.csv")
df=pd.read_csv(DATA_PATH1)
X = df.drop('MRP', axis=1)
y = df['MRP']
oe = OrdinalEncoder(categories = [['128GB', '256GB','512GB','1TB','2TB'],['4GB','8GB','16GB','32GB']])
preprocessor = ColumnTransformer(
    [
        ('oh', OneHotEncoder(sparse=False), ["Brand","OS","Processor", "RAM_Type","Storage_type"]),
        ('Ordinal Encoder', oe, ['Storage_Size','RAM_Size'])
    ],
    remainder='passthrough'
)
X_pr = preprocessor.fit_transform(X)
grb= GradientBoostingRegressor(n_estimators =100,random_state =0) 
grb.fit(X_pr, y) 


#Accepting the required features from user
col1, col2, col3= st.columns(3)
with col1:
    brand = st.selectbox(
        ':blue[Select Laptop Brand]',
        (df.Brand.unique()))
    st.write('Your Selected Brand:', brand)

with col2:
    operating_system=st.selectbox(
        ':blue[Select Operating System]',
        (df['OS'].unique()))
    st.write('Your Selected Operating System:', operating_system)

with col3:
    processor=st.selectbox(
        ':blue[Select Processor Type]',
        (df['Processor'].unique()))
    st.write('Your Selected Processor Type:', processor)

col1, col2= st.columns(2)
with col1:
    ram_size=st.selectbox(
        ':blue[Select RAM Size]',
        (df['RAM_Size'].unique()))
    st.write('Your Selected RAM Size:', ram_size)

with col2:
    ram_type=st.selectbox(
        ':blue[Select RAM Type]',
        (df['RAM_Type'].unique()))
    st.write('Your Selected RAM Type:', ram_type)

col1, col2= st.columns(2)
with col1:
    storage_size=st.selectbox(
        ':blue[Select Storage Size]',
        (df['Storage_Size'].unique()))
    st.write('Your Selected Storage Size:', storage_size)

with col2:
    storage_type=st.selectbox(
        ':blue[Select Storage Type]',
        (df['Storage_type'].unique()))
    st.write('Your Selected Storage Type:', storage_type)  

#Create dataframe using all these values
X_test=pd.DataFrame({"Brand":[brand],"OS":[operating_system], "Processor":[processor],
                   "RAM_Size":[ram_size], "RAM_Type":[ram_type],
                   "Storage_Size":[storage_size], "Storage_type":[storage_type]})

X_test_pr = preprocessor.transform(X_test)
if st.button('Predict'):
    price=grb.predict(X_test_pr)
    price=price[0].round(2)    
    st.subheader(":blue[Laptop Price For Your Selected Feature :] :blue[{}]".format("₹"+str(price)))
else:
    pass



    














