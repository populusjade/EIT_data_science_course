import osmnx as ox
import geopandas as gpd
import matplotlib.pyplot as plt
import shapely
import os
import fiona

study_point = shapely.Point(-9.1393, 38.7223)  # Latitude and Longitude for Lisbon
print(study_point)
study_geom = gpd.GeoSeries([study_point], crs=4326)
print(study_geom)
study_polygon = study_geom.to_crs(epsg=3857).buffer(6000).to_crs(epsg=4326).union_all()
print(study_polygon)
study_polygon_gpd = gpd.GeoDataFrame(geometry=[study_polygon], crs="EPSG:4326")
# Read-in geosjon already saved from R
study_polygon = gpd.read_file("C:/Jun/EIT_Urban mobility application/EIT_data_science_course/lisbon_study_area.geojson")
# study_polygon_gpd.explore()
tags = {"highway": True, "maxspeed": True, "lit": True, "cycleway": True}
gdf = ox.features_from_polygon(study_polygon, tags)
gdf = gdf[gdf.geom_type.isin(["LineString", "MultiLineString"])]
gdf = gdf.to_crs(epsg=3857)
gdf.plot(column="maxspeed", figsize=(10, 10), legend=True)
plt.show()