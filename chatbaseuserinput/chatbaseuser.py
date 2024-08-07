import streamlit as st
import openai

# Streamlit 페이지 설정
st.set_page_config(page_title="🦜🔗 뭐든지 질문하세요~ ")
st.title('🦜🔗 뭐든지 질문하세요~ ')

# API 키 입력을 위한 입력창
api_key = st.text_input("OpenAI API Key를 입력하세요:", type="password")

def generate_response(input_text, api_key):  # LLM이 답변 생성
    openai.api_key = api_key  # API 키 설정
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": input_text}
        ]
    )
    return response.choices[0].message['content']  # 응답 반환

if api_key:
    # Streamlit 폼 사용
    with st.form('Question'):
        text = st.text_area('질문 입력:', '')  # 첫 페이지가 실행될 때 보여줄 질문
        submitted = st.form_submit_button('보내기')
        if submitted:
            response = generate_response(text, api_key)  # 폼 제출 시 응답 생성
            st.info(response)  # 응답 출력
else:
    st.warning("API 키를 입력해주세요.")
