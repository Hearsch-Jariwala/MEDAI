import os
import streamlit as st
import openai

# OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Function to generate responses using OpenAI's text generation API
def generate_response(prompt):
    completions = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = completions.choices[0].text
    return message

# Chatbot UI using Streamlit
def chatbot():
    st.title("Chatbot for Cleaning Datasets")
    user_input = st.text_input("Ask a question related to cleaning datasets")

    if user_input:
        response = generate_response(user_input)
        st.success(response)

chatbot()
