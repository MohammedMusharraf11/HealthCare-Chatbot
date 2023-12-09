import streamlit as st
import streamlit_authenticator as stauth
import datetime
import re
from deta import Deta
import main1

DETA_KEY = 'd04nyffhm82_xhmNoMKMDZsw23o5kLJ6jU6K8E5schfy'

deta = Deta(DETA_KEY)

db = deta.Base('Streamlit')

class SessionState:
    def __init__(self):
        self.is_authenticated = False

# Create a session state object
session_state = SessionState()


def app():
    st.title("Login Authentication")
    def insert_user(email, username, password):
        """
    Inserts Users into the DB
    :param email:
    :param username:
    :param password:
    :return User Upon successful Creation:
    """
        date_joined = str(datetime.datetime.now())

        return db.put({'key': email, 'username': username, 'password': password, 'date_joined': date_joined})


    insert_user("mush@gmail.com" , "Musharraf" , "1234")

    def fetch_users():
        """
    Fetch Users
    :return Dictionary of Users:
    """
        users = db.fetch()
        return users.items


    def get_user_emails():
        """
    Fetch User Emails
    :return List of user emails:
        """
        users = db.fetch()
        emails = []
        for user in users.items:
            emails.append(user['key'])
        return emails


    def get_usernames():
        """
    Fetch Usernames
    :return List of user usernames:
    """
        users = db.fetch()
        usernames = []
        for user in users.items:
            usernames.append(user['key'])
        return usernames


    def validate_email(email):
        """
    Check Email Validity
    :param email:
    :return True if email is valid else False:
    """
        pattern = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$" #tesQQ12@gmail.com

        if re.match(pattern, email):
            return True
        return False


    def validate_username(username):
        """
    Checks Validity of userName
    :param username:
    :return True if username is valid else False:
        """

        pattern = "^[a-zA-Z0-9]*$"
        if re.match(pattern, username):
            return True
        return False 

    def sign_up():
        with st.form(key='signup', clear_on_submit=True):
            st.subheader(':green[Sign Up]')
            email = st.text_input(':blue[Email]', placeholder='Enter Your Email')
            username = st.text_input(':blue[Username]', placeholder='Enter Your Username')
            password1 = st.text_input(':blue[Password]', placeholder='Enter Your Password', type='password')
            password2 = st.text_input(':blue[Confirm Password]', placeholder='Confirm Your Password', type='password')

            if email:
                if validate_email(email):
                    if email not in get_user_emails():
                        if validate_username(username):
                            if username not in get_usernames():
                                if len(username) >= 2:
                                    if len(password1) >= 6:
                                        if password1 == password2:
                                        # Add User to DB
                                            hashed_password = stauth.Hasher([password2]).generate()
                                        #insert_user(email, username, hashed_password[0])
                                            insert_user(email, username, password2)
                                            st.success('Account created successfully!!')
                                            st.info("Please Login to continue")
                                            st.balloons()
                                        else:
                                            st.warning('Passwords Do Not Match')
                                    else:
                                        st.warning('Password is too Short')
                                else:
                                    st.warning('Username Too short')
                            else:
                                st.warning('Username Already Exists')

                        else:
                            st.warning('Invalid Username')
                    else:
                        st.warning('Email Already exists!!')
                else:        
                    st.warning('Invalid Email')

            st.form_submit_button("Sign Up!")
    
    sign_up()



#st.set_page_config(page_title='Streamlit', page_icon='🐍', initial_sidebar_state='collapsed')

#st.set_page_config(page_title='Streamlit', page_icon='🐍', initial_sidebar_state='collapsed')
    st.write("------")
    users = fetch_users()
    emails = [user['key'] for user in users]
    usernames = [user['username'] for user in users]
    passwords = [user['password'] for user in users]

    email = st.text_input('Email')
    password = st.text_input('Password', type='password')

    if st.button('Login'):
        if email in emails:
            user_index = emails.index(email)
            if passwords[user_index] == password:
                st.success('Login successful!')
                st.sidebar.subheader(f'Welcome {usernames[user_index]}')
                st.snow()
                session_state.is_authenticated = True
             


            else:
                st.warning('Incorrect password')
        else:
            st.warning('Email not found. Please sign up.')

    st.write("------")