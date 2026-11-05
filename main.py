import streamlit as st
from groq import Groq

MAX_HISTORY = 12
MODEL = "openai/gpt-oss-20b"

SYSTEM_PROMPT = {
    "role": "system",
    "content": (
        "Jesteś pomocnym asystentem AI. "
        "Odpowiadasz po polsku, krótko i konkretnie (maksymalnie kilka zdań). "
        "Nie wymyślasz faktów: jeśli czegoś nie wiesz, mówisz to wprost."
    ),
}

st.set_page_config(page_title="ChatBot AI", page_icon="")
st.title("ChatBot AI")
st.write("Porozmawiaj z modelem językowym.")

if "groq_client" not in st.session_state:
    st.session_state.groq_client = Groq(api_key=st.secrets["GROQ_API_KEY"])

if "messages" not in st.session_state:
    st.session_state.messages = [SYSTEM_PROMPT]

with st.sidebar:
    st.header("Ustawienia")
    creativity = st.slider("Kreatywność bota", 0.0, 2.0, 0.7, 0.1)
    if st.button("🗑️ Wyczyść rozmowę"):
        st.session_state.messages = [SYSTEM_PROMPT]
        st.rerun()

for msg in st.session_state.messages[-15:]:
    if msg["role"] != "system":
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

prompt = st.chat_input("Napisz wiadomość...")

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    try:
        client = st.session_state.groq_client
        with st.spinner("Bot myśli..."):
            response = client.chat.completions.create(
                model=MODEL,
                messages=st.session_state.messages,
                creativity=creativity,
            )
        odpowiedz = response.choices[0].message.content

        st.session_state.messages.append({"role": "assistant", "content": odpowiedz})
        with st.chat_message("assistant"):
            st.write(odpowiedz)

    except Exception as e:
        st.error(f"Coś poszło nie tak: {e}")