#!/bin/bash/env python3
"""
CH10 code associated with exploring the folium lib
@author Ellery Penas
@version 2018-04-09
"""

import folium
import pandas


def main():

    data = pandas.read_csv(
        "./python-class-app/CH10-App2/mapping/Volcanoes_USA.txt")
    lat = list(data['LAT'])
    lon = list(data['LON'])
    fg = folium.FeatureGroup("MyFeatures")
    map = folium.Map(location=[37.60, -122.38],
                     zoom_start=10)
    for lt, ln in zip(lat, lon):
        fg.add_child(
            folium.Marker(
                location=[lt, ln],
                popup="this is a popup!",
                icon=folium.Icon(
                    color="red")))

    map.add_child(fg)

    map.save("./python-class-app/map.html")


if __name__ == "__main__":
    main()
