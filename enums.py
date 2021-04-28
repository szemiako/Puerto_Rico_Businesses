# Class that holdings our enumerations relevant to this project.
class attributes:
    def __init__(
        self
    ):
        self._default_path = 'C:/Scripts/puerto_rico/'
        self._make_file = True
        self._delimiter = ','
        self._extension = '.csv'
        self._map_path = 'C:/puerto_rico/puerto_rico_shape_file.shx'      

class enums:
    def __init__(
        self
    ):
        self._key = '${SECRET_KEY}'

        self._types = [
            'restaurant',
            'grocery_or_supermarket',
            'point_of_interest',
            'museum',
            'tourist_attraction'
        ]

        self._coordinates = [
            [18.3728082, -65.7296007], # Luquillo
            [18.3332458, -65.6913897], # Fajardo
            [18.2652302, -65.6582447], # Ceiba
            [18.2104218, -65.7464871]  # Naguabo
        ]

        self._properties = [
            'name',
            'types',
            'rating',
            'user_ratings_total',
            'vicinity',
            'open_now',
            'lat',
            'lng'
        ]