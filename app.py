"""Simple Streamlit test app for Coolify deployment verification."""

import streamlit as st
import datetime

st.set_page_config(page_title="Coolify Test", page_icon="🚀")

st.title("Coolify Deployment Test")
st.success("If you can see this, the deployment worked!")
st.info("v5 — checking webhook delivery logs")

st.markdown("---")
st.markdown(f"**Server time:** {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
st.markdown(f"**Streamlit version:** {st.__version__}")

name = st.text_input("Enter your name", placeholder="Captain")
if name:
    st.balloons()
    st.write(f"Hello, {name}! 🎉")
