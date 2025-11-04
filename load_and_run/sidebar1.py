import streamlit as st


def render():
    st.header("⚙️ Configuration")

    st.subheader("Run configuration")

    with st.expander("Model setting"):
        model_name = st.text_input("model_name")
        temperature = st.text_input("temperature")
        thinking = st.checkbox("thinking")

        prompt_versions = {
            "v1.0": "This is prompt version 1.0. " * 100,
            "v2.0": "This is prompt version 2.0 with updated instructions. " * 100,
            "v3.0": "This is prompt version 3.0 with enhanced guidelines. " * 100
        }

        prompt_version = st.selectbox("prompt version", list(prompt_versions.keys()))

        if st.checkbox("Show prompt preview", key="show_prompt"):
            st.text_area("Prompt text", prompt_versions[prompt_version], height=200, disabled=True)

    with st.expander("News setting"):
        news_start_date = st.date_input("start date", key="news_start")
        news_end_date = st.date_input("end date", key="news_end")
        news_days = st.number_input("#days", step=1, key="news_days")

    with st.expander("Performance setting"):
        perf_start_date = st.date_input("start date", key="perf_start")
        perf_end_date = st.date_input("end date", key="perf_end")
        perf_days = st.number_input("#days", step=1, key="perf_days")

    st.subheader("Load configuration")

    with st.expander("Load configuration"):
        bucket_name = st.text_input("bucket_name")
        prefix = st.text_input("prefix")
        gcs_inference_filename = st.text_input("gcs_inference_filename")

    if st.button("Load Data"):
        from services import data_loader_service
        st.session_state.inference_data = data_loader_service.load_data()
        st.success("Data loaded successfully!")

    if st.button("Run Eval", disabled='inference_data' not in st.session_state):
        from services import eval_analysis_service
        st.session_state.eval_results = eval_analysis_service.load_data()
        st.success("Evaluation completed successfully!")