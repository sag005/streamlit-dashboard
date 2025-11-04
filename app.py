import streamlit as st
from load_and_run import sidebar1, tab1
from eval_analysis import tab2
from playground import tab3

def main():
    st.set_page_config(layout="wide")

    tabs = st.tabs(["Load & Run", "Eval analysis", "Playground"])

    with st.sidebar:
        sidebar1.render()

    with tabs[0]:
        tab1.render()

    with tabs[1]:
        tab2.render()

    with tabs[2]:
        tab3.render()


if __name__ == "__main__":
    main()