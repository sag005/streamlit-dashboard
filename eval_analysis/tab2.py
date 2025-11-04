import streamlit as st
from services import eval_analysis_service


def load_css(file_path):
    with open(file_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


def render():
    # Check if eval results are loaded
    if 'eval_results' not in st.session_state:
        st.info("Please run evaluation from the sidebar to view results.")
        return

    st.header("Eval Analysis")
    load_css("assets/styles.css")

    data = st.session_state.eval_results

    # Initialize session state
    if 'case_idx' not in st.session_state:
        st.session_state.case_idx = 0
    if 'eval_source' not in st.session_state:
        st.session_state.eval_source = "vertex_ai"

    # Top section: metadata card (left) + 4 metric cards (right)
    left_top, right_top = st.columns([1, 3])

    with left_top:
        metadata = data['inference_metadata']
        st.markdown(f"""
            <div class="eval-card">
                <div class="card-name">Inference Metadata</div>
                <div class="card-row">
                    <div class="card-label">GCS Filename</div>
                    <div class="card-value">{metadata.gcs_filename}</div>
                </div>
                <div class="card-row">
                    <div class="card-label">Prompt Version</div>
                    <div class="card-value">{metadata.prompt_version}</div>
                </div>
                <div class="card-row">
                    <div class="card-label">LLM Used</div>
                    <div class="card-value">{metadata.llm_used}</div>
                </div>
                <div class="card-row">
                    <div class="card-label">Temperature</div>
                    <div class="card-value">{metadata.temperature}</div>
                </div>
            </div>
        """, unsafe_allow_html=True)

    with right_top:
        col1, col2, col3, col4 = st.columns(4)
        for col, metric in zip([col1, col2, col3, col4], data['overall_metrics_stats']):
            with col:
                status_class = "card-status" if metric.verdict == "pass" else "card-status-fail"
                st.markdown(f"""
                    <div class="eval-card">
                        <div class="card-name">{metric.eval_name}</div>
                        <div class="card-row">
                            <div class="card-label">Score</div>
                            <div class="card-value">{metric.score}</div>
                        </div>
                        <div class="card-row">
                            <div class="card-label">Verdict</div>
                            <div class="{status_class}">{metric.verdict.upper()}</div>
                        </div>
                        <div class="card-row">
                            <div class="card-label">Std Dev</div>
                            <div class="card-value">{metric.std_deviation}</div>
                        </div>
                        <div class="card-row">
                            <div class="card-label">Total Cases</div>
                            <div class="card-value">{metric.total_cases}</div>
                        </div>
                        <div class="card-row">
                            <div class="card-label">System Errors</div>
                            <div class="card-value">{metric.system_errors}</div>
                        </div>
                    </div>
                """, unsafe_allow_html=True)

    st.divider()

    # Bottom section: case evaluation results
    total_cases = len(data['case_eval_results'])

    # Case navigation
    nav_col1, nav_col2, nav_col3 = st.columns([1, 3, 1])
    with nav_col1:
        if st.button("◀", key="prev_case"):
            st.session_state.case_idx = (st.session_state.case_idx - 1) % total_cases
    with nav_col2:
        st.markdown(
            f"<div style='text-align: center'><b>Case {st.session_state.case_idx + 1} of {total_cases}</b></div>",
            unsafe_allow_html=True)
    with nav_col3:
        if st.button("▶", key="next_case"):
            st.session_state.case_idx = (st.session_state.case_idx + 1) % total_cases

    case = data['case_eval_results'][st.session_state.case_idx]

    # Toggle between evaluation sources
    eval_source = st.radio("Evaluation Source", ["Vertex AI", "DeepEval"], horizontal=True, key="eval_toggle")
    st.session_state.eval_source = "vertex_ai" if eval_source == "Vertex AI" else "deepeval"

    # Split into left (eval cards) 60% and right (summary) 40%
    left_bottom, right_bottom = st.columns([3, 2])

    with left_bottom:
        # Get the appropriate eval results
        eval_results = case.vertex_ai_eval_results if st.session_state.eval_source == "vertex_ai" else case.deepeval_results

        # Display cards in 2x4 grid (2 cols per row)
        for i in range(0, len(eval_results), 2):
            cols = st.columns(2)
            for j, col in enumerate(cols):
                if i + j < len(eval_results):
                    eval_result = eval_results[i + j]
                    with col:
                        status_class = "card-status" if eval_result.verdict == "pass" else "card-status-fail"
                        score_display = str(eval_result.score) if isinstance(eval_result.score,
                                                                             bool) else f"{eval_result.score}"
                        st.markdown(f"""
                            <div class="eval-card-small">
                                <div class="card-name">{eval_result.eval_name}</div>
                                <div class="card-row">
                                    <div class="card-label">Score</div>
                                    <div class="card-value">{score_display}</div>
                                </div>
                                <div class="card-row">
                                    <div class="{status_class}">{eval_result.verdict.upper()}</div>
                                </div>
                            </div>
                        """, unsafe_allow_html=True)

    with right_bottom:
        st.markdown(f"""
            <div class="eval-card">
                <div class="card-row">
                    <div class="card-label">Portfolio ID</div>
                    <div style="color: #fff; font-size: clamp(0.9rem, 2cqw, 1.1rem);">{case.portfolio_id}</div>
                </div>
                <div class="card-name" style="margin-top: 20px;">Summary</div>
                <div style="color: #ccc; font-size: 0.9rem; line-height: 1.5;">{case.summary}</div>
            </div>
        """, unsafe_allow_html=True)