import streamlit as st
from auth.core import initialize_session
from auth.email import verify_email
from model.predict import get_risk_prediction
from services.pdf import generate_health_report

# Initialize app
initialize_session()

# Page configuration
st.set_page_config(
    page_title="FemCare Health",
    page_icon="🌸",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Authentication flow
if not st.session_state.get('authenticated'):
    from auth.views import render_login_page
    render_login_page()
elif not st.session_state.get('email_verified'):
    verify_email()
else:
    from pages.dashboard import show_dashboard
    show_dashboard()