#https://github.com/giswqs/streamlit-geospatial/blob/master/apps/device_loc.py
import time
import streamlit as st

placeholder = st.empty()

# Replace the placeholder with some text:
placeholder.text("Hello")
time.sleep(5)

# Replace the text with a chart:
placeholder.line_chart({"data": [1, 5, 2, 6]})
time.sleep(5)

# Replace the chart with several elements:
with placeholder.container():
     st.write("This is one element")
     st.write("This is another")
     time.sleep(5)

# Clear all those elements:
placeholder.empty()

    
