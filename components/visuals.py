import streamlit as st
import pandas as pd


def render_metric_chart(df: pd.DataFrame, metric_name: str, category: str = None):
    """
    Render a simple line chart in Streamlit for a specific metric.

    Args:
        df: Time-series DataFrame with columns: date, metric_name, value
        metric_name: Name of the metric to plot
        category: Category (used for future enhancements, not needed now)
    """
    # Filter data for this metric
    metric_df = df[df['metric_name'] == metric_name].copy()
    metric_df = metric_df.sort_values('date')

    if metric_df.empty:
        st.warning(f"No data available for {metric_name}")
        return

    # Prepare chart data - set date as index for cleaner display
    chart_data = metric_df.set_index('date')[['value']]
    chart_data.columns = [metric_name]

    # Display title
    st.subheader(metric_name)

    # Render simple line chart
    st.line_chart(chart_data, use_container_width=True)