import streamlit as st
import google.generativeai as genai

# Cấu hình Gemini
# Lưu ý: Nếu bạn dùng Secrets, hãy giữ lại phần genai.configure... cũ của bạn
genai.configure(api_key=st.secrets["API_KEY"])
model = genai.GenerativeModel('gemini-1.5-flash')

# Giao diện
st.title("Chào mừng đến với Phố cổ Đồng Văn")
st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/Pho_co_Dong_Van.jpg/800px-Pho_co_Dong_Van.jpg", caption="Phố cổ Đồng Văn - Trái tim đá")

st.write("Hãy cùng trò chuyện về lịch sử nơi đây!")
