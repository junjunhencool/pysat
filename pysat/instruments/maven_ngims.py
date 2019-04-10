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
import pysat
import functools


from . import nasa_cdaweb_methods as cdw

platform = 'maven'
name = 'ngims'
tags = {'csn': 'Neutral Composition Data',
        'ion': 'Ion Composition Data'}
sat_ids = {'': ['csn', 'ion']}
test_dates = {'': {'csn': pysat.datetime(2018, 8, 1),
                   'ion': pysat.datetime(2018, 8, 1)}}

# support list files routine
# use the default CDAWeb method
fname1 = ''.join(['mvn_ngi_l2_csn-abund-?????_{year:04d}{month:02d}',
                  '{day:02d}T??????_v08_r01.csv'])
fname2 = ''.join(['mvn_ngi_l2_ion-abund-?????_{year:04d}{month:02d}',
                  '{day:02d}T??????_v08_r01.csv'])
supported_tags = {'': {'csn': fname1,
                       'ion': fname2}}

multi_file_day = True

list_files = functools.partial(cdw.list_files,
                               supported_tags=supported_tags)
# support download routine
# use the default CDAWeb method modified for the PDS website
basic_tag1 = {'dir': '/PDS/data/PDS4/MAVEN/ngims_bundle/l2/',
              'remote_fname': '{year:04d}/{month:02d}/' + fname1,
              'local_fname': fname1}
basic_tag2 = {'dir': '/PDS/data/PDS4/MAVEN/ngims_bundle/l2/',
              'remote_fname': '{year:04d}/{month:02d}/' + fname2,
              'local_fname': fname2}
supported_tags = {'': {'csn': basic_tag1,
                       'ion': basic_tag2}}
download = functools.partial(cdw.download, supported_tags,
                             remote_site='https://atmos.nmsu.edu',
                             multi_file_day=multi_file_day)

# support listing files currently on CDAWeb
list_remote_files = functools.partial(cdw.list_remote_files,
                                      remote_site='https://atmos.nmsu.edu',
                                      supported_tags=supported_tags)


def load(fnames, tag=None, sat_id=None):
    """Load Kp index files

    Parameters
    ------------
    fnames : (pandas.Series)
        Series of filenames
    tag : (str or NoneType)
        tag or None (default=None)
    sat_id : (str or NoneType)
        satellite id or None (default=None)

    Returns
    ---------
    data : (pandas.DataFrame)
        Object containing satellite data
    meta : (pysat.Meta)
        Object containing metadata such as column names and units

    Notes
    -----
    Called by pysat. Not intended for direct use by user.


    """

    data = pds.read_csv(fnames[0], index_col=0, parse_dates=True)
    for fname in fnames[1:]:
        new_data = pds.read_csv(fname, index_col=0, parse_dates=True)
        data = data.append(new_data, sort=True)

    # TODO: sort data by mass

    meta = pysat.Meta()

    # TODO: add metadata from columns

    return data, meta


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
