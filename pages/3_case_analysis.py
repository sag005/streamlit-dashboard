import streamlit as st
from datetime import datetime
import pandas as pd
import math
from utils.data_engine import generate_case_data
from utils.state import initialize_session_state
from components.cards import data_card
from components.tables import metric_detail_card
from constants import CATEGORIES

initialize_session_state()

st.title("🔍 Case Analysis")
st.markdown("---")

# Sidebar controls
with st.sidebar:
    st.subheader("Filters")

    # Date picker (only past dates)
    case_date = st.date_input(
        "Select date",
        value=st.session_state.get("case_date", datetime.now().date()),
        max_value=datetime.now().date()
    )
    st.session_state.case_date = case_date

    # Category selector
    category = st.radio(
        "Category",
        CATEGORIES,
        index=CATEGORIES.index(st.session_state.get("case_category", "news"))
    )
    st.session_state.case_category = category

# Get case data
case_data = generate_case_data(
    case_date.isoformat(),
    category
)

if not case_data:
    st.warning("No case data available for selected date and category")
    st.stop()

# ===== TOP SECTION: Data card + Response text =====
col1, col2 = st.columns([1, 1], gap="large")

# Create mock dataframe for data_card
mock_df = pd.DataFrame({
    'metric_name': [m['name'] for m in case_data['metrics']],
    'value': [m['score'] for m in case_data['metrics']]
})

with col1:
    st.subheader("Summary")
    data_card(df=mock_df, unit="")

with col2:
    st.subheader("Case Response")
    with st.container(border=True):
        st.write(case_data['response_text'])

st.markdown("---")

# ===== BOTTOM SECTION: Dynamic Grid of Metric Cards =====
st.subheader("Metrics Analysis")

metrics = case_data['metrics']
num_metrics = len(metrics)
num_cols = 3
num_rows = math.ceil(num_metrics / num_cols)

# Create grid with spacing between rows
metric_index = 0
for row in range(num_rows):
    cols = st.columns(num_cols, gap="medium")

    for col_idx, col in enumerate(cols):
        if metric_index < num_metrics:
            with col:
                metric_detail_card(metrics[metric_index])
            metric_index += 1

    # Add vertical space between rows
    if row < num_rows - 1:
        st.markdown("")
        st.markdown("")