import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
from styleformer import Styleformer
import torch
import webbrowser

st.set_page_config(
    page_title='Passiv/Activ converter',
    page_icon='📖'
)

selected = option_menu(
    menu_title=None,  # required
    options=["Active to Passiv", "Passiv to Active"],  # required
    icons=["book", "book"],  # optional
    menu_icon="cast",  # optional
    default_index=0,  # optional
    orientation="horizontal",
        )

if selected == "Active to Passiv":
    sf = Styleformer(style = 2) 
    st.title('Active Voice to Passive Voice Converter')
    st.write("Please enter your sentence in active voice")
    text = st.text_input('Entered Text:')
    if st.button('Convert'):
        target_sentence = sf.transfer(text)
        st.write(target_sentence)
    else:
        pass


if selected == "Passiv to Active":
    sf = Styleformer(style = 3) 
    st.title('Passive Voice to Active Voice Converter')
    st.write("Please enter your sentence in passive voice")
    text1 = st.text_input('Entered Text:')
    if st.button('Convert'):
        target_sentence1 = sf.transfer(text1)
        st.write(target_sentence1)
    else:
        pass

st.markdown("<h3 style='text-align: center; color: grey;'>Made with ❤ by Luwey Da Silva</h3>", unsafe_allow_html=True)

st.markdown("""<a style='display: block; text-align: center;' href="https://github.com/Luwey-Silva">Github</a>""", unsafe_allow_html=True,)


col1, col2, col3 , col4, col5 = st.columns(5)

with col1:
    pass
with col2:
    pass
with col4:
    pass
with col5:
    pass
with col3 :
    if st.button('Github octocat'):
         webbrowser.open_new_tab('https://github.com/Luwey-Silva')


# if st.button('Github'):
#         link = '[GitHub](http://github.com)'
        
    else:
        pass





