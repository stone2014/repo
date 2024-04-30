import streamlit as st
import pandas as pd
# from pinotdb import connect
from datetime import datetime
import time
# import plotly.express as px
# import plotly.graph_objects as go 
import os
import requests

# pinot_host=os.environ.get("PINOT_SERVER", "pinot-broker")
# pinot_port=os.environ.get("PINOT_PORT", 8099)
# conn = connect(pinot_host, pinot_port)

# delivery_service_api = "http://kafka-streams-quarkus:8080"

st.set_page_config(layout="wide")
st.title("All About That Dough Dashboard 🍕")


now = datetime.now()
dt_string = now.strftime("%d %B %Y %H:%M:%S")
st.write(f"Last update: {dt_string}")

# Use session state to keep track of whether we need to auto refresh the page and the refresh frequency

if not "sleep_time" in st.session_state:
    st.session_state.sleep_time = 2

if not "auto_refresh" in st.session_state:
    st.session_state.auto_refresh = True

auto_refresh = st.checkbox('Auto Refresh?', st.session_state.auto_refresh)

if auto_refresh:
    number = st.number_input('Refresh rate in seconds', value=st.session_state.sleep_time)
    st.session_state.sleep_time = number

# curs = conn.cursor()


if auto_refresh:
    time.sleep(number)
    st.experimental_rerun()
