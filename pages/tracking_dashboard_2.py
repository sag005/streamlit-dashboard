import streamlit as st
from utils.data_engine import generate_timeseries_data
from utils.state import initialize_session_state
from components.cards import data_card
from components.visuals import render_metric_chart
from constants import CATEGORIES, METRIC_NAMES


def run():
    """Tracking Dashboard 2"""
    initialize_session_state()

    st.title("📊 Tracking Dashboard 2")
    st.markdown("---")

    # Sidebar controls
    with st.sidebar:
        st.subheader("Filters")
        days = st.number_input("Days back", 1, 365, st.session_state.days_back)
        st.session_state.days_back = days

        category = st.radio("Category", CATEGORIES, index=CATEGORIES.index(st.session_state.category))
        st.session_state.category = category

    # Get data
    df = generate_timeseries_data(st.session_state.days_back, st.session_state.category)

    if df.empty:
        st.warning("No data available")
        return

    # Grid layout
    col1, col2, col3 = st.columns(3, gap="medium")
    with col1:
        data_card(df=df, unit="L")
    with col2:
        render_metric_chart(df, METRIC_NAMES[0], st.session_state.category)
    with col3:
        render_metric_chart(df, METRIC_NAMES[1], st.session_state.category)

    col1, col2, col3 = st.columns(3, gap="medium")
    with col1:
        render_metric_chart(df, METRIC_NAMES[2], st.session_state.category)
    with col2:
        render_metric_chart(df, METRIC_NAMES[3], st.session_state.category)
    with col3:
        render_metric_chart(df, METRIC_NAMES[4], st.session_state.category)


if __name__ == "__main__":
    run()