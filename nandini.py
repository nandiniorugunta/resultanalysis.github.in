import streamlit as st
import pandas as pd
st.title("JNTUACEK")
st.header("College of Engineering")
st.text_input("enter ur email")
uploaded_file=st.file_uploader("upload ur file")
if uploaded_file is not None:
    file_contents=uploaded_file.read()
    st.write(file_contents)
st.sidebar.title("result analysis")
excel_file='marks.xlsx'
sheet_name='Book1'
df=pd.read_excel(excel_file,sheet_name=sheet_name)
st.dataframe(df)
if st.sidebar.button("greater than 80"):
    d=df.loc[df['per']>80]
    st.sidebar.write("count:",len(d))
if st.sidebar.button("Bet 60 and 80"):
    e=df.loc[(df['per']>60)&(df['per']<80)]
    st.sidebar.write("count:",len(e))
if st.sidebar.button("<60"):
    f=df.loc[df['per']<60]
    st.sidebar.write("count:",len(f))
    