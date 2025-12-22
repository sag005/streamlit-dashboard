import streamlit as st
import pandas as pd


def data_card(df: pd.DataFrame, unit: str = "L"):
    """
    Display a summary data card with all 5 metrics.
    Shows each metric's total in a single card.

    Args:
        df: Time-series DataFrame with metric values
        unit: Unit of measurement (e.g., "L")
    """
    if df.empty:
        st.info("No data available")
        return

    # Group by metric and sum
    metric_totals = df.groupby('metric_name')['value'].sum().sort_values(ascending=False)

    # Create card with border
    with st.container(border=True):
        # Title
        st.markdown(
            "<div style='text-align: center; color: #9CA3AF; font-size: 16px; margin-bottom: 20px;'>"
            "Total Consumption"
            "</div>",
            unsafe_allow_html=True
        )

        # Display each metric in the card
        for metric_name, total_value in metric_totals.items():
            col1, col2 = st.columns([3, 1])

            with col1:
                st.markdown(f"<div style='font-size: 16px;'>{metric_name}</div>",
                            unsafe_allow_html=True)

            with col2:
                st.markdown(
                    f"<div style='text-align: right; font-size: 16px; font-weight: 500;'>{int(total_value)} {unit}</div>",
                    unsafe_allow_html=True)


def placeholder_chart():
    """
    Display a placeholder container for charts.
    Used during layout development before actual charts are added.
    """
    with st.container(border=True):
        st.markdown(
            "<div style='display: flex; align-items: center; justify-content: center; height: 300px; color: #CCC;'>"
            "<div style='text-align: center;'>"
            "<p style='font-size: 48px; margin: 0;'>📈</p>"
            "<p style='margin: 10px 0 0 0; color: #999;'>Chart placeholder</p>"
            "<p style='font-size: 12px; margin: 5px 0 0 0; color: #CCC;'>Built in PR 4</p>"
            "</div>"
            "</div>",
            unsafe_allow_html=True
        )