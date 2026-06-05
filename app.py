import streamlit as st
import google.generativeai as genai

# 1. Cấu hình Gemini AI
genai.configure(api_key="DÁN_API_KEY_CỦA_BẠN_VÀO_ĐÂY")
model = genai.GenerativeModel('gemini-1.5-flash')

# 2. Giao diện Web
st.title("Chào mừng đến với Phố cổ Đồng Văn")
st.image("pho_co_dong_van.jpg", caption="Phố cổ Đồng Văn - Trái tim đá")

st.write("Nhấn để nghe câu chuyện của chúng mình:")
st.audio("chuyen_pho_co.mp3")

# 3. Chat với AI
st.subheader("Hỏi người bạn Cao nguyên")
user_input = st.text_input("Bạn muốn hỏi gì về Phố cổ?")
if user_input:
    prompt = f"Bạn là hướng dẫn viên du lịch tại Phố cổ Đồng Văn. Hãy trả lời câu hỏi này: {user_input}"
    response = model.generate_content(prompt)
    st.write(response.text)