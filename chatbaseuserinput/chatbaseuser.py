import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage

# Streamlit 페이지 설정
st.set_page_config(page_title="🦜🔗 뭐든지 질문하세요~ ")
st.title('🦜🔗 뭐든지 질문하세요~ ')

# API 키 입력을 위한 입력창
api_key = st.text_input("OpenAI API Key를 입력하세요:", type="password")

def generate_response(input_text, api_key):  # LLM이 답변 생성
    llm = ChatOpenAI(
        temperature=0,  # 창의성 0으로 설정
        model_name='gpt-3.5-turbo',  # 모델명
        openai_api_key=api_key  # API 키 설정
    )
    messages = [HumanMessage(content=input_text)]  # 메시지 생성
    response = llm(messages)  # 모델 호출
    return response.content  # 응답 반환

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
