#!/bin/bash python3
"""
CH10 code associated with exploring the folium lib
@author Ellery Penas
@version 2018-04-09
"""

import folium


def main():
    fg = folium.FeatureGroup("MyFeatures")
    map = folium.Map(location=[37.60, -122.38],
                     zoom_start=12, tiles="Mapbox Bright")
    fg.add_child(folium.Marker(location=[
                  37.60, -122.38], popup="this is a popup!", icon=folium.Icon(color="green")))
    map.add_child(fg)
    map.save("./python-class-app/map.html")


if __name__ == "__main__":
    main()
