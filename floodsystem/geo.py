# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""
from .utils import sorted_by_key 
from haversine import haversine, Unit   #import a new library to calculate distance between two stations



""" Task 1B """

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

    
""" Task 1C """
def station_within_radius(stations, centre, r):
    
    # This function returns a list of all stations (type MonitoringStation) within radius r of a geographic coordinate x

    fit_station = []
    for station in stations:
        dist = haversine(station.coord, centre)
        if dist <= r:
            fit_station.append(station.name)
                   
    fit_station = sorted(fit_station)  # why fit_station.sort() will fail here?
    return fit_station
            

""" Task 1D """         
def rivers_with_station(stations):
    # given a list of station objects, this function returns a container (set) with the names of the rivers with a monitoring station
    
    river_name = set()
    for station in stations:
        river_name.add(f"{station.river}")
    return sorted(river_name)



def stations_by_river(stations):
    river_dict = {}
    for station in stations:
        if station.river not in river_dict:
            river_dict[station.river] = [station.name]
        # elif station.river in rivers_with_station(stations):
        else:
            river_dict[station.river].append(station.name)
    return river_dict

""" Task 1E """

def rivers_by_station_number(stations, N):
    # This funciton returns the N rivers with the greatest number of monitoring stations. (river name, number of stations) tuples, sorted by the number of stations. 
    # In the case that there are more rivers with the same number of stations as the N th entry, it includes these rivers in the list
    river_dict = stations_by_river(stations)
    river_station_num = []
    for i in river_dict.keys():
        z = (i, len(river_dict[i]))
        river_station_num.append(z)
        
    river_station_num = sorted_by_key(river_station_num, 1, True)
    while river_station_num[N][1] != river_station_num[N+1][1]:
        N = N + 1
        print(N)
        
    return river_station_num[0:N] 
