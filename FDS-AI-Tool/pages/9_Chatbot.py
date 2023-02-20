import os
import re
import streamlit as st
import openai
from modules.classes import mongo_data
from modules import utils


# OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

def set_up():
    if "row_idx" not in st.session_state:
        st.session_state["row_idx"] = {}
    if "dataset" not in st.session_state:
        st.session_state["dataset"] = mongo_data.Dataset()

    if "default_dataset_idx" not in st.session_state:
        st.session_state["default_dataset_idx"] = 0

    return st.session_state["dataset"], st.session_state["default_dataset_idx"]


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
def chatbot(dataset_info, numerical_cols, categorical_cols, null_cols, has_duplicate):
    st.title("Chatbot for Cleaning Datasets")
    user_input = st.text_input("Ask a question related to cleaning datasets")
    tool_info = '''
        1. Home tab: A brief description of the functionality of the tool
        2. Dataset tab: Operations regarding I/O of datasets
        a. Dataset List: list the dataset name of existing datasets, and let the user select the default dataset for other operations. Users can also delete datasets here.
        b*. Read Dataset: Users can load the dataset to the tool, by uploading from the local machine, loading from GitHub URL, manually inputting, or trying with a sample dataset.
        c*. Split Dataset: Users can split the dataset into different datasets, e.g., train set and test set. Users can also specify the percentage of the test set and the random state of the split.
        d*. Download Dataset: Users can display the data, set the download name, set the download parameter such as including the header and index here, and download the dataset here.
        3. Exploratory Data tab: Explore the dataset by graphs and statistics of the dataset
        a. Statistics
        a1. Display: Users can display the dataset to see the exact content of the dataset, display the information of the dataset such as null value, unique value and data type by column, and calculate the statistics such as count, mean, standard deviation by column
        a2. Correlation: Calculate the correlation between each column
        a3*. Duplicate: Find duplicate rows and delete them
        a4. Aggregation: Perform aggregation functions by selected column values
        b. Graph
        b1. bar plot
        b2. Pie Plot
        b3. Count Plot
        b4. Histogram
        b5. Box Plot
        b6. Violin Plot
        b7. Scatter Plot
        b8. Reg Plot
        b9. Line Plot
        4. Feature Engineering tab: Operations regarding feature engineers
        a*. Add/Modify: Operations between one or several columns and the result will form a new column, the operations could be math operation, extract text by regular expression, group by categorical or group by numerical
        b*. Change Data type: change data type for numerical data, e.g. float to integer
        c*. Imputation: impute null value with chosen strategy, e.g. mean for numerical data, mode for categorical data
        d*. Encoding: encode the value of chosen column, method could be ordinal, one-hot, target
        e*. Scaling: scale the chosen column, methods could be standard, min-max, robust
        f*. Drop column: drop the chosen column
        5*. Pipeline tab: operations performed in feature engineering tab could be added to pipeline, so that all the setting will be memorized and could be easily performed in the future
        6. Model Building: Build model with chosen dataset
        a*. Build Model: User can choose dataset, choose model from KNN, SVM, Logistic Regression, Decision Tree, Random Forest, or MLP
        b. Model Report: shows the metrics of the model on test set
        c*. Model Prediction: Use trained model to make prediction on other dataset
        d*. Delete Model: delete the chosen model
        7*. Named Entity Recognition tab: User can label the named entity in the dataset

        The function of prefixes containing * is operational, while the others are demonstrative.
    '''
    sample_answers_with_null = f'''
        Question: How can I clean the dataset
        Answer:
        1. <4c> Feature Engineering tab, Imputation, impute the null values, which are {null_cols}
        2. <4d> Feature Engineering tab, Encoding, encode the categorical columns, which are {categorical_cols}
        3. <4e> Feature Engineering tab, Scaling, scale the numerical columns, which are {numerical_cols}
        ''' if null_cols != 'No' else " "
    
    sample_answers_with_duplicate = f'''
        Question: How can I clean the dataset
        Answer:
        1. <3a3> Exploratory Data tab, Statistics, Duplicate, find the duplicate rows
        2. <4d> Feature Engineering tab, Encoding, encode the categorical columns, which are {categorical_cols}
        3. <4e> Feature Engineering tab, Scaling, scale the numerical columns, which are {numerical_cols}
        ''' if has_duplicate == "has" else " "

    
    sample_questions = f'''
        Question: How can I fill in the missing values
        Answer:
        1. <3a1> Exploratory Data tab, Statistics, Display, find the columns with null values
        2. <4c> Feature Engineering tab, Imputation, impute the null values
        
        Question: How can I find the correlation between columns
        Answer:
        1. <3a2> Exploratory Data tab, Statistics, Correlation, find the correlation between columns

        Question: How can I find the duplicate rows
        Answer:
        1. <3a3> Exploratory Data tab, Statistics, Duplicate, find the duplicate rows

        {sample_answers_with_null}

        {sample_answers_with_duplicate}
        '''
    

    prompt = f"""
        Tool information: {tool_info}
        
        Dataset information: {dataset_info}

        Please answer the question in a step by step manner that can be followed using the functions mentioned above. For example:
        {sample_questions}
        Question: """

    print(prompt)
    if user_input:
        response = generate_response(prompt + user_input)
        tags = re.findall(r'<(.*?)>', response)
        print(tags)
        # remove all the tags in the response
        response = re.sub(r'<(.*?)>', '', response)

        
        st.success(response)

dataset, default_idx = set_up()
data_opt = utils.dataset_opt(dataset.list_name(), default_idx)
data = dataset.get_data(data_opt)
rows, cols = data.shape
columns = ", ".join(data.columns.tolist())
numerical_cols = ", ".join(data.select_dtypes(include=['int64', 'float64']).columns.tolist()) if data.select_dtypes(include=['int64', 'float64']).columns.tolist() else "none"
categorical_cols = ", ".join(data.select_dtypes(include=['object']).columns.tolist()) if data.select_dtypes(include=['object']).columns.tolist() else "none"
null_cols = ", ".join(data.columns[data.isnull().any()].tolist()) if data.isnull().any().any() else "No"
has_duplicates = "has" if data.duplicated().any() else "has no"

dataset_info = f'''
                The dataset contains {rows} rows and {cols} columns. The columns are {columns}.
                Among the columns, {numerical_cols} are numerical columns and {categorical_cols} are categorical columns.
                Categorical columns should be encoded before training the model.
                Numerical columns should be scaled before training the model.
                Columns with null values should be imputed or deleted before training the model, {null_cols} columns have null values.
                Duplicated rows should be removed before training the model, otherwise, no actions for duplicate rows. The dataset {has_duplicates} duplicated rows.
                '''

chatbot(dataset_info, numerical_cols, categorical_cols, null_cols, has_duplicates)
