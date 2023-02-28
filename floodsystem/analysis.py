import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import datetime


def polyfit(dates, levels, p):
    #return a tuple of (i) the polynomial object and (ii) any shift of the time (date) axis
    x = matplotlib.dates.date2num(dates)
    print(f"x[0] = {x[0]}")
    print(f"x[-1] = {x[-1]}")

    p_coeff = np.polyfit(x - x[-1], levels, p)
    
    return np.poly1d(p_coeff), dates[-1]


