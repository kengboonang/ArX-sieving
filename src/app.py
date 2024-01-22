import streamlit as st
from streamlit_chat import message
import subprocess
import os

# Setting page description
st.set_page_config(page_title="ArX-sieving app", page_icon=":smiley:")
st.markdown("<h1 style='text-align: center; color: white;'>How may I ArX-serve you today?</h1>", unsafe_allow_html=True)
st.divider()
st.markdown("<h3 style='text-align: center; color: white;'>ArX-sieving aims to serve as an LLM assistant to help with finding relevant papers from ArXiv and to provide information in a conversational manner.</h3>", unsafe_allow_html=True)
st.divider()

if "generated" not in st.session_state:
    st.session_state.generated = []
if "past_queries" not in st.session_state:
    st.session_state.past_queries = []

# Setting up the sidebar
st.sidebar.title("ArX-sieving")
counter_placeholder = st.sidebar.empty()
with st.sidebar:
    st.markdown("<h3 style='text-align: center; color: white;'>Ask me anything you need help with</h3>", unsafe_allow_html=True)
    clear_button = st.button("Clear history")

if clear_button:
    st.session_state.generated = []
    st.session_state.past_queries = []
    counter_placeholder.empty()

response_container = st.container()

if query := st.chat_input("Ask away!", key="query"):
    st.session_state.past_queries.append(query)

    with response_container:
        for i in range(len(st.session_state.past_queries)):
            message(st.session_state.past_queries[i], "user")
    