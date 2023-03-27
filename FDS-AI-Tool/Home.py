import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Home", initial_sidebar_state="auto")

try:
    dataset = st.session_state["dataset"]
    list_data = st.session_state["list_data"] + dataset.list()
except:
    st.session_state["list_data"] = ["-"]
    list_data = st.session_state["list_data"]

st.image("imgs/logo1.png", use_column_width=True)
st.title("Welcome to HAPI!")
st.subheader("Project: Human-AI Partnership Initiative (HAPI)")
st.markdown(
    """
	HAPI is a web app to help people to do some machine learning techniques 
	such as exploratory data, preprocessing and model building. The most interesting part
	about this app is that you can do all of those things **WITHOUT CODE**.
	"""
)

st.header("What Do We Have ?")
with st.expander(label = "Dataset"):
    st.markdown(
        """
		#### Read Dataset

		In this app, you can read multiple datasets from various sources. You can upload the dataset from your computer, 
		read the dataset from GitHub raw file URL (see [example](https://raw.githubusercontent.com/Hearsch-Jariwala/MEDAI/main/FDS-AI-Tool/sample_data/titanic.csv?token=GHSAT0AAAAAABYIGVRKYR3QZJSNN5AQJ6BAY6UHMOQ)), 
		and enter (or copy-paste) your dataset manually. We also provided some sample data in this app that you can use 
		in the *sample dataset* tab.

		#### Split Dataset

		When building a machine learning model, we usually need to split our dataset into training and test set (we also 
		need validation set sometimes). That's why we also provide a dataset splitter to deal with that problem.

		#### Download Dataset

		You can also download your dataset again after doing some preprocessing or data cleaning.
		"""
    )

with st.expander(label = "Exploratory Data"):
	st.markdown(
	"""

	Exploratory Data Analysis (EDA) is used to analyze the data to discover trends and patterns, so we can get a 
	better understanding of the bigger picture and insights into the data. EDA is often performed with the help 
	of several data visualization techniques.
        
	### Data Visualization
	
	In this app, we provide some data visualization techniques that you can use to explore the data i.e. Bar Plot, 
	Pie Plot, Count Plot, Histogram, Box Plot, Violin Plot, Scatter Plot, Regression Plot, and Line Plot.

	### Data Exploration
	
	You can also use the Statistics, Correlation, Duplicate, and Aggregation tab to explore your data.
	
	#### Display

	Display your dataset in the data frame structure, which is a 2-dimensional table of rows and columns much 
	like a spreadsheet.

	#### Information

	Every important information you need to know about your datasets such as total column, column name, a total 
	of non-null values, percentage of null values, total of unique values, column data type, and memory needed 
	to store your dataset.

	#### Statistics

	Descriptive statistics include those that summarize the central tendency, dispersion, and shape of a dataset's 
	distribution.

	#### Correlation

	Measure the size and direction of a relationship between two or more variables in your dataset. Here, you can 
	use 3 different methods to measure the correlation coefficient, i.e. Pearson, Kendall, and spearman. You can 
	also display the correlation value in a table, heatmap, and feature pair.

	#### Duplicate

	Check if there are duplicate data in your dataset.

	#### Group

	Group your data by variable(s) or column(s) and then apply the aggregate function.
	"""
)

with st.expander(label = "Power-BI dashboard"):
     st.markdown(
          "Titanic dataset analysis using Power BI"
	 )





with st.expander(label = "Feature Engineering"):
    st.markdown(
        """
		Feature engineering is a mandatory process to prepare input data that best fits the machine learning algorithms, 
		by selecting, manipulating, and transforming the most relevant features from existing data. It helps to represent 
		an underlying problem to predictive models in a better way, which as a result, improves the accuracy of the model 
		for unseen data.
		
		There are a few feature engineering techniques that you can use in this app:

		#### Add/Modify

		The first technique you can do is to add or modify a feature. We have provided some methods for you to do that, 
		i.e. using mathematical operations between features, extracting patterns from text, or grouping variable values.

		#### Change Data type

		Data is sometimes stored in the wrong type, therefore we need to change it first before further processing. 
		Reducing the bit length of a variable can also save more memory and speed up the training process. But we need 
		to be careful when doing this because we may lose information from that variable which results in lower accuracy.

		#### Imputation

		Imputation is the process to deal with missing values. You can fill in missing values in a variable with its 
		mean or median value (for numerical variable), with its mode (for categorical variable), or with a constant 
		value you choose.

		#### Encoding

		Machine learning models require all input to be numeric, hence we need to encode all categorical variables. 
		To do this, we have provided 3 feature encoding methods that are Ordinal Encoding, One-Hot Encoding, and 
		Target Encoding.

		#### Scaling

		Feature scaling is the process of scaling the values of features in a dataset so that they will be in the 
		same range of values. To do this, we have also provided 3 feature scaling methods that is Standard Scaling 
		(Standardization), Min-Max Scaling, and Robust Scaling

		#### Drop Column

		Finally, you can drop or remove unnecessary variables from your dataset before feeding the dataset into a 
		machine learning model.

		"""
    )


with st.expander(label="Pipeline"):
    st.markdown(
        """
		A pipeline is a linear sequence of data preparation, modeling, and prediction to codify and automate the workflow 
		it takes to produce a machine-learning model.
		
		In this app, we will only use pipelines in the preprocessing step. You can choose whether to add the feature 
		engineering process into the pipeline or not and then you can use the stored process in the pipeline to transform 
		other data with the same process sequentially.

		"""
    )

with st.expander(label="Model Building"):
    st.markdown(
        """
		After your dataset is ready, the next step is to build a machine learning model. And after building a model, we 
		can find out the performance of our model using metrics. There are some different metrics that we can use depending 
		on the problem we want to solve.
		
		In this app, currently, we only provide some classification algorithms. We will add more algorithms soon, including 
		other algorithms to handle the different tasks or problems e.g. regression and clustering.

		"""
    )
