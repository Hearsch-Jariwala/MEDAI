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
    st.write("Insights about the dataset:")

    completion = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content" : "You’re a Data analyst"},
        {"role": "user", "content": "Generate some insights on this https://community.powerbi.com/t5/Data-Stories-Gallery/Exploratory-Data-Analysis-of-the-Titanic-Dataset/m-p/2902210 Power BI dashboard"}
    ]
    )

    st.success(completion.choices[0].message.content)

powerbi_dashboard()
