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

Internal_Storage = st.selectbox('Internal Storage',[32,64,128,256,512,1024])

primary_camera = st.selectbox('Primary Camera',[5,8,12,16,32,48,50,108,200])

# secondary_camera = st.selectbox('Secondary Camera',[0,1])

# wifi = st.selectbox('Wifi',[0,1])

battery = st.selectbox('Battery Capacity In MAH',[2000,2500,3000,3500,4000,4250,4500,4750,5000,6000,7000])

# smartphone = st.selectbox('Smart Phone',[0,1])

# X_res = st.number_input("X_resolution")

# y_res = st.number_input("Y_resolution")

proce = st.selectbox('Processor Brand',df['Processor'].unique())

g = st.selectbox('5G',['Yes','No'])


if st.button('Pridict'):
    if g=='Yes':
        gg = 1
    else:
        gg = 0
    query = pd.DataFrame([[brand,color,1,display_size,os,processor_core,Internal_Storage,primary_camera,1,1,battery,1,2400,1080,proce,gg]],columns=['Brand','Color','Touchscreen','Display_size_inches','Operating System','Processor Core','Internal Storage','Primary Camera','Secondary Camera Available','Wi-Fi','Battery Capacity','SmartPhone','X_res','Y_res','Processor','5G'])
    # st.title(query)
    st.title(f"The Predicted Price RS:- {int(pipe.predict(query)[0])}")


