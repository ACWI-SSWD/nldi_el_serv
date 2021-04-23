#!/usr/bin/env python


import pytest

from nldi_el_serv.nldi_el_serv import getXSAtEndPts
from tempfile import NamedTemporaryFile

with NamedTemporaryFile(mode='w+') as tf:
    @pytest.mark.parametrize(
                                'path, mumpts, crs, file, res',
                                [
                                    ([(-107.077270, 39.643839), (-107.078088, 39.644977)], 101, 'crs:84', tf, 1),
                                    ([(-104.8195510, 40.116538), (-104.817563, 40.116721)], 101, 'crs:84', tf, 10),
                                ]
    )
    def run_getXSAtEndPts(path, numpts, crs, file, res):
        getXSAtEndPts(path=path, numpts=numpts, crs=crs, file=file, res=res)
