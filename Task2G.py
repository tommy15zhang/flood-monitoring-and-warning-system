from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import build_station_list
from floodsystem.stationdata import update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.plot import plot_water_level_with_fit_future
import datetime
from floodsystem.flood import stations_highest_rel_level
import matplotlib
import numpy as np

stations = build_station_list()
update_water_levels(stations)

#number of days of the data
dt = 2
#number of degree of the polynomial
p = 4
#number of stations
N = 5




station_list = stations_highest_rel_level(stations, N)
station_name = []
for i in station_list:
    station_name.append(i[0])
new_list = []
for station in stations:
    if station.name in station_name:
        new_list.append(station)
        
severe_town_list = []

for station in new_list:
    dates, levels = fetch_measure_levels(station.measure_id,
                                         dt=datetime.timedelta(days=dt))
    
    predicted_water_level = plot_water_level_with_fit_future(station, dates, levels, p)
    
    x = matplotlib.dates.date2num(dates)
    p_coeff = np.polyfit(x - x[-1], levels, p)
    coeff = np.poly1d(p_coeff)
    
    dx = 0.0000001
    x = matplotlib.dates.date2num(dates[0])
    rate_of_change = (coeff(x+dx) - coeff(x))/dx
    
    if rate_of_change > 0 and predicted_water_level > station.typical_range[1]:
        print(f'risk level of {station.name} = severe')
        severe_town_list.append(station.name)
    elif rate_of_change < 0 and predicted_water_level > station.typical_range[1]:
        print(f'risk level of {station.name} = high')
    elif rate_of_change > 0 and predicted_water_level < station.typical_range[1]:
        print(f'risk level of {station.name} = moderate')
    else:
        print(f'risk level of {station.name} = low')
        
# > high range + rising = servere
# > high range + falling = high
# < high range + rising = moderate
# < high range + falling = low

print(f'severe_town_list = {severe_town_list}')       
    
