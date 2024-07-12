import streamlit as st
import requests
import datetime
from time import strftime

'''
# TaxiFareModel front
'''


date = st.date_input('Date')
time = st.time_input('Time')
pickup_location = st.text_input('Your adress', '')
dropoff_location = st.text_input('Where do you want to go ?', '')
passenger_count = st.number_input('Passenger count', step=1, min_value=1, max_value=4)


def coordinates(address):
    '''
Requête sur api Nomatim pour obtenir les latitudes et longitudes
'''
    url = "https://nominatim.openstreetmap.org/search"
    params = {
        'q': address,
        'format': 'json'
    }
    response = requests.get(url, params=params).json()
    return (response[0]['lat'], response[0]['lon'])


pickup_latitude, pickup_longitude = coordinates(pickup_location)
dropoff_latitude, dropoff_longitude = coordinates(dropoff_location)

info_api = {'pickup_datetime': f'{date} {time}',
            'pickup_longitude': pickup_longitude,
            'pickup_latitude': pickup_latitude,
            'dropoff_longitude': dropoff_longitude,
            'dropoff_latitude': dropoff_latitude,
            'passenger_count': passenger_count
            }

def pred(info_api: dict):
    url = 'https://taxifare.lewagon.ai/predict'
    params = info_api

    response = requests.get(url, params=params).json()
    return response

if st.button('predict my course'):
    st.text_input('Fare estimated for your drive', pred(info_api)['fare'])




