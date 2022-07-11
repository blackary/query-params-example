from time import sleep

import streamlit as st

if "params" not in st.session_state:
    params = st.experimental_get_query_params()
    st.session_state["params"] = params

"Params when the page was loaded:"
st.write(st.session_state["params"])

st.write(
    '<a href="?foo=bar" target=_blank>Click me to add query params</a>',
    unsafe_allow_html=True,
)
