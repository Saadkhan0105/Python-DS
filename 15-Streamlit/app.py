import streamlit as st
import pandas as pd
import numpy as np

## Title of the app
st.title("Hello Streamlit App")

## Displaying a simple text
st.write("Welcome to your first Streamlit app!")

## Creating a simple DataFrame
df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})


## Displaying the DataFrame
st.write("Here is a DataFrame:")
st.write(df)

## Creating a simple line chart
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c']
)
st.line_chart(chart_data)