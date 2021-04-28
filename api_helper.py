import data_helper
import enums
import json
import urllib.request

def url_builder(lat, lon, kind, key=enums.enums()._key):
    # This 'Nearby Search' request allows us to simply specify lat / lon
    # coordinates and the desired centroid pair. Can filter by types.
    return'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={0},{1}&radius=50000&type={2}&key={key}'.format(
        str(lat),
        str(lon),
        str(kind),
        key=key
    )

def next_page_url(page_token, key=enums.enums()._key):
    return 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?pagetoken={0}&key={key}'.format(
        page_token,
        key=key
    )

def url_list(coordinates=enums.enums()._coordinates, types=enums.enums()._types):
    return [url_builder(c[0], c[1], t) for c in coordinates for t in types]

def get_data(url):
    with urllib.request.urlopen(url) as url:
        data = json.loads(url.read().decode())
    return data

def data_list():
    return list(map(get_data, url_list()))

def fetch_data(data=data_list()):
    for datum in data:
        next_page = data_helper.get_value(datum, 'next_page_token')
        
        while next_page is not None:
            next_page_datum = get_data(next_page_url(next_page))
            data.append(next_page_datum)
            next_page = data_helper.get_value(next_page_datum, 'next_page_token')
            
    return data