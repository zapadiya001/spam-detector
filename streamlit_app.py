# streamlit_app.py
import streamlit as st
from spam_detector import predict_spam

st.set_page_config(page_title="Spam Detector", page_icon="📩")

st.title("📩 Spam Detection App")
st.write("Enter a message to check if it's **spam** or **ham**.")

# Text input
user_input = st.text_area("Enter your message:")

# Predict button
if st.button("Check"):
    if user_input.strip() == "":
        st.warning("Please enter a message.")
    else:
        result = predict_spam(user_input)
        if result == "Spam":
            st.error("🚨 This message is SPAM.")
        else:
            st.success("✅ This message is HAM (not spam).")
