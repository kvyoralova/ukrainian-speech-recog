import requests
r = requests.get('https://api.ipdata.co?api-key=88e9d071ff5d290a3400ffb486184750e54f7f50affb3c8dc750878f').json()
clicked = st.button("Give me your location")
if clicked:
    pprint(r)
