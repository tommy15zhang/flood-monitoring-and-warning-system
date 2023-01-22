# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""
from .utils import sorted_by_key 
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

    
    
def station_within_radius(stations, centre, r):
    #The functions takes the input of 
    fit_station = []
    for station in stations:
        dist = haversine(station.coord, centre)
        if dist <= r:
            fit_station.append(station.name)
                   
    fit_station = sorted(fit_station)  # why fit_station.sort() will fail here?
    return fit_station
            
            
