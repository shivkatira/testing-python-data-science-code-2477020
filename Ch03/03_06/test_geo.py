import numpy as np
from geo import haversine
from hypothesis import given
from hypothesis.strategies import floats

lat_strategy = floats(-90, 90, allow_nan=False)
lng_strategy = floats(-180, 180, allow_nan=False)


@given(lat1=lat_strategy, lng1=lng_strategy, lat2=lat_strategy, lng2=lng_strategy)
def test_haversine(lat1, lng1, lat2, lng2):
    dist = haversine(lat1, lng1, lat2, lng2)
    if not np.isnan(dist):
        assert dist >= 0
