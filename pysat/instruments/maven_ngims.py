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
    'csn' or 'ion'
sat_id : string
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
tags = {'csn': 'Neutral Composition Data',
        'ion': 'Ion Composition Data'}
sat_ids = {'': ['csn', 'ion']}
test_dates = {'': {'csn': pysat.datetime(2018, 8, 1)},
              '': {'ion': pysat.datetime(2018, 8, 1)}}

# support list files routine
# use the default CDAWeb method
fname = ''.join(['mvn_ngi_l2_csn-abund-?????_{year:04d}{month:02d}',
                 '{day:02d}T??????_v08_r01.csv'])
supported_tags = {'': {'csn': fname},
                  '': {'ion': fname}}
list_files = functools.partial(cdw.list_files,
                               supported_tags=supported_tags)
# support load routine
# use pandas csv reader
load = pds.read_csv

# support download routine
# use the default CDAWeb method modified for the PDS website
basic_tag = {'remote_site': 'https://atmos.nmsu.edu',
             'dir': '/PDS/data/PDS4/MAVEN/ngims_bundle/l2/',
             'remote_fname': '{year:04d}/{month:02d}/' + fname,
             'local_fname': fname}
supported_tags = {'': {'csn': basic_tag},
                  '': {'ion': basic_tag}}
download = functools.partial(cdw.download, supported_tags, multi_file_day=True)

# support listing files currently on CDAWeb
list_remote_files = functools.partial(cdw.list_remote_files,
                                      supported_tags=supported_tags)


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
