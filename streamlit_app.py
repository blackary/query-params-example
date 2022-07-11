from time import sleep

import streamlit as st

params = st.experimental_get_query_params()

st.write(params)

if "redirect" in params:
    st.write("Redirecting...")
    st.experimental_set_query_params(redirected=True)
    sleep(0.1)
    st.experimental_rerun()
elif "redirected" in params:
    st.write("Redirected!")

"[Click here to redirect](?redirect=true)"
