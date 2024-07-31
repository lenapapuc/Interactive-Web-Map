import folium
import pandas as pd
import xyzservices.providers as xyz
import functions

# Reading the volcanoes file and extracting the necessary details
data = pd.read_csv("volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
name = list(data["NAME"])
elevation = list(data["ELEV"])

html = """<h4>Volcano information:</h4>
Name: %s \n

Height: %s m 
"""

# Using xyz library, I got a custom set of tiles
# Important - instead of using xyz.provider.url, use xyz.provider.build_url()
tiles = xyz.Stadia.StamenTerrain.build_url()
attr =  xyz.Stadia.StamenTerrain.html_attribution

# Creating a feature group (important for layers)
feature_group = folium.FeatureGroup(name="Markers")

# Adding each marker to the map
for lt, lg, nm, el in zip(lat, lon, name, elevation):
    iframe = folium.IFrame(html=html % (nm, str(el)), width=200, height=100)
    feature_group.add_child(folium.CircleMarker(location=[lt, lg], radius = 10,
                                                 popup= folium.Popup(iframe),
                                                 color = "black", 
                                                 weight = 1,
                                                 fill_opacity = 1,
                                                 fill_color=str(functions.elevation_calculation(el))))

# Create a map with the specified tiles and attribution
map = folium.Map(location=[38.58, -99], tiles=tiles, attr=attr, zoom_start=4)
map.add_child(feature_group)

map.save("map1.html")
