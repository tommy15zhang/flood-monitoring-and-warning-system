from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import build_station_list
from floodsystem.stationdata import update_water_levels



stations = build_station_list()
update_water_levels(stations)

N = 10
station_list = stations_highest_rel_level(stations, N)

for i in range(N):
        print(f"{station_list[i][0]} {station_list[i][1]}")