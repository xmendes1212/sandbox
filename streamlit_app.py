import streamlit as st
from streamlit_card import card
import base64

st.title(' ⏳ Sandbox')

with st.sidebar:
    st.markdown('''
    <img src="https://executive-education.minesparis.psl.eu/wp-content/themes/psl/images/logo-header.svg">
    ''', unsafe_allow_html=True)



with open('bg-img.png', "rb") as f:
    data = f.read()
    encoded = base64.b64encode(data)
data = "data:image/png;base64," + encoded.decode("utf-8")


hasClicked = card(
  title="Button 1",
  text="Some description",
  image=data,
  on_click=lambda: print('hi'),
  key='first'
)

hasClicked2 = card(
  title="Button 2",
  text="Some description",
  image=data,
  on_click=lambda: print('hi again'),
  key='second'
)
