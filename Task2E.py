from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import build_station_list
from floodsystem.stationdata import update_water_levels
from floodsystem.plot import plot_water_levels
from floodsystem.datafetcher import fetch_measure_levels
import datetime
from floodsystem.plot import plot_water_levels_with_lists


stations = build_station_list()
update_water_levels(stations)

N = 5
dt = 10
station_list = stations_highest_rel_level(stations, N)

station_name = []

for i in station_list:
    station_name.append(i[0])

new_list = []
for station in stations:
    if station.name in station_name:
        new_list.append(station)



for station in new_list:
    dates, levels = fetch_measure_levels(station.measure_id,
                                         dt=datetime.timedelta(days=dt))
    
    plot_water_levels(station, dates, levels)

    
plot_water_levels_with_lists(new_list)