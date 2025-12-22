import streamlit as st
import pandas as pd


def render_metric_chart(df: pd.DataFrame, metric_name: str, category: str = None):
    """
    Render a line chart for a specific metric.

    Args:
        df: Time-series DataFrame
        metric_name: Name of the metric to plot
        category: Category (for future enhancements)
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

    # Render simple line chart
    st.line_chart(chart_data, use_container_width=True)


def render_merged_charts(df: pd.DataFrame, metrics: list):
    """
    Render all metrics in a single merged chart.
    X-axis: time (date)
    Y-axis: percentage value

    Args:
        df: Time-series DataFrame with columns: date, metric_name, value
        metrics: List of metric names to include
    """
    if df.empty:
        st.warning("No data available")
        return

    # Prepare data for merged chart
    chart_data = pd.DataFrame()

    for metric in metrics:
        metric_df = df[df['metric_name'] == metric].copy()
        metric_df = metric_df.sort_values('date')

        if not metric_df.empty:
            metric_data = metric_df.set_index('date')[['value']]
            metric_data.columns = [metric]
            chart_data = pd.concat([chart_data, metric_data], axis=1)

    if chart_data.empty:
        st.warning("No data to display")
        return

    # Render merged line chart
    st.line_chart(chart_data, use_container_width=True)