import folium
import pandas as pd
import xyzservices.providers as xyz
import functions
import branca
# Reading the volcanoes file and extracting the necessary details
data = pd.read_csv("volcanoes2.csv")
lat = list(data["Latitude"])
lon = list(data["Longitude"])
name = list(data["Volcano Name"])
elevation = list(data["Elevation (m)"])

html = """<h4>Volcano information:</h4>
Name: %s \n

Height in meters: %s 
"""

# Using xyz library, I got a custom set of tiles
# Important - instead of using xyz.provider.url, use xyz.provider.build_url()
tiles = xyz.Stadia.StamenTerrain.build_url()
attr =  xyz.Stadia.StamenTerrain.html_attribution

# Creating a feature group (important for layers)
feature_group = folium.FeatureGroup(name = "Volcanoes")
feature_group1 = folium.FeatureGroup(name = "Countries Population")

# Adding each marker to the map
for lt, lg, nm, el in zip(lat, lon, name, elevation):
    iframe = folium.IFrame(html=html % (nm, str(el)), width=200, height=100)
    feature_group.add_child(folium.CircleMarker(location=[lt, lg], radius = 6   ,
                                                 popup= folium.Popup(iframe),
                                                 color = "black", 
                                                 weight = 1,
                                                 fill_opacity = 1,
                                                 fill_color=str(functions.elevation_calculation(el))))

feature_group1.add_child(folium.GeoJson(data = open("world.json", 'r', encoding="utf-8-sig").read(), 
                                       style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000
                                                                 else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}, 
                                                                 popup=folium.GeoJsonPopup(fields=["POP2005"], labels=False),
                                                                 zoom_on_click=True))
# Create a map with the specified tiles and attribution
map = folium.Map(location=[38.58, -99], tiles=tiles, attr=attr, zoom_start=4)

legend_html = '''
{% macro html(this, kwargs) %}
<div style="position: fixed; 
     bottom: 50px; left: 50px; width: 250px; height: 150px; 
     border:2px solid grey; z-index:9999; font-size:14px;
     background-color:white; opacity: 0.85;">
     &nbsp; <b>Legend</b> <br>
     &nbsp; Unknown Height &nbsp; <i class="fa fa-circle" style="color:blue;"></i><br>
     &nbsp; Height less than 2000 m &nbsp; <i class="fa fa-circle" style="color:green; border-color: black"></i><br>
     &nbsp; Height between 2000 and 3000 m &nbsp; <i class="fa fa-circle" style="color:orange; border-color: black"></i><br>
     &nbsp; Height more than 3000 m &nbsp; <i class="fa fa-circle" style="color:red; border-color: black"></i><br>
</div>
{% endmacro %}
'''

legend = branca.element.MacroElement()
legend._template = branca.element.Template(legend_html)

map.add_child(feature_group1)

map.add_child(feature_group)

map.add_child(folium.LayerControl())

map.get_root().add_child(legend)
map.save("map1.html")
