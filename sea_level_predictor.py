import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']

    # Create scatter plot
    # Use matplotlib to create a scatter plot using the "Year" column as the x-axis 
    # and the "CSIRO Adjusted Sea Level" column as the y-axix.
    fig, ax = plt.subplots()
    plt.scatter(x, y)

    # Create first line of best fit
    # Use the linregress function from scipy.stats to get the slope and y-intercept 
    # of the line of best fit. Plot the line of best fit over the top of the scatter plot. 
    # Make the line go through the year 2050 to predict the sea level rise in 2050.
    res = linregress(x, y)
    x_pred = pd.Series([i for i in range(1880, 2051)])
    y_pred = res.slope*x_pred + res.intercept # mx + b
    plt.plot(x_pred, y_pred, 'r')

    # Create second line of best fit
    # Plot a new line of best fit just using the data from year 2000 through the most 
    # recent year in the dataset. Make the line also go through the year 2050 to predict 
    # the sea level rise in 2050 if the rate of rise continues as it has since the year 2000.
    new_df = df[df['Year'] >= 2000]
    new_x = new_df['Year']
    new_y = new_df['CSIRO Adjusted Sea Level']
    res_2 = linregress(new_x, new_y)
    x_pred2 = pd.Series([i for i in range(2000, 2051)])
    y_pred2 = res_2.slope*x_pred2 + res_2.intercept # mx + b
    plt.plot(x_pred2, y_pred2, 'g')

    # Add labels and title
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()