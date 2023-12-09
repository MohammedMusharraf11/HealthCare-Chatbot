import streamlit as st
import datetime

def run_feedback_app():
    st.title("Feedback App")

    # User input for feedback
    feedback = st.text_area("Provide your feedback here:")

    # Submit button
    if st.button("Submit Feedback"):
        if feedback:
            # Append feedback to the 'feedback.txt' file
            with open('feedback.txt', 'a') as file:
                timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                file.write(f"{timestamp} - {feedback}\n")
            
            st.success("Thank you for your feedback!")

        else:
            st.warning("Please provide feedback before submitting.")
    st.write('____')
    st.write("Contact us at:" , 'iammusharraf11@gmail.com')
    st.write('                    https://wa.me/917975962858')