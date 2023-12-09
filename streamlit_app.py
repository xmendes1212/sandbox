import streamlit as st
import os
from os.path import isfile, join

st.title(' ⏳ Sandbox')

with st.sidebar:
    st.markdown('''
    <img src="https://executive-education.minesparis.psl.eu/wp-content/themes/psl/images/logo-header.svg"
    ''', unsafe_allow_html=True)
    
st.subheader('os')
file_path = os.getcwd()
files_list = [f for f in os.listdir(file_path) if isfile(join(file_path, f))]
st.code('''
file_path = os.getcwd()
files_list = [f for f in os.listdir(file_path) if isfile(join(file_path, f))]
''')
st.write(files_list)


st.subheader('file selector')
def file_selector(folder_path='.'):
    filenames = os.listdir(folder_path)
    selected_filename = st.selectbox('Select a file', filenames)
    return os.path.join(folder_path, selected_filename)

filename = file_selector()
st.write('You selected `%s`' % filename)


# Pandas version
import pandas as pd

st.subheader('Pandas version')
st.write(pd.__version__)

# White space formatting
st.subheader('White space formatting')
st.text('''
8  ♖ ♘ ♚ ♙ ♘
7    ♚     ♙
6      ♖
5        ♙
4          ♙
3  ♘
2        ♚
1  ♖
   a b c d e 
''')
