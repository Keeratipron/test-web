import streamlit as st
import importlib

# Load secrets from secrets.toml
USERS = st.secrets["user_credentials"]

no_sidebar_style = """
    <style>
        div[data-testid="stSidebarNav"] {display: none;}
    </style>
"""

# Initialize session state
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "login_error" not in st.session_state:
    st.session_state.login_error = False
if "username_input" not in st.session_state:
    st.session_state.username_input = ""
if "password_input" not in st.session_state:
    st.session_state.password_input = ""

# Login function
def handle_login():
    username = st.session_state.username_input
    password = st.session_state.password_input
    if username == USERS["username"] and password == USERS["password"]:
        st.session_state.logged_in = True
        st.session_state.login_error = False
        
    else:
        st.session_state.login_error = True

# Logout function
def handle_logout():
    st.session_state.logged_in = False

# App logic
    
if st.session_state.logged_in:
    # Main Page (Logged-in content)
    st.set_page_config(initial_sidebar_state="expanded")

    # menu = importlib.import_module("views.main")
    menu = importlib.import_module("main")
    menu.menu()

    with st.sidebar:
        menu = st.popover(f'{USERS["name"]}')
        menu.markdown("###### Line1")
        menu.markdown("###### Line2")
        menu.markdown("###### Line3")
    st.sidebar.button("Logout", on_click=handle_logout)  # Logout button in sidebar

elif not st.session_state.get("logged_in", False):
    # Set page configuration to collapse the sidebar
    st.set_page_config(initial_sidebar_state="collapsed")

    # Style to hide the sidebar
    st.markdown(no_sidebar_style, unsafe_allow_html=True)

    # Login Page UI
    st.title("Login")

    # Input fields for username and password
    username = st.text_input("Username", key="username_input")
    password = st.text_input("Password", type="password", key="password_input")

    st.button("Login", on_click=handle_login)

    # Automatically call the login handler when inputs change (if needed)
    if username and password and st.session_state.get("login_attempted", False):
        handle_login()

    # Show error message if login fails
    if st.session_state.get("login_error", False):
        st.error("Invalid username or password!")

    if not username or not password:
        st.session_state.login_error = False