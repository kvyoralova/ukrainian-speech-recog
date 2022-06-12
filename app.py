#https://github.com/giswqs/streamlit-geospatial/blob/master/apps/device_loc.py
import time

with st.empty():
     for seconds in range(60):
         st.write(f"⏳ {seconds} seconds have passed")
         time.sleep(1)
     st.write("✔️ 1 minute over!")
    
