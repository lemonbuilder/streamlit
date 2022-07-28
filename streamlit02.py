import streamlit as st 
import time

import pandas as pd

import folium
from streamlit_folium import st_folium

st.title("hello world !!")



#######################################
# Sidebar pagination initialization
st.set_page_config("파일 업로드로 지도 그리기!")

page = st.sidebar.radio(
        "Select page!", 
        ["1. upload geo file", "2. Map is here!"], index=0)

if 'geocode1' not in st.session_state:
    st.session_state['geocode1'] = []

#######################################

#@st.cache
@st.cache(suppress_st_warning=True)  # 👈 Changed this
def expensive_computation(a, b):
    st.write("Cache miss: expensive_computation(", a, ",", b, ") ran")
    time.sleep(2)
    return a * b


a = 3
b = 21

result = expensive_computation(a, b)

########################################
st.title("Cache Test!")

st.write("Results: ", result)

if page == "1. upload geo file":
    try:
        uploaded_file = st.file_uploader("Choose geocode file")
        uploaded_file = pd.read_excel(uploaded_file).head()
        uploaded_file = uploaded_file[['district', 'latitude', 'longitude']]

        st.write(uploaded_file)
        st.write(len(uploaded_file))

        st.session_state.geocode1 = uploaded_file
        st.write(st.session_state.geocode1)

    except:
        pass


elif page == "2. Map is here!":
       
    # 위도
    latitude = 37.394946
    # 경도
    longitude = 127.111104

    m = folium.Map([latitude, longitude],
            zoom_start=16)

    folium.Marker([latitude, longitude]
            ).add_to(m)

    for idx, row in st.session_state.geocode1.iterrows():
        # st.write(row[0],row[1], row[2])
        folium.Marker([row[1], row[2]]).add_to(m)
    st_map = st_folium(m, width=750, height=400)
