from floodsystem.geo import station_by_distance
from floodsystem.geo import station_within_radius
from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river
from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river
from floodsystem.geo import rivers_by_station_number
from floodsystem.station import inconsistent_typical_range_stations
from floodsystem.station import MonitoringStation


def fake_station_list():
    
    s_id = "test-s-id"
    m_id = "test-m-id"
    
    # station 1
    label_A = "some stationA"
    coord_A = (-4.0, 4.0)
    trange_A = (2, 3.4445)
    river_A = "River A"
    town_A = "My Town A"
    
    A = MonitoringStation(s_id, m_id, label_A, coord_A, trange_A, river_A, town_A)
    
    # station 2
    
    label_B = "some stationB"
    coord_B = (-10.0, 4.0)
    trange_B = (1, 4.4445)
    river_B = "River B"
    town_B = "My Town B"
    
    B = MonitoringStation(s_id, m_id, label_B, coord_B, trange_B, river_B, town_B)

    # station 3
    label_C = "some stationC"
    coord_C = (-13.0, 4.0)
    trange_C = (3, 5.4445)
    river_C = "River C"
    town_C = "My Town C"
    
    C = MonitoringStation(s_id, m_id, label_C, coord_C, trange_C, river_C, town_C)

    # station 4
    label_D = "some stationD"
    coord_D = (-15.0, 4.0)
    trange_D = (4, 6.4445)
    river_D = "River D"
    town_D = "My Town D"
    
    D = MonitoringStation(s_id, m_id, label_D, coord_D, trange_D, river_D, town_D)
    
    # station 5
    label_E = "some stationE"
    coord_E = (-17.0, 4.0)
    trange_E = (5, 7.4445)
    river_E = "River E"
    town_E = "My Town"
    
    E = MonitoringStation(s_id, m_id, label_E, coord_E, trange_E, river_E, town_E)

    fake_station_list = []
    fake_station_list.append(A)
    fake_station_list.append(B)
    fake_station_list.append(C)
    fake_station_list.append(D)
    fake_station_list.append(E)

    return fake_station_list

def test_station_by_distance():

    p = (0, 0)    
    
    assert len((station_by_distance(fake_station_list(), p))) == 5
    
    
def test_station_within_radius(): 
    
    r = 1000
    
    centre = (0,0)
    
    assert station_within_radius(fake_station_list(), centre, r) == ['some stationA']

def test_rivers_with_station():

    assert len(rivers_with_station(fake_station_list())) == 5
    

def test_stations_by_river():
    
    assert type(stations_by_river(fake_station_list())) == dict
    

def test_rivers_by_station_number():
    x = rivers_by_station_number(fake_station_list(), 1)
    
    assert x == [('River A', 1)]
    

def test_inconsistent_typical_range_stations():
    assert type(inconsistent_typical_range_stations(fake_station_list())) == list
    

