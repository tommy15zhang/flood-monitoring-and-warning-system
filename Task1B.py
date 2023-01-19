from floodsystem.geo import station_by_distance
from floodsystem.stationdata import build_station_list





p = (52.2053, 0.1218) #Coordiante of Cambridge City Centre
x = station_by_distance(build_station_list(), p)
print(f"the closest 10 entries are {x[:10]}")
print(f"the furthest 10 entries are {x[-10:]}")

