#!/usr/bin/env/ python3
"""
Ch09 - numpy and pandas exploration
@author Ellery Penas
@version 2018.04.07
"""
import pandas
from geopy.geocoders import Nominatim


def main():
    """main line function"""
    df = pandas.DataFrame([[1, 2, 3], [20, 30, 40]])
    print(df)

    nom = Nominatim()
    n = nom.geocode("1441 Kains Ave, San Bruno, CA 94066")
    print("%s,%s" % (n.latitude, n.longitude))


if __name__ == "__main__":
    main()
