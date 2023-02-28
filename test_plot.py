from floodsystem.plot import plot_water_levels, plot_water_levels_with_lists, plot_water_level_with_fit, plot_water_level_with_fit_future
import numpy
from floodsystem.station import MonitoringStation
from floodsystem.datafetcher import fetch_measure_levels
import datetime

def fake_station_list():
    s_id = 'test_id'
    a_id = "http://environment.data.gov.uk/flood-monitoring/id/measures/52119-level-stage-i-15_min-mASD"
    b_id = "http://environment.data.gov.uk/flood-monitoring/id/measures/E2043-level-stage-i-15_min-mASD"
    c_id = 'http://environment.data.gov.uk/flood-monitoring/id/measures/1029TH-level-stage-i-15_min-mASD'
    d_id = 'http://environment.data.gov.uk/flood-monitoring/id/measures/52119-level-stage-i-15_min-mASD'
    e_id = 'http://environment.data.gov.uk/flood-monitoring/id/measures/E2043-level-stage-i-15_min-mASD'
    
    # station 1
    label_A = "some stationA"
    coord_A = (-4.0, 4.0)
    trange_A = (1, 3.4445)
    river_A = "River A"
    town_A = "My Town A"
    A = MonitoringStation(s_id, a_id, label_A, coord_A, trange_A, river_A, town_A)
    
    A.latest_level = 1.3
    # station 2
    
    label_B = "some stationB"
    coord_B = (-10.0, 4.0)
    trange_B = (1, 4.4445)
    river_B = "River B"
    town_B = "My Town B"
    
    B = MonitoringStation(s_id, b_id, label_B, coord_B, trange_B, river_B, town_B)
    B.latest_level = 1.4

    # station 3
    label_C = "some stationC"
    coord_C = (-13.0, 4.0)
    trange_C = (2.3, 5.4445)
    river_C = "River C"
    town_C = "My Town C"


    
    C = MonitoringStation(s_id, c_id, label_C, coord_C, trange_C, river_C, town_C)
    C.latest_level = 1.5
    
    # station 4
    label_D = "some stationD"
    coord_D = (-15.0, 4.0)
    trange_D = (2.3, 6.4445)
    river_D = "River D"
    town_D = "My Town D"
    
    D = MonitoringStation(s_id, d_id, label_D, coord_D, trange_D, river_D, town_D)
    D.latest_level = 1.6
    # station 5
    label_E = "some stationE"
    coord_E = (-17.0, 4.0)
    trange_E = (2.3, 7.4445)
    river_E = "River E"
    town_E = "My Town"
    
    
    E = MonitoringStation(s_id, e_id, label_E, coord_E, trange_E, river_E, town_E)
    E.latest_level = 1.7
    
    fake_station_list = []
    fake_station_list.append(A)
    fake_station_list.append(B)
    fake_station_list.append(C)
    fake_station_list.append(D)
    fake_station_list.append(E)

    return fake_station_list


def test_plot_water_levels():
    dt = 2
    
    fake_stations = fake_station_list()
    for station in fake_stations:
        dates, levels = fetch_measure_levels(station.measure_id,
                                         dt=datetime.timedelta(days=dt))
        assert plot_water_levels(station, dates, levels) == None
        

def test_plot_water_levels_with_lists():
    stations = fake_station_list()
    assert plot_water_levels_with_lists(stations) == None



def test_plot_water_level_with_fit():
    stations = fake_station_list()
    p = 4
    dt = 2
    for station in stations:
        dates, levels = fetch_measure_levels(station.measure_id,
                                         dt=datetime.timedelta(days=dt))
        assert plot_water_level_with_fit(station, dates, levels, p) == None
    


def test_plot_water_level_with_fit_future():
    stations = fake_station_list()
    p = 4
    dt = 2
    for station in stations:
        dates, levels = fetch_measure_levels(station.measure_id,
                                         dt=datetime.timedelta(days=dt))
    x = plot_water_level_with_fit_future(station, dates, levels, p)
    assert type(x) == numpy.float64

