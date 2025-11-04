import streamlit as st
from services import data_loader_service

def load_css(file_path):
    with open(file_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


def render():
    data = data_loader_service.load_data()

    # Load CSS
    load_css("assets/styles.css")

    # Initialize session state
    if 'portfolio_idx' not in st.session_state:
        st.session_state.portfolio_idx = 0
    if 'summary_idx' not in st.session_state:
        st.session_state.summary_idx = {}

    # Top: Data Summary
    st.header("Data Summary")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Portfolio", data['summary']['total_portfolio'])
    with col2:
        st.metric("Avg Size of Portfolio", f"${data['summary']['avg_size_of_portfolio']:,}")
    with col3:
        st.metric("Avg Summaries per Portfolio", data['summary']['avg_summaries_in_each_portfolio'])

    st.divider()

    # Below divider: 2 columns
    left_col, right_col = st.columns([1, 2])

    # Left: Run Configuration with card styling
    with left_col:
        st.subheader("Run Configuration")

        # Model Setting Card
        model_config = data['run_configuration']['model_setting']
        st.markdown(f"""
            <div class="eval-card">
                <div class="card-name">Model Setting</div>
                <div class="card-row">
                    <div class="card-label">model_name</div>
                    <div class="card-value">{model_config['model_name']}</div>
                </div>
                <div class="card-row">
                    <div class="card-label">temperature</div>
                    <div class="card-value">{model_config['temperature']}</div>
                </div>
                <div class="card-row">
                    <div class="card-label">thinking</div>
                    <div class="card-value">{model_config['thinking']}</div>
                </div>
                <div class="card-row">
                    <div class="card-label">prompt_version</div>
                    <div class="card-value">{model_config['prompt_version']}</div>
                </div>
            </div>
        """, unsafe_allow_html=True)

        # News Setting Card
        news_config = data['run_configuration']['news_setting']
        st.markdown(f"""
            <div class="eval-card">
                <div class="card-name">News Setting</div>
                <div class="card-row">
                    <div class="card-label">start_date</div>
                    <div class="card-value">{news_config['start_date']}</div>
                </div>
                <div class="card-row">
                    <div class="card-label">end_date</div>
                    <div class="card-value">{news_config['end_date']}</div>
                </div>
                <div class="card-row">
                    <div class="card-label">days</div>
                    <div class="card-value">{news_config['days']}</div>
                </div>
            </div>
        """, unsafe_allow_html=True)

        # Performance Setting Card
        perf_config = data['run_configuration']['performance_setting']
        st.markdown(f"""
            <div class="eval-card">
                <div class="card-name">Performance Setting</div>
                <div class="card-row">
                    <div class="card-label">start_date</div>
                    <div class="card-value">{perf_config['start_date']}</div>
                </div>
                <div class="card-row">
                    <div class="card-label">end_date</div>
                    <div class="card-value">{perf_config['end_date']}</div>
                </div>
                <div class="card-row">
                    <div class="card-label">days</div>
                    <div class="card-value">{perf_config['days']}</div>
                </div>
            </div>
        """, unsafe_allow_html=True)

    # Right: Single Portfolio with navigation
    with right_col:
        total_portfolios = len(data['portfolios'])

        # Portfolio navigation
        nav_col1, nav_col2, nav_col3 = st.columns([1, 3, 1])
        with nav_col1:
            if st.button("◀", key="prev_portfolio"):
                st.session_state.portfolio_idx = (st.session_state.portfolio_idx - 1) % total_portfolios
        with nav_col2:
            st.markdown(
                f"<div style='text-align: center'><b>Portfolio {st.session_state.portfolio_idx + 1} of {total_portfolios}</b></div>",
                unsafe_allow_html=True)
        with nav_col3:
            if st.button("▶", key="next_portfolio"):
                st.session_state.portfolio_idx = (st.session_state.portfolio_idx + 1) % total_portfolios

        portfolio = data['portfolios'][st.session_state.portfolio_idx]

        # Portfolio Insight Card
        st.markdown(f"""
            <div class="eval-card">
                <div class="card-name">Portfolio Insight</div>
                <div class="card-row">
                    <div style="color: #ccc;">{portfolio['portfolio_insight']}</div>
                </div>
            </div>
        """, unsafe_allow_html=True)

        # Holdings Table
        holdings_html = '<div class="holdings-table"><div class="holdings-header"><div>Asset</div><div>Movement ($)</div><div>Movement (%)</div></div>'

        for ticker, movement in portfolio['holdings'].items():
            dollar_class = "holdings-positive" if movement['movement_dollars'] >= 0 else "holdings-negative"
            percent_class = "holdings-positive" if movement['movement_percentage'] >= 0 else "holdings-negative"
            dollar_sign = "+" if movement['movement_dollars'] >= 0 else ""
            percent_sign = "+" if movement['movement_percentage'] >= 0 else ""

            holdings_html += f'<div class="holdings-row"><div class="holdings-asset"><div class="holdings-name">{ticker}</div></div><div class="holdings-price {dollar_class}">{dollar_sign}${movement["movement_dollars"]}</div><div class="holdings-amount {percent_class}">{percent_sign}{movement["movement_percentage"]}%</div></div>'

        holdings_html += "</div>"
        st.markdown(holdings_html, unsafe_allow_html=True)

        with st.container(border=True):
            st.write("**Ticker Summaries**")

            # Ticker selection dropdown
            tickers = list(portfolio['ticker_summaries'].keys())
            selected_ticker = st.selectbox("Select Ticker", tickers,
                                           key=f"ticker_select_p{st.session_state.portfolio_idx}")

            if selected_ticker:
                summaries = portfolio['ticker_summaries'][selected_ticker]

                # Initialize summary index for this ticker
                ticker_key = f"p{st.session_state.portfolio_idx}_{selected_ticker}"
                if ticker_key not in st.session_state.summary_idx:
                    st.session_state.summary_idx[ticker_key] = 0

                total_summaries = len(summaries)
                current_idx = st.session_state.summary_idx[ticker_key]

                # Summary navigation
                s_col1, s_col2, s_col3 = st.columns([1, 3, 1])
                with s_col1:
                    if st.button("◀", key=f"prev_{ticker_key}"):
                        st.session_state.summary_idx[ticker_key] = (current_idx - 1) % total_summaries
                with s_col2:
                    st.markdown(f"<div style='text-align: center'>Summary {current_idx + 1} of {total_summaries}</div>",
                                unsafe_allow_html=True)
                with s_col3:
                    if st.button("▶", key=f"next_{ticker_key}"):
                        st.session_state.summary_idx[ticker_key] = (current_idx + 1) % total_summaries

                st.write(summaries[st.session_state.summary_idx[ticker_key]])