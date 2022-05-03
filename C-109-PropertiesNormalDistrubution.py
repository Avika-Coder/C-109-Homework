import pandas as pd
import statistics
import csv
import plotly.figure_factory  as ff
import plotly_express as px 

df=pd.read_csv("height-weight.csv")
height_list=df["Height(Inches)"].to_list()
weight_list=df["Weight(Pounds)"].to_list()
height_mean=statistics.mean(height_list)
weight_mean=statistics.mean(weight_list)
height_median=statistics.mean(height_list)
weight_median=statistics.mean(weight_list)
height_mode=statistics.mean(height_list)
weight_mode=statistics.mean(weight_list)
height_std_deviation=statistics.stdev(height_list)
weight_std_deviation=statistics.stdev(weight_list)
print(height_mean,height_median,height_mode,weight_mean,weight_median,weight_mode,height_std_deviation,weight_std_deviation)

#graph=ff.create_distplot([df["Height(Inches)"].tolist()],["Height"],show_hist=False)
#graph.show()
#graph2=ff.create_distplot([df["Weight(Pounds)"].tolist()],["Weight"],show_hist=False)
#graph2.show()