import pickle
import numpy as np
import streamlit as st
from sklearn.impute import SimpleImputer


st.title("Predict your house price")

#bds = st.number_input("Enter number of bedrooms",min_value=0,step=1)
bds = st.number_input("Enter number of bedrooms",min_value=0,step=1)
livs = st.slider("Enter the living area",min_value=25,max_value=2000,step=5)

pools_ = st.checkbox("Does it have swimming pool ?",value=False) 
pools_value = 1 if pools_ else 0

frshs_ = st.checkbox("It is fully furnished ?",value=False)
frshs_value = 1 if frshs_ else 0
constructionYear = st.number_input("Construction year",min_value=0,step=1)
numberoffacades = st.number_input("Facade number : ",min_value=0,step=1)
bathroomcount = st.number_input("How many bathrooms ? ",min_value=1,step=1)


with open('model.pkl', 'rb') as f:
    loaded_model = pickle.load(f)

new_data = np.array([[bds, pools_value, frshs_value, livs , constructionYear,numberoffacades,bathroomcount]])

imputer = SimpleImputer(strategy='mean')

imputed_data = imputer.fit_transform(new_data)

st.write("Your house predicted price is around : ",loaded_model.predict(imputed_data)[0],"$")