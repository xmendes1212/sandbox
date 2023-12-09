import streamlit as st
from streamlit_card import card
import base64



with open('bg-img.png', "rb") as f:
    data = f.read()
    encoded = base64.b64encode(data)
    
data = "data:image/png;base64," + encoded.decode("utf-8")


def card1():
    return card(
          title="Button 1",
          text="Some description",
          image=data,
          key='first'
        )

def card2():
    return card(
          title="Button 2",
          text="Some description",
          image=data,
          key='second'
        )


st.button('Button 1', on_click=card1)
st.button('Button 2', on_click=card2)


###############

if 'dummy_key' not in st.session_state:
    st.session_state.dummy_key = 0

def clicked_checkbox():
    st.session_state.dummy_key = 1

st.checkbox("dummy_name", on_click=clicked_checkbox)

st.write(st.session_state.dummy_key)



