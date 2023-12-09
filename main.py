import streamlit as st
from streamlit_option_menu import option_menu
import welcome
import info
import dependices
import feedback

from dependices import session_state
st.set_page_config(page_title="Healthcare Bot", page_icon="👩‍⚕️", layout="centered", initial_sidebar_state="auto", menu_items=None)
with st.sidebar:
    selected = option_menu('Health Care Chatbot',
                          
                          ['Welcome',
                           'Authentication',
                           'ChatBot',
                           'Dibetic Prediction',
                           'About',
                           'Feedback'
                           ],
                          icons=['book','person-lock','robot' ,'magic', 'info', 'star'],
                          default_index=0)
    
if (selected == 'Welcome'):
    welcome.welcome_page()

if (selected == 'About'):
    info.about_page()

if (selected == 'Authentication'):
    dependices.app()

if (selected == 'ChatBot'):
    if session_state.is_authenticated:
        st.info("Welcome to the ChatBot!")
        import app5
        app5.run_chatbot()
    else:
        st.warning("Please log in to access the ChatBot.")
if (selected=='Feedback'):
    feedback.run_feedback_app()

if (selected=='Dibetic Prediction'):
    if session_state.is_authenticated:
        st.info("Welcome to Diabetic Prediction")
        import Diabetes
        Diabetes.run()
        st.warning("This is just a prediction!!. It is always better to consult a Doctor")
    else:
        st.warning("Please log in to access the Diabetic Prediction Feature")