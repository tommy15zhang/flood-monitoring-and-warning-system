import datetime
from floodsystem.datafetcher import fetch_measure_levels
import matplotlib.pyplot as plt
from floodsystem.datafetcher import fetch_measure_levels
import numpy as np
import matplotlib


#displays a plot (using Matplotlib) of the water level data against time 
#for a station, and include on the plot lines for the typical low and high
#levels
def plot_water_levels(station, dates, levels):    
    plt.plot(dates, levels)
    plt.axhline(y = station.typical_range[1], color = 'r', label = 'high_range')
    plt.axhline(y = station.typical_range[0], color = 'g', label = 'low_range')
    plt.legend()
    plt.xlabel('date')
    plt.ylabel('water level(m)')
    plt.xticks(rotation = 45)
    plt.title(f"Station {station.name}")
    
    plt.tight_layout()
    plt.show()
    
    
def plot_water_levels_with_lists(stations):
    dt = 10
    fig, axs = plt.subplots(len(stations), sharex=True, sharey=True)
    fig.suptitle('Sharing both axes')
    for i in range(len(stations)):
        dates, levels = fetch_measure_levels(stations[i].measure_id, dt=datetime.timedelta(days=dt))
        
        axs[i].plot(dates, levels)
        axs[i].axhline(y = stations[i].typical_range[1], color = 'r', label = 'high_range')
        axs[i].axhline(y = stations[i].typical_range[0], color = 'g', label = 'low_range')
        axs[i].set_title(f"Station {stations[i].name}")
    
    plt.legend()
    plt.tight_layout()
    plt.xticks(rotation = 45)
    plt.show()
    


def plot_water_level_with_fit(station, dates, levels, p):


    # Create set of 10 data points on interval (1000, 1002)
    x = matplotlib.dates.date2num(dates)
    y = levels

    # Using shifted x values, find coefficient of best-fit
    # polynomial f(x) of degree 4
    p_coeff = np.polyfit(x - x[-1], levels, p)

    # Convert coefficient into a polynomial that can be evaluated
    # e.g. poly(0.3)
    poly = np.poly1d(p_coeff)
    print(f'{station.name} has the polynomial of')
    print(poly)
    # Plot original data points
    x1 = np.linspace(x[0], x[-1], len(dates))
    plt.plot(dates, y, label = 'actual')
    plt.plot(dates, poly(x1-x[-1]), color = 'y', label = 'best fit polynomial')
    plt.axhline(y = station.typical_range[1], color = 'r', label = 'high_range')
    plt.axhline(y = station.typical_range[0], color = 'g', label = 'low_range')
    

    plt.legend()
    plt.xlabel('date')
    plt.ylabel('water level(m)')
    plt.xticks(rotation = 45)
    plt.title(f"Station {station.name}")
    
    plt.tight_layout()

    # Display plot
    plt.show()
    
    


def plot_water_level_with_fit_future(station, dates, levels, p):


    # Create set of 10 data points on interval (1000, 1002)
    x = matplotlib.dates.date2num(dates)
    y = levels
    dt = 24
    
    time = matplotlib.dates.date2num(datetime.timedelta(hours = dt)+dates[0])
    num_spacing = np.linspace(time , x[-1], 2*len(dates))
    date_spacing = matplotlib.dates.num2date(num_spacing)
    
    
    # Using shifted x values, find coefficient of best-fit
    # polynomial f(x) of degree 4
    p_coeff = np.polyfit(x - x[-1], levels, p)
    poly = np.poly1d(p_coeff)

    
    # Plot original data points
    plt.plot(dates, y, label = 'actual')
    plt.plot(date_spacing, poly(num_spacing-x[-1]), color = 'y', label = 'best fit polynomial')
    plt.axhline(y = station.typical_range[1], color = 'r', label = 'high_range')
    plt.axhline(y = station.typical_range[0], color = 'g', label = 'low_range')
    

    plt.legend()
    plt.xlabel('date')
    plt.ylabel('water level(m)')
    plt.xticks(rotation = 45)
    plt.title(f"Station {station.name}")
    
    plt.tight_layout()

    # Display plot
    plt.show()
#   print(poly(num_spacing - x[-1])[0])
    return poly(num_spacing - x[-1])[0]

