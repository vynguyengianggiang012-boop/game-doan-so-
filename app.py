import streamlit as st
import random

st.set_page_config(page_title="Game Đoán Số", page_icon="🎮")
st.title("🎮 Trò chơi Đoán Số Bí Ẩn")

if "secret_number" not in st.session_state:
    st.session_state.secret_number = random.randint(1, 100)
    st.session_state.attempts = 0
    st.session_state.game_over = False

st.write("Hệ thống đã chọn một số ngẫu nhiên từ **1 đến 100**. Hãy thử tài đoán số!")

with st.form(key="guess_form"):
    user_guess = st.number_input("Nhập số bạn đoán:", min_value=1, max_value=100, step=1)
    submit_button = st.form_submit_button(label="Đoán số")

if submit_button and not st.session_state.game_over:
    st.session_state.attempts += 1
    if user_guess < st.session_state.secret_number:
        st.warning(f"Số {user_guess} quá THẤP! Thử lại xem.")
    elif user_guess > st.session_state.secret_number:
        st.warning(f"Số {user_guess} quá CAO! Thử lại xem.")
    else:
        st.success(f"🎉 Xuất sắc! Bạn đã đoán đúng số {st.session_state.secret_number} sau {st.session_state.attempts} lượt đoán.")
        st.session_state.game_over = True

if st.session_state.game_over:
    if st.button("Chơi lại vòng mới"):
        st.session_state.secret_number = random.randint(1, 100)
        st.session_state.attempts = 0
        st.session_state.game_over = False
        st.rerun()
