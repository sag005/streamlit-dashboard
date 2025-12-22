import streamlit as st
import pandas as pd


def data_card(df: pd.DataFrame, unit: str = "L"):
    """
    Display a summary data card with all 5 metrics.

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
        st.write("**Total Consumption**")

        # Display each metric
        for metric_name, total_value in metric_totals.items():
            col1, col2 = st.columns([3, 1])
            with col1:
                st.write(metric_name)
            with col2:
                st.write(f"{int(total_value)} {unit}")


def metric_summary_card(metric_name: str, success_pct: float, fail_pct: float, error_pct: float):
    """
    Display a metric summary card with success/fail/error percentages (VERTICAL LAYOUT).
    Used in dashboard top section.

    Args:
        metric_name: Name of the metric
        success_pct: Success percentage (0-100)
        fail_pct: Fail percentage (0-100)
        error_pct: Error percentage (0-100)
    """
    with st.container(border=True):
        # Header with metric name
        st.write(f"**{metric_name}**")

        st.divider()

        # Display percentages VERTICALLY (stacked)
        st.markdown(f"✅ **Success** {success_pct:.1f}%")
        st.markdown(f"❌ **Fail** {fail_pct:.1f}%")
        st.markdown(f"⚠️ **Error** {error_pct:.1f}%")