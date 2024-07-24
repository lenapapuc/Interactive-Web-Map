import folium
import pandas as pd
import xyzservices.providers as xyz

# Reading the volcanoes file and extracting the necessary details
data = pd.read_csv("volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
name = list(data["NAME"])
elevation = list(data["ELEV"])

# Using xyz library, I got a custom set of tiles
# Important - instead of using xyz.provider.url, use xyz.provider.build_url()
tiles = xyz.Stadia.StamenTerrain.build_url()
attr =  xyz.Stadia.StamenTerrain.html_attribution

# Creating a feature group (important for layers)
feature_group = folium.FeatureGroup(name="Markers")

# Adding each marker to the map
for lt, lg, nm, el in zip(lat, lon, name, elevation):
    feature_group.add_child(folium.Marker(location=[lt, lg], popup= f"{nm} \n Elevation: {el} ", icon=folium.Icon(color="green")))

# Create a map with the specified tiles and attribution
map = folium.Map(location=[38.58, -99], tiles=tiles, attr=attr, zoom_start=4)
map.add_child(feature_group)

map.save("map1.html")
