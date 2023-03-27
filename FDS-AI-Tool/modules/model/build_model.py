import streamlit as st  

from modules import utils
from modules.model import classification
from modules.classes import model

def build_model(dataset, models):
	data_opt = dataset.list_name()
	default_idx = st.session_state["default_dataset_idx"]

	col1, col2, col3 = st.columns(3)
	train_name = col1.selectbox(
			"Train Data",
			data_opt,
			default_idx,
			key="model_train_data"
		)

	test_name = col2.selectbox(
			"Test Data",
			data_opt,
			default_idx,
			key="model_test_data"
		)

	train_data = dataset.get_data(train_name)
	target_var = col3.selectbox(
			"Target Variable",
			utils.get_variables(train_data),
			key="model_target_var"
		)

	classification.classification(dataset, models, train_name, test_name, target_var)


def model_chat(data, add_to_pipeline):
	dataset = st.session_state["dataset"]
	try:
		models = st.session_state["models"]

	except:
		st.session_state["models"] = model.Classification()
		models = st.session_state["models"]

	data_opt = dataset.list_name()
	default_idx = st.session_state["default_dataset_idx"]

	col1, col2, col3 = st.columns(3)
	train_name = col1.selectbox(
			"Train Data",
			data_opt,
			default_idx,
			key="model_train_data"
		)

	test_name = col2.selectbox(
			"Test Data",
			data_opt,
			default_idx,
			key="model_test_data"
		)

	train_data = dataset.get_data(train_name)
	target_var = col3.selectbox(
			"Target Variable",
			utils.get_variables(train_data),
			key="model_target_var"
		)

	classification.classification(dataset, models, train_name, test_name, target_var)

def model_chat_criteria(numerical, categorical, null, duplicate):
	return True