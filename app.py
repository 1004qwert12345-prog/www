import streamlit as st

st.title("카운터 앱")
count = 0
if st.button("증가"):
    count = count +1 

stmarkdown(f"##혀ㄴ재숫자:'{count}'")
