import folium
import xyzservices.providers as xyz

# Using xyz library, I got a custom set of tiles
# Important - instead of using xyz.provider.url, use xyz.provider.build_url()
tiles = xyz.Stadia.StamenTerrain.build_url()
attr =  xyz.Stadia.StamenTerrain.html_attribution

# Create a map with the specified tiles and attribution
map = folium.Map(location=[38.58, -99], tiles=tiles, attr=attr, zoom_start=4)

map.save("map1.html")
