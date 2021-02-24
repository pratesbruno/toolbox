from math import radians, sin, cos, asin, sqrt
import matplotlib.pyplot as plt
import seaborn as sns


def haversine(lon1, lat1, lon2, lat2):
    """
    Compute distance between two pairs of (lat, lng)
    See - (https://en.wikipedia.org/wiki/Haversine_formula)
    """
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    return 2 * 6371 * asin(sqrt(a))