import os
import spacy
import streamlit.components.v1 as components

_RELEASE = False

if not _RELEASE:
    _component_func = components.declare_component(
        "st_ner_annotate", url="http://localhost:6006",
    )
else:
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(parent_dir, "frontend/public")
    _component_func = components.declare_component(
        "st_ner_annotate", path=build_dir)


def st_ner_annotate(label, text, ents, key=None):
    """st_edit_named_entities.

    Parameters
    ----------
    text: str
        Text to render
    ents: object
        Entities found in text
    key: str or None
        An optional key that uniquely identifies this component. If this is
        None, and the component's arguments are changed, the component will
        be re-mounted in the Streamlit frontend and lose its current state.

    Returns
    -------
    object
        Entities that have been selected
    """
    component_value = _component_func(
        label=label, text=text, ents=ents, key=key, default=ents)

    return component_value


# app: `$ streamlit run my_component/__init__.py`
if not _RELEASE:
    import streamlit as st
    import sys
    sys.path.append("..")
    from modules import utils

    st.title("Named entity recognition demo")
    try:
        dataset = st.session_state["dataset"]
        default_idx = st.session_state["default_dataset_idx"]

        data_opt = utils.dataset_opt(dataset.list_name(), default_idx)
        data = dataset.get_data(data_opt)

        col1, col2 = st.columns([4, 6])
        cols = utils.get_categorical(data, add_hypen=True)

        col_opt = col1.selectbox(
            "Choose Column",
            cols,
            default_idx,
            key="display_col_opt"
	    )

        idx = col2.slider(
            "Choose Index",
            0,
            len(data[col_opt]) - 1,
            0,
            key="display_idx"
        )

    except KeyError:
        st.header("No Dataset Found")
        st.stop()

    except Exception as e:
        st.write(e)
        st.stop()

    data = dataset.get_data(data_opt)
    text = data[col_opt].to_list()[idx]

    nlp = spacy.load("en_core_web_sm")
    entity_labels = nlp.get_pipe('ner').labels

    doc = nlp(text)
    ents = doc.to_json()['ents']

    current_entity_type = st.selectbox("Mark for Entity Type", entity_labels)
    entities = st_ner_annotate(current_entity_type, text, ents, key=42)
    st.json(entities)
