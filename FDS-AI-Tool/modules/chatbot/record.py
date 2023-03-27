# streamlit_audio_recorder by stefanrmmr (rs. analytics) - version January 2023

import streamlit as st

import os
import numpy as np
from io import BytesIO
import streamlit.components.v1 as components
import openai


def st_audiorec():

    # get parent directory relative to current directory
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    # Custom REACT-based component for recording client audio in browser
    build_dir = os.path.join(parent_dir, "st_audiorec/frontend/build")
    # specify directory and initialize st_audiorec object functionality
    st_audiorec = components.declare_component("st_audiorec", path=build_dir)

    # Create an instance of the component: STREAMLIT AUDIO RECORDER
    raw_audio_data = (
        st_audiorec()
    )  # raw_audio_data: stores all the data returned from the streamlit frontend
    wav_bytes = None  # wav_bytes: contains the recorded audio in .WAV format after conversion

    # the frontend returns raw audio data in the form of arraybuffer
    # (this arraybuffer is derived from web-media API WAV-blob data)

    if isinstance(raw_audio_data, dict):  # retrieve audio data
        with st.spinner("retrieving audio-recording..."):
            ind, raw_audio_data = zip(*raw_audio_data["arr"].items())
            ind = np.array(ind, dtype=int)  # convert to np array
            raw_audio_data = np.array(raw_audio_data)  # convert to np array
            sorted_ints = raw_audio_data[ind]
            stream = BytesIO(
                b"".join([int(v).to_bytes(1, "big") for v in sorted_ints])
            )
            # wav_bytes contains audio data in byte format, ready to be processed further
            wav_bytes = stream.read()
            st.session_state["new_audio_input"] = True

    return wav_bytes


# DESIGN implement changes to the standard streamlit UI/UX
# --> optional, not relevant for the functionality of the component!
# st.set_page_config(page_title="streamlit_audio_recorder")
# # Design move app further up and remove top padding
# st.markdown('''<style>.css-1egvi7u {margin-top: -3rem;}</style>''',
#             unsafe_allow_html=True)
# # Design change st.Audio to fixed height of 45 pixels
# st.markdown('''<style>.stAudio {height: 45px;}</style>''',
#             unsafe_allow_html=True)
# # Design change hyperlink href link color
# st.markdown('''<style>.css-v37k9u a {color: #ff4c4b;}</style>''',
#             unsafe_allow_html=True)  # darkmode
# st.markdown('''<style>.css-nlntq9 a {color: #ff4c4b;}</style>''',
#             unsafe_allow_html=True)  # lightmode


def transcribe():

    # TITLE and Creator information
    # st.title('streamlit audio recorder')
    # st.markdown('Implemented by '
    #     '[Stefan Rummer](https://www.linkedin.com/in/stefanrmmr/) - '
    #     'view project source code on '
    #     '[GitHub](https://github.com/stefanrmmr/streamlit_audio_recorder)')
    # st.write('\n\n')

    # TUTORIAL: How to use STREAMLIT AUDIO RECORDER?
    # by calling this function an instance of the audio recorder is created
    # once a recording is completed, audio data will be saved to wav_audio_data

    wav_audio_data = st_audiorec()  # tadaaaa! yes, that's it! :D

    # add some spacing and informative messages
    col_info, col_space = st.columns([0.57, 0.43])
    with col_info:
        st.write("\n")  # add vertical spacer
        st.write("\n")  # add vertical spacer
        # st.write('The .wav audio data, as received in the backend Python code,'
        #          ' will be displayed below this message as soon as it has'
        #          ' been processed. [This informative message is not part of'
        #          ' the audio recorder and can be removed easily] 🎈')

    if wav_audio_data is not None:
        # display audio data as received on the Python side
        with open("audio.wav", "wb") as f:
            f.write(wav_audio_data)
        data = open("audio.wav", "rb")
        if st.session_state["new_audio_input"]:
            text = openai.Audio.transcribe(file=data, model="whisper-1")
            st.session_state["new_audio_input"] = False
            return text["text"]
        # col_playback, col_space = st.columns([0.58,0.42])
        # with col_playback:
        #     st.audio(wav_audio_data, format='audio/wav')
    return None


if __name__ == "__main__":
    # call main function
    transcribe()
