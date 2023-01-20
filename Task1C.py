
from floodsystem.geo import station_within_radius
from floodsystem.stationdata import build_station_list


r = 10
centre = (52.2053, 0.1218)
stations = build_station_list()
fit_stations = station_within_radius(stations, centre, r)
print(fit_stations)