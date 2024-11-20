# Create a scatter plot of fares and distances
import matplotlib.pyplot as plt
import pandas as pd
import mpl_toolkits.mplot3d import Axes3D

trips_df = pd.read_json("../Trips from area 8.json")

trips_g_1 = trips_df[['trip_miles', 'fare', 'dropoff_community_area']].query('trip_miles > 1')

fare_series = trips_gt_1.fare
trip_miles = trips_gt_1.trip_miles
dropoff_area = trip_gt_1.dropoff_community_area

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Put fare series on the x axis, dropoff area on the acis, miles on the y acis
ax.scatterplot

