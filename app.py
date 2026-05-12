import streamlit as st

st.title("Cloud PaaS demo")

st.write("Ứng dụng này được xây dựng bằng python và streamlit.")

name = st.text_input("Nguyễn Thế Anh")

if name:
    st.write(f"Xin chào {name}!")

st.subheader("Ý nghĩa cloud")

st.write("Khi triển khai lên streamlit cloud , ứng dungj này sẽ chạy trên nền tảng Paas")
