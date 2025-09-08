import osmnx as ox
from osgeo import gdal
import geopandas as gpd
import matplotlib.pyplot as plt
import shapely
import os
print(gdal.GetDriverCount())

study_point = shapely.Point(-9.1393, 38.7223)  # Latitude and Longitude for Lisbon
study_geom = gpd.GeoSeries([study_point], crs=4326)
study_polygon = study_geom.to_crs(epsg=3857).buffer(6000).to_crs(epsg=4326).unary_union
study_polygon_gpd = gpd.GeoDataFrame(geometry=[study_polygon], crs="EPSG:4326")
# Read-in geosjon already saved from R
study_polygon = gpd.read_file("lisbon_study_area.geojson")
# study_polygon_gpd.explore()
tags = {"highway": True, "maxspeed": True, "lit": True, "cycleway": True}
gdf = ox.features_from_polygon(study_polygon, tags)
gdf = gdf[gdf.geom_type.isin(["LineString", "MultiLineString"])]
gdf = gdf.to_crs(epsg=3857)
gdf.plot(column="maxspeed", figsize=(10, 10), legend=True)
plt.show()