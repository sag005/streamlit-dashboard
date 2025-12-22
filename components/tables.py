import streamlit as st
import pandas as pd


def metrics_table(metrics: list):
    """
    Display metrics in a table format (5 columns).

    Args:
        metrics: List of metric dictionaries from case_data
    """
    if not metrics:
        st.info("No metrics available")
        return

    # Create dataframe from metrics
    table_data = []
    for metric in metrics:
        table_data.append({
            'Metric': metric['name'],
            'Score': f"{metric['score']:.0f}",
            'Unit': metric['unit'],
            'Status': '✅ Pass' if metric['is_pass'] else '❌ Fail',
            'Min Pass': f"{metric['minimum_pass']:.0f}"
        })

    df = pd.DataFrame(table_data)

    # Display as table
    st.dataframe(df, use_container_width=True, hide_index=True)


def metric_detail_card(metric: dict):
    """
    Display a single metric in a card with scrollable content.

    Args:
        metric: Single metric dictionary
    """
    with st.container(border=True):
        # Header with name and status
        col1, col2 = st.columns([3, 1])
        with col1:
            st.write(f"**{metric['name']}**")
        with col2:
            status_text = '✅ Pass' if metric['is_pass'] else '❌ Fail'
            st.write(status_text)

        st.divider()

        # Scrollable content area with fixed height
        st.markdown(
            f"""
            <div style="height: 250px; overflow-y: auto; padding-right: 10px;">
                <p><strong>Score:</strong> {metric['score']:.1f} {metric['unit']}</p>
                <p><strong>Min Pass:</strong> {metric['minimum_pass']:.1f}</p>
                <p><strong>Reason:</strong></p>
                <p>{metric['reason']}</p>
            </div>
            """,
            unsafe_allow_html=True
        )