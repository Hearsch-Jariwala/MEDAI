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
    prompt = """The tool has the following functions inside each tab as shown below
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

Please answer the question in a step by step manner that can be followed using the functions mentioned above. For example:
Question: How can I fill in the missing values
Answer: 
1. 3a1 Exploratory Data tab, Statistics, Display, find the columns with null values
2. 4c, Feature Engineering tab, Imputation, impute the null values
Question:"""

    if user_input:
        response = generate_response(prompt + user_input)
        st.success(response)

chatbot()
