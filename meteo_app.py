import streamlit as st
import requests
from datetime import datetime, date
import json

st.title('Meteo città')

API_key ='b97e9616f2a3d59278dd296a41a59467'
city_name = st.text_input('Please write the city')

if city_name:
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}'
    result = requests.get(url)
    json = result.json()

    now = datetime.now()
    #st.write(f'Oggi è {now.date()}')
    st.write(f'Il meteo di oggi {now.day}/{now.month}/{now.year}')
    st.write('')
    
    temp = json['main']['temp'] -273.15
    st.write(f'Temperatura - {round(temp, 2)} °C')

    perc = json['main']['feels_like'] -273.15
    st.write(f'Temperatura percepita - {round(perc, 2)} °C')

    temp_min = json['main']['temp_min'] -273.15
    st.write(f'Temperatura minima - {round(temp_min, 2)} °C')

    temp_max = json['main']['temp_max'] -273.15
    st.write(f'Temperatura massima - {round(temp_max, 2)} °C')

    pressione = json['main']['pressure']
    st.write(f'Pressione: {round(pressione, 2)} hPa')

    umidita = json['main']['humidity']
    st.write(f'Umidità: {round(umidita, 2)} %')

    vento = json['wind']['speed']
    st.write(f'Vento velocità: {round(vento, 2)} m/s')


# valori = list(json['main'].keys())
# print(valori)

# for i in valori:
#     var = json['main'][i]
#     st.write(f'{i}= {var}')
