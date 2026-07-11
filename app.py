import streamlit as st


name = st.text_input("이름", placeholder="이름")
class = st.radio("학년", ["1", "2","3"], horizontal=True)
ban = st.text_input("반", placeholder="반")

level = st.select_slider("난이도",options=["매우쉬움", "쉬움", "보통", "어려움", "지옥"],value="보통")
creativity = st.slider("점수", 0, 100, 50)

agree = st.text_area("소감", placeholder="소감")

if st.button("확인"):
    if agree:
        st.success(f"성공적으로 전송되었습니다! ({user_id}님)")
        st.markdown(f"""
        * **질문 내용:** {question}
        * **선택 모델:** `{ai_model}` | **말투:** `{tone}`
        * **활성화 기능:** {', '.join(features) if features else '없음'}
        * **창의성:** `{creativity}%` | **처리 속도:** `{ai_speed}`
        """)
        st.info("점수: 14세 미만 사용자이므로 보호자 모드가 활성화됩니다.")
        
    else:
        st.error("⚠️ 소감은 필수 항목입니다.")
