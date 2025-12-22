import streamlit as st
from datetime import datetime, timedelta
from utils.data_engine import generate_timeseries_data
from utils.state import initialize_session_state
from components.cards import metric_summary_card
from components.visuals import render_merged_charts
from constants import CATEGORIES, METRIC_NAMES

initialize_session_state()

# Set page to wide layout
st.set_page_config(layout="wide")

st.title("📊 Tracking Dashboard 2")
st.markdown("---")

# Control inputs on main screen (not sidebar)
col1, col2, col3 = st.columns([1.5, 1.5, 1], gap="medium")

with col1:
    start_date = st.date_input(
        "Start date",
        value=st.session_state.get("start_date", datetime.now().date() - timedelta(days=6)),
        max_value=datetime.now().date()
    )
    st.session_state.start_date = start_date

with col2:
    end_date = st.date_input(
        "End date",
        value=st.session_state.get("end_date", datetime.now().date()),
        max_value=datetime.now().date()
    )
    st.session_state.end_date = end_date

with col3:
    category = st.selectbox(
        "Category",
        CATEGORIES,
        index=CATEGORIES.index(st.session_state.category)
    )
    st.session_state.category = category

st.markdown("---")

# Validate date range
if start_date > end_date:
    st.error("Start date cannot be after end date!")
    st.stop()

# Calculate days for data generation
days_back = (end_date - start_date).days + 1

# Get data
df = generate_timeseries_data(days_back, st.session_state.category)

if df.empty:
    st.warning("No data available")
    st.stop()

# ===== TOP SECTION: 5 Metric Summary Cards =====
st.subheader("Metrics Summary")

cols = st.columns(5, gap="small")
for idx, metric_name in enumerate(METRIC_NAMES):
    # Calculate success/fail/error percentages for each metric
    metric_data = df[df['metric_name'] == metric_name]['value']

    if not metric_data.empty:
        avg_value = metric_data.mean()
        success_pct = avg_value
        fail_pct = 100 - avg_value
        error_pct = max(0, fail_pct - 30)  # Error is subset of fail
        fail_pct = min(fail_pct, 30)  # Keep fail reasonable

        with cols[idx]:
            metric_summary_card(metric_name, success_pct, fail_pct, error_pct)

# ===== BOTTOM SECTION: Merged Line Chart =====
st.markdown("---")
st.subheader("Trend Analysis")

render_merged_charts(df, METRIC_NAMES)