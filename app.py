#https://github.com/giswqs/streamlit-geospatial/blob/master/apps/device_loc.py
import streamlit as st
from bokeh.models.widgets import Button
from bokeh.models import CustomJS
from streamlit_bokeh_events import streamlit_bokeh_events
import leafmap.foliumap as leafmap
import geopy
from geopy.geocoders import Nominatim

def geo():
    loc_button = Button(label="Отримати місцезнаходження пристрою", max_width=250)
    loc_button.js_on_event(
        "button_click",
        CustomJS(
            code="""
        navigator.geolocation.getCurrentPosition(
            (loc) => {
                document.dispatchEvent(new CustomEvent("GET_LOCATION", {detail: {lat: loc.coords.latitude, lon: loc.coords.longitude}}))
            }
        )
        """
        ),
    )
    result = streamlit_bokeh_events(
        loc_button,
        events="GET_LOCATION",
        key="get_location",
        refresh_on_update=False,
        override_height=75,
        debounce_time=0,
    )
    if result:
        if "GET_LOCATION" in result:
            loc = result.get("GET_LOCATION")
            lat = loc.get("lat")
            lon = loc.get("lon")
            #st.write(f"Lat, Lon: {lat}, {lon}")
            latlon = str(lat) + ", " + str(lon)
            geoLoc = Nominatim(user_agent="GetLoc")
            locname = geoLoc.reverse(latlon)
            address = locname.address
            import re
            regexpr = r'[A-Za-z]+'
            actual_location = re.findall(regexpr, address.lower())
            country = actual_location[-1]
            if country == "italia":
              language = "it"
              st.write("Ви перебуваєте в Італії, тому програма працюватиме італійською мовою.")
              st.write("Sei in Italia, quindi l'app verrà eseguita in italiano.")
            else:
              language =  "en"
              st.write("Ви перебуваєте за межами Італії, тому програма працюватиме англійською мовою.")
              st.write("You are out of Italy, so the app will run in English.")

geo()
