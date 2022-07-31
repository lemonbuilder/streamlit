import streamlit as st 
from streamlit_folium import st_folium
import folium

st.title("hello world")


# multi-selection

## source = data.stocks()
## all_symbols = source.symbol.unique()
multi_select = st.multiselect('Please select!',
    ['A', 'B', 'C', 'D'])


# center on, add marker
m = folium.Map(location=[37.492151, 127.030949], tiles = "CartoDB positron", zoom_start=16)
folium.Marker(
    [37.492151, 127.030949],
    popup="HERE",
    tooltip="MODULABS"
    ).add_to(m)

# circle
folium.Circle(radius=50,
    location=[37.492151, 127.030949],
    color='#31ccb2',
    fill=True,
    fill_color='#31ccb2'
    ).add_to(m)


# call to Folium map in Streamlit
st_data = st_folium(m, width = 800)
