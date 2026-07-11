import streamlit as st


name = st.text_input("이름", placeholder="이름")
clas = st.radio("학년", ["1", "2","3"], horizontal=True)
ban = st.text_input("반", placeholder="반")

level = st.select_slider("난이도",options=["매우쉬움", "쉬움", "보통", "어려움", "지옥"],value="보통")
score = st.slider("점수", 0, 100, 50)

agree = st.text_area("소감", placeholder="소감")

if st.button("확인"):
    if agree:
        st.success(f"{name} / {clas}학년 / {ban}반 / {level}")
        st.markdown(f"점수: '{score}'")
        st.info(f"소감: {agree}")
        
    else:
        st.error("⚠️ 소감은 필수 항목입니다.")
