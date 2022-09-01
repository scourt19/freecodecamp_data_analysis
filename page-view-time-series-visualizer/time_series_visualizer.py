import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv", index_col="date", parse_dates=True)

# Clean data
bottom = df["value"].quantile(0.025)
top = df["value"].quantile(0.975)
df = df[(df["value"] >= bottom) & (df["value"] <= top)]


def draw_line_plot():
  # Draw line plot
  fig = df.plot(color = "red", xlabel = "Date", ylabel = "Page Views", legend = False, figsize=(18,6)).figure
  plt.title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")

  # Save image and return fig (don't change this part)
  fig.savefig('line_plot.png')
  return fig

def draw_bar_plot():
  df_bar = df.copy()
  df_bar['year'] = df_bar.index.year
  df_bar['month'] = df_bar.index.month
  # Copy and modify data for monthly bar plot
  df_bar = df_bar.groupby(["year", "month"])["value"].mean()
  df_bar = df_bar.unstack()
  
  # Draw bar plot
  months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
  fig = df_bar.plot(kind = "bar", xlabel = "Years", ylabel = "Average Page Views", legend = True, figsize=(15,12)).figure
  plt.legend(title = "Months", labels = months)


  # Save image and return fig (don't change this part)
  fig.savefig('bar_plot.png')
  return fig

def draw_box_plot():
  # Prepare data for box plots (this part is done!)
  df_box = df.copy()
  df_box.reset_index(inplace=True)
  df_box['year'] = [d.year for d in df_box.date]
  df_box['month'] = [d.strftime('%b') for d in df_box.date]

  # Draw box plots (using Seaborn)
  fig, axes = plt.subplots(1, 2, figsize = (25,8))
  sns.boxplot(data = df_box, ax = axes[0], x = "year", y = "value")
  axes[0].set_title("Year-wise Box Plot (Trend)")
  axes[0].set_xlabel("Year")
  axes[0].set_ylabel("Page Views")
  
  month_order = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

  sns.boxplot(data = df_box, ax = axes[1], x = "month", y = "value", order = month_order)
  axes[1].set_title("Month-wise Box Plot (Seasonality)")
  axes[1].set_xlabel("Month")
  axes[1].set_ylabel("Page Views")


  # Save image and return fig (don't change this part)
  fig.savefig('box_plot.png')
  return fig
