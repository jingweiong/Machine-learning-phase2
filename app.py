import streamlit as st 

col1, col2 = st.columns([1, 4])  

with col1:
    st.image("Dell_logo_2016.svg.png", width=200)

with col2:
    st.title("Dell Global Business Center Sdn Bhd")
    
st.date_input("Transaction Date")
st.radio("Your department:",["Software Engineer","NPI","Test Engineer","Quality Engineer"])