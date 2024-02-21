import streamlit as st
import plotly_express as px
import pandas as pd

st.title("Hello Data Analyst!")
#df = px.data.gapminder()
#df = pd.read_csv("https://github.com/agung5114/PJJDA24/blob/main/sample_peserta.csv?raw=true")
df = pd.read_csv("sample_peserta.csv")
st.dataframe(df)

#fig = px.bar(df, y="pop", x="year",color="pop")
#st.write(fig)

#https://github.com/agung5114/PJJDA24