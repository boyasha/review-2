import requests
import xmltodict
import json

link = 'https://www.cbr-xml-daily.ru/daily_json.js'
past_link = 'http://www.cbr.ru/scripts/XML_daily.asp?date_req='

DATA = requests.get(link).json()


def return_past_api(date):
    past_DATA = requests.get(past_link+date)
    dict_data = xmltodict.parse(past_DATA.content)
    return dict_data
