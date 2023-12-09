import streamlit as st
import os
from os.path import isfile, join

st.title(' ⏳ Sandbox')

with st.sidebar:
    st.markdown('''
    <img src="https://executive-education.minesparis.psl.eu/wp-content/themes/psl/images/logo-header.svg"
    ''', unsafe_allow_html=True)
