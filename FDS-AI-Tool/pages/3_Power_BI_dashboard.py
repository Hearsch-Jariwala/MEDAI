import os

import openai
import streamlit as st
import streamlit.components.v1 as components
from modules.powerBI.insight import powerbi_dashboard

openai.api_key = os.getenv("OPENAI_API_KEY")

if __name__ == "__main__":
    powerbi_dashboard()
