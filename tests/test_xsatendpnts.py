#!/usr/bin/env python


import pytest

from nldi_el_serv.nldi_el_serv import getXSAtEndPts
from tempfile import NamedTemporaryFile


@pytest.mark.parametrize(
                            'path, numpts, crs, file, res',
                            [
                                ([(-107.077270, 39.643839), (-107.078088, 39.644977)], 101, 'epsg:4326', None, 1),
                                ([(-104.8195510, 40.116538), (-104.817563, 40.116721)], 101, 'epsg:4326', None, 10),
                            ]
)
def test_run_getXSAtEndPts(path, numpts, crs, file, res):
    with NamedTemporaryFile(mode='w+') as tf:
        xs = getXSAtEndPts(path=path, numpts=numpts, crs=crs, file=tf, res=res)
        assert(xs == 0)
