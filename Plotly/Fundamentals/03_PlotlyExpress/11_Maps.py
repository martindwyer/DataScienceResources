import plotly.express as px
from environment import Env

px.set_mapbox_access_token(Env.MAPBOX_TOKEN)

df = px.data.carshare()

fig = px.scatter_mapbox(df, 
                        lat="centroid_lat", 
                        lon="centroid_lon",
                        color="peak_hour", 
                        size="car_hours", 
                        color_continuous_scale=px.colors.cyclical.IceFire,
                        size_max=15, zoom=10)
fig.show()


df = px.data.carshare()
fig = px.line_mapbox(df, 
                     lat="centroid_lat", 
                     lon="centroid_lon", 
                     color="peak_hour")
fig.show()


df = px.data.gapminder()

fig = px.scatter_geo(df, 
                     locations="iso_alpha", 
                     color="continent", 
                     hover_name="country", 
                     size="pop",
                     animation_frame="year", 
                     projection="natural earth")
fig.show()

fig = px.line_geo(df.query("year==2007"), 
                  locations="iso_alpha", 
                  color="continent", 
                  projection="orthographic")
fig.show()


fig = px.choropleth(df, 
                    locations="iso_alpha", 
                    color="lifeExp", 
                    hover_name="country", 
                    animation_frame="year", 
                    range_color=[20,80])
fig.show()