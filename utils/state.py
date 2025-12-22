import streamlit as st
from constants import SESSION_STATE_DEFAULTS
from datetime import datetime


def initialize_session_state():
    """
    Initialize all session state variables with default values.
    Call this at the start of each page.
    """
    if "days_back" not in st.session_state:
        st.session_state.days_back = SESSION_STATE_DEFAULTS["days_back"]

    if "category" not in st.session_state:
        st.session_state.category = SESSION_STATE_DEFAULTS["category"]

    if "case_date" not in st.session_state:
        st.session_state.case_date = datetime.now().date()

    if "case_category" not in st.session_state:
        st.session_state.case_category = SESSION_STATE_DEFAULTS["case_category"]