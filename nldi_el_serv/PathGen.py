import numpy as np
from shapely.geometry import LineString, Point
import geopandas as gpd
import pandas as pd


class PathGen:

    def __init__(self, path_geom, ny) -> None:
        print(path_geom, ny)
        self.path_geom = path_geom
        self.width = self.path_geom.geometry[0].length
        self.ny = ny
        self.x = np.zeros(self.ny+1, dtype=np.double)
        self.y = np.zeros(self.ny+1, dtype=np.double)
        self.int_path = None
        self._buildpath()

    def _buildpath(self):
        line = self.path_geom.geometry[0]
        spacing = line.length/self.ny
        d = 0.0
        index = 0
        while d < self.width:
            point = line.interpolate(d)
            self.x[index] = point.x
            self.y[index] = point.y
            d += spacing
            index += 1

    def get_xs(self):
        points = gpd.GeoSeries(map(Point, zip(self.x, self.y)))
        ls = LineString((points.to_list()))
        d = {0: {'name': 'section-path', 'geometry': ls}}
        df = pd.DataFrame.from_dict(d, orient='index')
        gdf = gpd.GeoDataFrame(df, geometry=df.geometry, crs=self.path_geom.crs)
        return gdf

    def get_xs_points(self):
        return self.x, self.y