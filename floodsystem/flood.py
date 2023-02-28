from floodsystem.utils import sorted_by_key
from floodsystem.station import inconsistent_typical_range_stations

def stations_level_over_threshold(stations, tol):
    stations_over_tol = []
    inconsistent_list = inconsistent_typical_range_stations(stations)
    
    for station in stations:
        if station.name not in inconsistent_list:
            relative_level = station.relative_water_level()
            if relative_level != None and station.relative_water_level() > tol:
                stations_over_tol.append((station.name, station.relative_water_level()))
    return sorted_by_key(stations_over_tol, 1, reverse=True)


def stations_highest_rel_level(stations, N):
    station_list = []
    inconsistent_list = inconsistent_typical_range_stations(stations)
    
    
    for station in stations:
        if station.name not in inconsistent_list:
            relative_level = station.relative_water_level()
            if relative_level != None:
                station_list.append((station.name, station.relative_water_level()))
        
    station_list = sorted_by_key(station_list, 1, reverse=True)
    return station_list[0:N]
        
        
        
        
            
            
            
        
        
    