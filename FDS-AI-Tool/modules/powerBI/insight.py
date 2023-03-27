import streamlit as st
import openai

def powerbi_dashboard(data = None, add_to_pipeline = False):

    st.header('Power BI dashboard')
    st.markdown(
    """
    <div style="text-align: left;">
        <iframe title="Report Section" width="600" height="400" src="https://app.powerbi.com/view?r=eyJrIjoiMDJmMzMxNjgtNThkZi00OTQ2LWIzODctMWJkMDc5YTAyY2VhIiwidCI6ImVmMmVhY2ZjLTZiYTctNDVjMy1iZDRjLTNkMThmYzAzMDUxZCIsImMiOjF9" frameborder="0" allowFullScreen="true"></iframe>
    </div>
    """,
    unsafe_allow_html=True
)

    st.header("Insights about the dataset:")

    completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content" : "You’re a Data analyst"},
        {"role": "user", "content": "Generate some insights on this https://community.powerbi.com/t5/Data-Stories-Gallery/Exploratory-Data-Analysis-of-the-Titanic-Dataset/m-p/2902210 Power BI dashboard"}
    ]
    )

    st.success(completion.choices[0].message.content)


def insight_criteria(numerical, categorical, null, duplicate):
    return True