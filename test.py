import requests
import pandas as pd


antenna_coordinates = [51.225779846347535, 4.400503131269632]
def get_elevation(coordinates):
    lat, long = coordinates
    query = ('https://api.open-elevation.com/api/v1/lookup'
             f'?locations={lat},{long}')
    r = requests.get(query, verify=False).json()
    elevation = r['results'][0]['elevation']
    return elevation


get_elevation(antenna_coordinates)