#!/usr/bin/env python3
"""
Chapter 19 - Data analysis and display in web
    candlestick chart.
@author Ellery Penas
@version 2018.04.07
"""
import pandas_datareader .data as web
import datetime
from bokeh.plotting import figure, show, output_file


def main():
    """main line function"""
    start_time = datetime.date(2018, 1, 1)
    end_time = datetime.date(2018, 1, 3)
    info = web.DataReader(
        "GOOG",
        data_source="iex",
        start=start_time,
        end=end_time)
    print(info)

    hours_12 = 12 * 60 * 60 * 1000
    p = figure(x_axis_type='datetime', width=500, height=200)
    # p.title = "Candlestick Chart"

    p.rect(info.index[info.close > info.open],
           (info.close + info.open) / 2, hours_12, abs(info.open - info.close))
    output_file('CS.html')
    show(p)


if __name__ == "__main__":
    main()
