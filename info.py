# about.py

import streamlit as st

def about_page():
    st.title("Know your Devs 🧑‍💻")
    st.write("------")

    team_members = [
        {"name": "Mohammed Musharraf", "description": "The Creator", "github_url": "https://github.com/MohammedMusharraf11", "linkedin_url": "https://www.linkedin.com/in/mohammed-musharraf-44a98a280/"},
        {"name": "Team Member 2", "description": "Description of Team Member 2.", "github_url": "https://github.com/member2", "linkedin_url": "https://linkedin.com/in/member2"},
        {"name": "Team Member 3", "description": "Description of Team Member 3.", "github_url": "https://github.com/member3", "linkedin_url": "https://linkedin.com/in/member3"},
        {"name": "Team Member 4", "description": "Description of Team Member 4.", "github_url": "https://github.com/member4", "linkedin_url": "https://linkedin.com/in/member4"}
    ]

    for member in team_members:
        st.subheader(member["name"])
        st.write(member["description"])
        st.button("GitHub", key=f"github_{member['name']}", on_click=lambda member=member: open_url(member["github_url"]))
        st.button("LinkedIn", key=f"linkedin_{member['name']}", on_click=lambda member=member: open_url(member["linkedin_url"]))
        st.write("------")

def open_url(url):
    import webbrowser
    webbrowser.open_new_tab(url)
