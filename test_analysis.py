from floodsystem.analysis import polyfit
import datetime
from floodsystem.datafetcher import fetch_measure_levels
import numpy



def test_polyfit():
    p = 1
    dates = [1, 2]
    levels = [2, 3]

    coeff, date0 = polyfit(dates, levels, p)
    
    assert type(coeff) == numpy.poly1d
    assert type(date0) == int
    
    
test_polyfit()