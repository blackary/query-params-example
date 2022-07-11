import streamlit as st

if "params" not in st.session_state:
    params = st.experimental_get_query_params()
    st.session_state["params"] = params

"Params when the page was loaded:"
st.write(st.session_state["params"])


"This works locally and on cloud:"
"https://blackary-query-params-example-streamlit-app-3kod4y.streamlitapp.com/~/+/?foo=bar"

"This only works locally:"
"https://blackary-query-params-example-streamlit-app-3kod4y.streamlitapp.com/?foo=bar"
