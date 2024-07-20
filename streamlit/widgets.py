import streamlit as st



st.title("HELLO SUDHIR")

name=st.text_input("Enter your name")
age=st.number_input("Enter your age")
clas=st.slider("Enter your class",1,12)
st.button("Submit")
options=[
    "Option 1",
    "Option 2",
    "Option 3"
]
st.selectbox("Choose option",options)
st.image("https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.pexels.com%2Fsearch%2Fflower%2F&psig=AOvVaw3Q6Z9Q6Q6Z9Q6")
st.write({clas})

if name:
    st.write(f"Hello {name}")
    
uploaded_file=st.file_uploader("Choose a file")
if uploaded_file:
    st.write(uploaded_file.getvalue())