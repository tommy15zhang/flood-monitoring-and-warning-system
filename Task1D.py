from floodsystem.geo import rivers_with_station
from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_river


stations = build_station_list()
rivers = rivers_with_station(stations)

station_river = stations_by_river(stations)
print(f"{len(rivers)} rivers have at least one station. First 10 - {rivers[0:9]}")
print(f"River Aire {sorted(station_river['River Aire'])}")
print(f"River Cam {sorted(station_river['River Cam'])}")
print(f"River Thames{sorted(station_river['River Thames'])}")