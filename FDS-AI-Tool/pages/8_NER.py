import os
import spacy
import streamlit.components.v1 as components
from modules.classes import mongo_data


_RELEASE = False

# if not _RELEASE:
#     _component_func = components.declare_component(
#         "st_ner_annotate", url="http://localhost:5000")
# else:
# parent_dir = os.path.dirname(os.path.join(os.path.abspath(__file__), "../../.."))
# build_dir = os.path.join(parent_dir, "frontend/public")
# _component_func = components.declare_component(
#     "st_ner_annotate", path=build_dir)


# def st_ner_annotate(label, text, ents, key=None):
#     """st_edit_named_entities.

#     Parameters
#     ----------
#     text: str
#         Text to render
#     ents: object
#         Entities found in text
#     key: str or None
#         An optional key that uniquely identifies this component. If this is
#         None, and the component's arguments are changed, the component will
#         be re-mounted in the Streamlit frontend and lose its current state.

#     Returns
#     -------
#     object
#         Entities that have been selected
#     """
#     component_value = _component_func(
#         label=label, text=text, ents=ents, key=key, default=ents)

#     return component_value

def set_up():
    if "row_idx" not in st.session_state:
        st.session_state["row_idx"] = {}
    if "dataset" not in st.session_state:
        st.session_state["dataset"] = mongo_data.Dataset()

    if "default_dataset_idx" not in st.session_state:
        st.session_state["default_dataset_idx"] = 0

    return st.session_state["dataset"], st.session_state["default_dataset_idx"]

def update_slider_values():
    number = st.session_state["idx_number"]
    if 0 <= number < len(data[col_opt]):
        st.session_state["idx_slider"] = number

def update_number_values():
    slider = st.session_state["idx_slider"]
    if 0 <= slider < len(data[col_opt]):
        st.session_state["idx_number"] = slider



# app: `$ streamlit run my_component/__init__.py`
if not _RELEASE:
    import streamlit as st
    import sys
    sys.path.append("..")
    from modules import utils

    st.title("Named entity recognition demo")
    
    dataset, default_idx = set_up()
    
    data_opt = utils.dataset_opt(dataset.list_name(), default_idx)
    data = dataset.get_data(data_opt)
    row_idx = st.session_state["row_idx"].get(data_opt, 0)
    st.session_state["row_idx"][data_opt] = row_idx

    col1, col2 = st.columns([4, 6])
    cols = utils.get_categorical(data, add_hypen=True)
    cols.remove("-")
    if len(cols) == 0:
        st.header("No Categorical Data Found")
        st.stop()
    
    col_opt = col1.selectbox(
        "Choose Column",
        cols,
        key="display_col_opt"
    )

    row_idx = col2.slider(
        "Choose Index",
        0,
        len(data[col_opt]) - 1,
        st.session_state["row_idx"][data_opt],
        key="idx_slider",
        on_change=update_number_values
    )
    
    row_idx = st.number_input("Index", value=row_idx, disabled=False, key="idx_number", on_change=update_slider_values)
    
    

    data = dataset.get_data(data_opt)
    text = data[col_opt].to_list()[row_idx]
    nlp = spacy.load("en_core_web_sm")
    entity_labels = nlp.get_pipe('ner').labels

    # try:
    #     state = st.session_state["state"]
    #     ents = st.session_state["ents"]
    #     print("state: ", True)
    # except:
    #     st.session_state["state"] = True
    #     doc = nlp(text)
    #     ents = doc.to_json()['ents']

    #     current_entity_type = st.selectbox("Mark for Entity Type", entity_labels)
    #     entities = st_ner_annotate(current_entity_type, text, ents, key=42)
    #     st.session_state["ents"] = entities
    #     print("state: ", False)
    
    # current_entity_type = st.selectbox("Mark for Entity Type", entity_labels)
    # entities = st_ner_annotate(current_entity_type, text, ents, key=42)
    # st.session_state["ents"] = entities
    # st.json(entities)

    
    
    from text_highlighter import text_highlighter
    result = text_highlighter(
    text=text, labels=entity_labels
    )


    st.write(result)
