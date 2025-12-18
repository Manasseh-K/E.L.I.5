import streamlit as st
from dotenv import load_dotenv
import os
from eli_prompt import build_eli5_prompt
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.set_page_config(page_title="ELI5 Bot", page_icon="🧃")

st.title("Explain It Like I'm Five 🧃")
st.write("Because some explanations forget what humans are.")

topic = st.text_area("What do you want explained?")
level = st.selectbox("Explain it like I'm…", ["5", "10", "15", "college"])

if st.button("Explain"):
    if not topic.strip():
        st.warning("Give me something to explain.")
    else:
        prompt = build_eli5_prompt(topic, level)

        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[{"role": "user", "content": prompt}],
        )

        st.subheader("Explanation")
        st.write(response.choices[0].message.content)