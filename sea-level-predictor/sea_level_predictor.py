import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
  # Read data from file
  df = pd.read_csv("epa-sea-level.csv")

  # Create scatter plot
  plt.scatter(data = df, x="Year", y="CSIRO Adjusted Sea Level", color = "red")

  # Create first line of best fit
  slope, intercept, r_value, p_value, std_err = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])

  first_year = df.iloc[0, 0]
  x_pred = list(range(first_year, 2051))
  y_pred = [x * slope + intercept for x in x_pred]
  plt.plot(x_pred, y_pred, color="blue")

  # Create second line of best fit
  new_df = df[df["Year"] >= 2000]
  slope, intercept, r_value, p_value, std_err = linregress(new_df["Year"], new_df["CSIRO Adjusted Sea Level"])

  new_x = list(range(2000, 2051))
  new_y = [x * slope + intercept for x in new_x]
  plt.plot(new_x, new_y, color="black")
  # Add labels and title
  plt.xlabel("Year")
  plt.ylabel("Sea Level (inches)")
  plt.title("Rise in Sea Level")
    
  # Save plot and return data for testing (DO NOT MODIFY)
  plt.savefig('sea_level_plot.png')
  return plt.gca()