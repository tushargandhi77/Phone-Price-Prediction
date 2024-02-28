import streamlit as st
import numpy as np
import pandas as pd
import pickle

pipe  = pickle.load(open('pipe.pkl','rb'))
df  = pickle.load(open('df.pkl','rb'))

st.title("Mobile Price Prediction")


brand = st.selectbox('Brand',df['Brand'].unique())

color = st.selectbox('color',df['Color'].unique())

# Touchscreen = st.selectbox('Touch Screen',[0,1])

display_size = st.number_input('Enter display Size')

os = st.selectbox('OS',df['Operating System'].unique())

processor_core = st.selectbox('Cores',df['Processor Core'].unique())

Internal_Storage = st.number_input('Internal Storage')

primary_camera = st.number_input('Primary Camera')

# secondary_camera = st.selectbox('Secondary Camera',[0,1])

# wifi = st.selectbox('Wifi',[0,1])

battery = st.number_input('Battery Capacity')

# smartphone = st.selectbox('Smart Phone',[0,1])

# X_res = st.number_input("X_resolution")

# y_res = st.number_input("Y_resolution")

proce = st.selectbox('Processor Brand',df['Processor'].unique())

g = st.selectbox('5G',[0,1])


if st.button('Pridict'):
    query = pd.DataFrame([[brand,color,1,display_size,os,processor_core,Internal_Storage,primary_camera,1,1,battery,1,2400,1080,proce,g]],columns=['Brand','Color','Touchscreen','Display_size_inches','Operating System','Processor Core','Internal Storage','Primary Camera','Secondary Camera Available','Wi-Fi','Battery Capacity','SmartPhone','X_res','Y_res','Processor','5G'])
    # st.title(query)
    st.title(int(pipe.predict(query)[0]))


