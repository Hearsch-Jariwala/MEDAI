import os

import openai
import streamlit as st
import streamlit.components.v1 as components

openai.api_key = os.getenv("OPENAI_API_KEY")


def powerbi_dashboard():

    st.header('Power BI dashboard')
    st.markdown(
    """
    <div style="text-align: left;">
        <iframe title="Report Section" width="600" height="400" src="https://app.powerbi.com/view?r=eyJrIjoiMDJmMzMxNjgtNThkZi00OTQ2LWIzODctMWJkMDc5YTAyY2VhIiwidCI6ImVmMmVhY2ZjLTZiYTctNDVjMy1iZDRjLTNkMThmYzAzMDUxZCIsImMiOjF9" frameborder="0" allowFullScreen="true"></iframe>
    </div>
    """,
    unsafe_allow_html=True
)

    completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content" : "You’re a Data analyst"},
        {"role": "user", "content": "Give some insights on this https://app.powerbi.com/view?r=eyJrIjoiMDJmMzMxNjgtNThkZi00OTQ2LWIzODctMWJkMDc5YTAyY2VhIiwidCI6ImVmMmVhY2ZjLTZiYTctNDVjMy1iZDRjLTNkMThmYzAzMDUxZCIsImMiOjF9 Power BI dashboard."}
    ]
    )

    st.success(completion.choices[0].message.content)

powerbi_dashboard()
