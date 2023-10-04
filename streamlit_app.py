import streamlit as st
from os import listdir
from os.path import isfile, join

st.title(' ⏳ Sandbox')


files_list = [f for f in listdir(mypath) if isfile(join(mypath, f))]
st.write(files_list)
