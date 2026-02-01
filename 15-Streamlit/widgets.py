import streamlit as st
import pandas as pd

st.title("Streamlit Text Input")

name = st.text_input("Enter your name:")

age = st.slider("Select your age:", 0, 100, 25)
st.write(f'You are {age} years old.')

options = ['Python', 'JavaScript', 'C++', 'Java', 'C#']
choice = st.selectbox("Select your favorite programming language:", options)
st.write(f'You selected: {choice}')

if name:
    st.write(f'Hello, {name}!')
    

data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [24, 30, 22],
    "City": ["New York", "Los Angeles", "Chicago"]
}
    
df = pd.DataFrame(data)
df.to_csv('sample_data.csv')
st.write(df)

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)