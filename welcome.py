import streamlit as st

# Function to display the welcome page
def welcome_page():
    st.title("Welcome to HealthCare Chatbot")
    #st.image("🩺", width=100)  # Replace with the actual path to your icon image

    st.write("Hello! 👋 Welcome to our HealthCare Chatbot. Navigate your path to wellness with our interactive features.")

    # Briefly describe the features of the chatbot
    st.write("Explore the following features:")
    st.markdown("- Have a conversation with our intelligent chatbot.")
    st.markdown("- Schedule appointments with our healthcare professionals.")
    st.markdown("- Get personalized disease diagnosis recommendations.")
    st.markdown("- Predict the risk of diabetes.")

    # Encourage the user to log in for full access
    st.write("For the best experience, log in to access all features and enjoy a personalized healthcare journey.")
    login_button = st.button("Log In")

    if login_button:
        # You can add the login functionality here
        # Redirect the user to the authentication page or take any appropriate action
        st.write("Redirecting to login page...")


