import api_helper
import enums
import geopandas as gpd
import pandas as pd
from pandas import DataFrame
from shapely.geometry import Point, Polygon

def get_value(data, attribute):
    return data.get(attribute, None)

def make_data_set(data, records=[]): 
    return [list(record(data=datum).__dict__.values()) for ind in range(len(data)) for datum in data[ind]['results']]

def columns_to_numeric():
    return [
        'rating',
        'user_ratings_total',
        'lat',
        'lng'
    ]

def clean_numeric(column):
    column = column.replace(str(None), 0)
    column = pd.to_numeric(column)
    return column

def make_df(data=make_data_set(data_set)):
    df = pd.DataFrame(data, columns = enums.enums()._properties)

    for column in columns_to_numeric():
        df[column] = clean_numeric(df[column])

    df['Coordinates'] = list(zip(df['lat'], df['lng']))
    df['Coordinates'] = df['Coordinates'].apply(Point)
    return df

def make_business_gdf(df):
    return gpd.GeoDataFrame(df, crs={'init':'epsg:2263'}, geometry=df.Coordinates)

def make_map_gdf():
    return gpd.GeoDataFrame.from_file(enums.attributes()._map_path)

class record:
    def __init__(
        self,
        data
    ):
        self._data = data
        self._name = get_value(self._data, 'name')
        self._types = get_value(self._data, 'types')
        self._rating = get_value(self._data, 'rating')
        self._user_ratings_total = get_value(self._data, 'user_ratings_total')
        self._vicinity = get_value(self._data, 'vicinity')
        self._open = self._get_status()
        self._lat = get_value(self._data['geometry']['location'], 'lat')
        self._lon = get_value(self._data['geometry']['location'], 'lng')

    def _get_status(self):
        if get_value(self._data, 'opening_hours'):
            return get_value(self._data['opening_hours'], 'open_now')
        else:
            return None