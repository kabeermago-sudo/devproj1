import streamlit as st
import os
import importlib.util

st.set_page_config(page_title="My Web App", layout="wide")

st.title("Your Full Name - CS 1301")
st.subheader("Welcome to My Streamlit Portfolio Web App")

st.markdown("""
This is a multi-page Streamlit app with the following sections:

- **Portfolio**: Learn about me, my projects, skills, and education.
- **Learn More Details about me**.

Use the sidebar to navigate between pages!
""")

page_folder = "pages"
page_files = {
    "Portfolio": os.path.join(page_folder, "Portfolio.py"),
    "Phase II Project": os.path.join(page_folder, "PhaseII.py")
}


st.sidebar.title("Navigation")
selected_page = st.sidebar.radio("Go to", list(page_files.keys()))


def load_module(file_path):
    spec = importlib.util.spec_from_file_location("page", file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)


load_module(page_files[selected_page])

