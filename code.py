import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import csv
import random

df = pd.read_csv("data.csv")
data = df["Math_score"].tolist()
fig = ff.create_distplot([data], ["Math Scores"], show_hist=False)
fig.show()
mean=statistics.mean(data)
std_deviation=statistics.stdev(data)
print(mean)
print(std_deviation)