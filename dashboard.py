import streamlit as st
import pandas as pd
import numpy as np

st.header("2024 AHI 507 Streamlit Example")
st.subheader("We will go through a few examples of loading and visualizing info into this dashboard")
st.text("In this streamlit dash we will focus on recently released school learning mods from the NCES from 2020-2021")



# ## https://healthdata.gov/National/School-Learning-Modalities-2020-2021/a8v3-a3m3/about_data
df = pd.read_csv("https://healthdata.gov/resource/a8v3-a3m3.csv?$limit=50000") ## first 1k

## data cleaning
df['week_recoded'] = pd.to_datetime(df['week'])
df['zip_code'] = df['zip_code'].astype(str)

df['week'].value_counts()


## box to show how many rows and columns of data we have 155
col1, col2, col3 = st.columns(3)
col1.metric("Columns", df.shape[1])
col2.metric("Rows", len(df))
col3.metric('Number of unique districts:', df['district_name'].nunique())
## exposing first 1k of data 
st.dataframe(df)


table = pd.pivot_table(df, values='student_count', index=['week'],
                       columns=['learning_modality'], aggfunc="sum")


## line chart by week                       
st.bar_chart(
    df,
    x="week",
    y="student_count",
    color="learning_modality",  # Optional
)

