import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
# app.py
import streamlit as st
st.title("StudyAI - Chemistry & Physics Helper")

user_input = st.text_input("Ask me a question about physics or chemistry:")
if user_input:
    st.write("Here's your answer!")
        # improve your study