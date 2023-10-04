import streamlit as st
import os
from os.path import isfile, join

st.title(' ⏳ Sandbox')

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
