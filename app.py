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

if geo():
    if language == 'it':
        st.title('Правоgrafia: навчись добре писати італійською! Impara a scrivere bene in italiano!')
        st.header('Грайте, пишіть і вчіться! Gioca, scrivi e impara!')
        st.caption("Ця програма орієнтована на українських дітей, які мають труднощі з основними італійськими орфографічними перешкодами.")
        st.caption("Questa applicazione è rivolta a bambini ucraini che hanno difficoltà con i principali ostacoli ortografici italiani.")
  
        st.subheader("Давай грати! Giochiamo!")
        number = st.text_input("Дай мені число від 1 до 10. Dammi un numero da 1 a 10. ", value="")
        st.write("Або натисніть тут, щоб отримати 5 випадкових зображень. Oppure clicca qui per avere 5 immagini casuali.")
        random = st.button("Tут. Qui.")
    else:
        st.title('Правоgraphy: навчись добре писати англійською! Learn to write correctly in English!')
        st.header('Грайте, пишіть і вчіться! Play, write and learn!')
        st.caption("Це програма орієнтована на українських дітей, які мають труднощі з основними італійськими орфографічними перешкодами. В англійській версії орфографічні перешкоди не згруповані, як в італійській, а повідомляються у випадковому порядку; однак він залишається програмою, з якою користувач може практикувати.")
        st.caption("This application is aimed at Ukrainian children who have difficulty with the main Italian spelling obstacles. In the English version the spelling obstacles are not grouped as in Italian, but are reported in random order; however, it remains an application with which the user can practice.")
  
        st.subheader("Давай грати! Let's play!")
        number = st.text_input("Дай мені число від 1 до 10. Give me a number from 1 to 10. ", value="")
        st.write("Або натисніть тут, щоб отримати 5 випадкових зображень. Or click here to get 5 random images.")
        random = st.button("Tут. Here.")
