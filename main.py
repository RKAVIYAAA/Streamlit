import streamlit as st
from streamlit_option_menu import option_menu
st.title("Hello,kaviya")

# with st.sidebar:
#     st.header("suve")
# st.write(" ❤️kaviya shiva")
# st.text_input("enter your name")
# st.button("submit")
with st.sidebar:
    data=option_menu(
        menu_title="kavishiv",
        options=["login","about us","contact us"],
        icons=["house-fill","people","telephone-fill"]
    )
if data=="login":
    st.header("registration form")
    


    col1,col2=st.columns(2)
    with col1:
        name=st.text_input("enter your name")
        email=st.text_input("email")
    with col2:
        number=st.text_input("enter your number")
        phone_number=st.text_input("ph.no")
    if st.button("submit"):
      st.write(name,email,number,phone_number)
      st.success("data inserted successfully")
      st.ballooon()
    st.metric(label="python",value=20,delta="20%")
    st.number_input("interger",max_value=0)
    st.radio(label=":rainbow[Gender]",options=["M","F"])
    st.selectbox(label="city",options=["mdu","cbe","blore"])
    st.slider("number",0,100)
    st.file_uploader("upload")

elif data=="about us":
    st.header("about page")
elif data=="contact us":
    st.header("contact page")
    
