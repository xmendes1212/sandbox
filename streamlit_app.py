import streamlit as st
import os
from os.path import isfile, join

st.title(' ⏳ Sandbox')

file_path = os.getcwd()
files_list = [f for f in os.listdir(file_path) if isfile(join(file_path, f))]
st.write(files_list)
