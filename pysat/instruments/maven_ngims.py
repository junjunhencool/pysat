# -*- coding: utf-8 -*-
"""Supports the Neutral Gas and Ion Mass Spectrometer
(NGIMS) instrument onboard the Mars Atmosphere and
Volatile Evolution (MAVEN) mission. Downloads data
from the NASA Planetary Data System (PDS).

Parameters
----------
platform : string
    'maven'
name : string
    'ngims'
tag : string
    None Supported

Warnings
--------
- Currently no cleaning routine.
- Module not written by NGIMS team.

"""

from __future__ import print_function
from __future__ import absolute_import
import pandas as pds
import numpy as np
import pysat
import sys
import functools


from . import nasa_cdaweb_methods as cdw

platform = 'maven'
name = 'ngims'
tags = {'csn':['Neutral Composition Data'],
           'ion':['Ion Composition Data']}
sat_ids = {'':''}
test_dates = {'':{'':pysat.datetime(2018,8,1)}}

# support list files routine
# use the default CDAWeb method
fname = 'mvn_ngi_l2_csn-abund-?????_{year:04d}{month:02d}{day:02d}T{hh:02d}{mm:02d}{ss:02d}_v08_r01.csv'
supported_tags = {'':{'':fname}}
list_files = functools.partial(cdw.list_files,
                               supported_tags=supported_tags)
# support load routine
# use pandas csv reader
load = pds.read_csv

# support download routine
# use the default CDAWeb method modified for the PDS website
basic_tag = {'ftp_site':'atmos.nmsu.edu',
            'dir':'/PDS/data/PDS4/MAVEN/ngims_bundle/l2/',
            'remote_fname':'{year:4d}/{month:2d}/'+fname,
            'local_fname':fname}
supported_tags = {'':{'':basic_tag}}
download = functools.partial(cdw.download, supported_tags)


def clean(inst):
    """Routine to return NGIMS data cleaned to the specified level

    Parameters
    -----------
    inst : (pysat.Instrument)
        Instrument class object, whose attribute clean_level is used to return
        the desired level of data selectivity.

    Returns
    --------
    Void : (NoneType)
        data in inst is modified in-place.

    Notes
    --------
    No cleaning currently available for NGIMS
    """

    return None
