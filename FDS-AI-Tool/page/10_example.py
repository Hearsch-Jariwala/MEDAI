from st_on_hover_tabs import on_hover_tabs
from pathlib import Path
import streamlit as st
from modules.classes import mongo_data
from page import Dataset, ExploratoryData, FeatureEngineering, Pipeline, ModelBuilding, NER, Chatbot, About
st.set_page_config(page_title="Home")
st.header("Custom tab component for on-hover navigation bar")
styles = Path("../FDS-AI-Tool/frontend/public/styles.css")
st.markdown(
    "<style>" + open(styles).read() + "</style>",
    unsafe_allow_html=True,
)


dataset, default_idx = Chatbot.set_up()

with st.sidebar:
    tabs = on_hover_tabs(
        tabName=["Home", "Dataset", "Explore Data", "Feature Engineering", "Pipeline", "Model Building", "NER", "Chatbot"],
        iconName=["dashboard", "money", "economy", "work", "work", "work", "work", "work"],
        default_choice=0,
    )

if tabs == "Home":
    About.About()
elif tabs == "Dataset":
    Dataset.Dataset()

elif tabs == "Explore Data":
    ExploratoryData.Exploratory_Data()

elif tabs == "Feature Engineering":
    FeatureEngineering.Feature_Engineering()

elif tabs == "Pipeline":
    Pipeline.Pipeline()

elif tabs == "Model Building":
    ModelBuilding.ModelBuilding()

elif tabs == "NER":
    NER.NER()

elif tabs == "Chatbot":
    # Chatbot.Chat()
    st.write("Chatbot")
