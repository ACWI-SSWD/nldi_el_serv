'''Console script for nldi_el_serv.'''
import sys
import click
# import numpy as np
from nldi_el_serv.nldi_el_serv import getXSAtPoint, getXSAtEndPts
# import geopandas as gpd
# import pandas as pd
# import json


class NLDI_El_Serv:
    def __init__(self):
        self.out_crs = 'epsg:4326'

    def setoutCRS(self, out_crs='epsg:4326'):
        self.out_crs = out_crs

    def outCRS(self):
        return self.out_crs

    def __repr__(self):
        return f'NLDI_El_Serv {self.out_crs}'


pass_nldi_el_serv = click.make_pass_decorator(NLDI_El_Serv)


@click.group()
@click.option('--outcrs',
              default='epsg:4326',
              help='Projection CRS to return cross-section geometry: default is epsg:4326')
@click.version_option('0.1')
@click.pass_context
def main(ctx, outcrs):
    '''NLDI_El_Serv is a command line tool to for elevation-based services to the NLDI'''

    ctx.obj = NLDI_El_Serv()
    ctx.obj.setoutCRS(outcrs)
    return 0

# XS command at point with NHD


@main.command()
@click.option('--file',
              required=True,
              type=click.File('w'),
              help='Output json file')
@click.option('--latlon',
              required=True,
              # nargs=2,
              type=tuple((float, float)),
              # default=(-103.80119199999999, 40.268403),
              help='format lat lon as floats for example lat lon or -103.8011 40.2684')
@click.option('--numpoints',
              default=100,
              type=int,
              help='number of points in cross-section')
@click.option('--width',
              default=1000.0,
              type=float,
              help='width of cross-section')
@pass_nldi_el_serv
def XSAtPoint(nldi_el_serv, latlon, numpoints, width, file):
    lat = latlon[0]
    lon = latlon[1]
    print(f'input={latlon}, lat={lat}, lon={lon}, \
    npts={numpoints}, width={width} and crs={nldi_el_serv.outCRS()} and \
    file={file} and out_epsg={nldi_el_serv.outCRS()}')
    # print(tuple(latlon))
    xs = getXSAtPoint(point=tuple((lat, lon)),
                      numpoints=numpoints,
                      width=width,
                      file=file)
    # jsdict = xs.to_crs(xstool.out_crs).to_dict() #.to_crs(xstool.out_crs)
    # # print(type(jsdict))
    # # print(jsdict)
    # json.dump(xs.to_dict(), file)
    return xs
    # df = pd.DataFrame({'elevation':xs.elevation.values,
    #                    'Latitude':xs.coords.y.values,
    #                    'Longitude':xs.coords.x.values})
    # gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df.Longitude, df.Latitude))
    # return gdf.to_json()

# XS command at user defined endpoints


@main.command()
@click.option('--file',
              required=True,
              type=click.File('w'),
              help='Output json file')
@click.option('-s', '--latlon1',
              required=True,
              type=tuple((float, float)),
              help='format lat lon pair as floats for example lat lon or  40.267335 -103.801134  40.272798 -103.800787')
@click.option('-e', '--latlon2',
              required=True,
              type=tuple((float, float)),
              help='format lat lon pair as floats for example lat lon or  40.267335 -103.801134  40.272798 -103.800787')
@click.option('--numpoints',
              default=100,
              type=int,
              help='number of points in cross-section')
@pass_nldi_el_serv
def XSAtEndPts(nldi_el_serv, latlon1, latlon2, numpoints, file):
    lat1 = latlon1[0]
    lon1 = latlon1[1]
    lat2 = latlon2[0]
    lon2 = latlon2[1]
    nl = '\n'
    print(
        f'input:  {nl}, \
        start: {latlon1}, {nl}, \
        end: {latlon2}, {nl}, \
        lat1:{lat1}, lon1:{lon1}, {nl}, \
        lat2:{lat2}, lon2:{lon2}, {nl}, \
        npts={numpoints},  {nl}, \
        crs={nldi_el_serv.outCRS()}  {nl}, \
        file={file}, {nl}, \
        out_epsg={nldi_el_serv.outCRS()} {nl}'
        )
    path = []
    path.append(latlon1)
    path.append(latlon2)
    print(type(path))
    xs = getXSAtEndPts(path=path, numpts=numpoints, file=file)
    print(xs)


@main.command()
@click.option('--file',
              required=True,
              type=click.File('w'),
              help='Output json file')
@click.option('--latlon',
              required=True,
              type=list,
              help='format lat lon pair as floats for example lat lon or  40.267335 -103.801134  40.272798 -103.800787')
@click.option('--numpoints',
              default=100,
              type=int,
              help='number of points in cross-section')
@pass_nldi_el_serv
def XSAtEndPts2(nldi_el_serv, latlon, numpoints, file):
    lat1 = latlon[0][0]
    lon1 = latlon[0][1]
    lat2 = latlon[1][0]
    lon2 = latlon[1][1]
    nl = '\n'
    print(
        f'input:  {nl}, \
        {latlon}, {nl}, \
        lat1:{lat1}, lon1:{lon1}, {nl}, \
        lat2:{lat2}, lon2:{lon2}, {nl}, \
        npts={numpoints},  {nl}, \
        crs={nldi_el_serv.outCRS()}  {nl}, \
        file={file}, {nl},  \
        out_epsg={nldi_el_serv.outCRS()} {nl}'
        )


if __name__ == '__main__':
    sys.exit(main())  # pragma: no cover
