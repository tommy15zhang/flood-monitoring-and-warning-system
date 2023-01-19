# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa
from haversine import haversine, Unit   #import a new library to calculate distance between two stations


def station_by_distance(stations, p):
    #This function is used to obtain a list of station, distance tuples by recieving a list of station objects and a coordinate p.
    # () is turple
    sta_town_dis = []
    for station in stations:
        distance = haversine(station.coord, p)
        a = (station.name, station.town, distance)
        sta_town_dis.append(a)
    sta_town_dis = sorted_by_key(sta_town_dis, 2)
    return sta_town_dis    
     