import netCDF4

# OPeNDAP.
url = 'http://geoport-dev.whoi.edu/thredds/dodsC/estofs/atlantic'
with netCDF4.Dataset(url) as nc:
    # Compiled with cython.
    assert nc.filepath() == url


url = 'http://geoport.whoi.edu/thredds/dodsC/usgs/vault0/models/tides/vdatum_gulf_of_maine/adcirc54_38_orig.nc'

with netCDF4.Dataset(url) as nc:
    nc['tidenames'][:]

# Fails with libnetcdf 4.6.1
url = 'http://data.oceansmap.com/thredds/dodsC/EDS/WCOFS'

import numpy as np
with netCDF4.Dataset(url) as nc:
    x = nc['lon_rho'][:]
    y = nc['lat_rho'][:]


print('coords')
print(np.min(x), np.max(x), np.min(y), np.max(y))
assert np.min(np.abs(x)) > 0
