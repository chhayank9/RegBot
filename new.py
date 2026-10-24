import streamlit as st
st.title("Hello World")
st.header("My first streamlit")
name=st.text_input("Enter your name")
st.write(name)
if st.button("click me"):
    st.write("This button was clicked")
age=st.number_input("Enter your age")
age =st.slider("Select your age", 1, 100)
course =st.selectbox("Select your course", ["Python", "Java", "C++"]) 
agree=st.checkbox("I agree to the terms and conditions") 
gender=st.radio("Select your gender", ["Male", "Female", "Other"])  
question=st.text_area("Enter your question") 
upload=st.file_uploader("Upload your file", type=["docx", "png", "pdf"])
sidebar=st.sidebar.title("Sidebar")
st.sidebar.selectbox("Select your option", ["Python", "Java", "C++"])
col1,col2=st.columns(2)
with col1:
    st.write("This is column 1")    
    st.button("Button in column 1")
with col2:
    st.write("This is column 2")    
    st.button("Button in column 2")