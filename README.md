#  ChatBot AI

A small chatbot I built with Python, Streamlit and the Groq API. You type a message, and an AI model answers in a chat window in your browser.

I made it as a practice project while studying AI at a technical school. The goal was to understand how a real chat app works under the hood: sending messages to a language model, keeping the conversation in memory, and handling things going wrong.

## What it does

- Chat with a language model (`openai/gpt-oss-20b` via Groq) right in the browser
- Remembers the whole conversation, so you can ask follow-up questions
- Uses a system prompt, so the bot answers in Polish, briefly and to the point
- Sidebar with a creativity (temperature) slider and a button to clear the chat
- Shows a readable error message instead of crashing when the API call fails

## Built with

Python, Streamlit, Groq API

## How to run it

1. Clone the repo and install the libraries:

   ```bash
   pip install -r requirements.txt
   ```

2. Create a free account at [console.groq.com](https://console.groq.com) and generate an API key.

3. Create a file called `.streamlit/secrets.toml` in the project folder and put your key in it:

   ```toml
   GROQ_API_KEY = "your_key_here"
   ```

4. Start the app:

   ```bash
   streamlit run main.py
   ```

## Screenshot

*(add a screenshot of the running app here)*

## What I learned

- How `st.session_state` keeps data between reruns of a Streamlit script
- How chat messages are structured for an LLM (`system`, `user`, `assistant` roles)
- Why API keys must stay out of the code and out of GitHub
- How to handle API errors without breaking the user experience

## A note on your API key

The key lives in `.streamlit/secrets.toml`, which is listed in `.gitignore`, so it never ends up in the repository. Never commit your own key.
