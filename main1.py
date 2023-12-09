import streamlit as st
from streamlit_option_menu import option_menu
import welcome
import info
import dependices

def app():
    with st.sidebar:
        selected = option_menu('Health Care chatbot',
                          
                          ['Welcome',
                           'Authentication',
                           'ChatBot',
                           'About'],
                          icons=['book','person-lock','robot' , 'info'],
                          default_index=0)
    
    if (selected == 'Welcome'):
        welcome.welcome_page()

    if (selected == 'About'):
        info.about_page()

    if (selected == 'Authentication'):
        dependices.app()


