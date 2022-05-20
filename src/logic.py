import src.api as api
import datetime


def return_all_currency():
    result_string = 'Список всех валют поддерживаемых ботом (имя валюты: сокращение валюты):\n\n'
    short_name_of_currency = api.DATA['Valute'].keys()

    for item in short_name_of_currency:
        result_string += api.DATA['Valute'][item]["Name"] + ' : ' + item + '\n'

    return result_string


def return_price_of_currency(short_name_of_currency):
    date = datetime.datetime.now()
    date_string = date.strftime("%d/%m/%y")
    nominal = api.DATA['Valute'][short_name_of_currency]['Nominal']
    price = api.DATA['Valute'][short_name_of_currency]['Value']
    past_price = api.DATA['Valute'][short_name_of_currency]['Previous']

    try:
        result_string = f"На: {date_string} \n"
        result_string += f"{nominal} {short_name_of_currency} = {price} RUB\n\n"
        result_string += f"Предыдущий день:\n"
        result_string += f"{nominal} {short_name_of_currency} = {past_price} RUB\n"
    except Exception as exc:
        result_string = "Я не знаю такую валюту"

    return result_string


def return_two_price_of_currency(short_name_of_currency):
    short_name_of_currency = short_name_of_currency.split("/")
    short_name_of_currency_1 = short_name_of_currency[0]
    short_name_of_currency_2 = short_name_of_currency[1]

    date = datetime.datetime.now()
    date_string = date.strftime("%d/%m/%y")

    nominal_1 = api.DATA['Valute'][short_name_of_currency_1]['Nominal']
    nominal_2 = api.DATA['Valute'][short_name_of_currency_2]['Nominal']
    price_1 = api.DATA['Valute'][short_name_of_currency_1]['Value']
    price_2 = api.DATA['Valute'][short_name_of_currency_2]['Value']
    past_price_1 = api.DATA['Valute'][short_name_of_currency_1]['Previous']
    past_price_2 = api.DATA['Valute'][short_name_of_currency_2]['Previous']

    try:
        result_string = f"На: {date_string} \n"
        result_string += f"{nominal_1} {short_name_of_currency_1} = " \
                         f"{round(price_1 / price_2 * nominal_2, 4)} {short_name_of_currency_2}\n\n"
        result_string += f"Предыдущий день:\n"
        result_string += f"{nominal_1} {short_name_of_currency_1} = " \
                         f"{round(past_price_1 / past_price_2 * nominal_2, 4)} {short_name_of_currency_2}\n"
    except Exception as exc:
        result_string = "Я не знаю такую валюту"

    return result_string


def return_past_price_of_currency(input_data):
    try:
        input_data = input_data.split(" ")
        date = input_data[0]
        short_name_of_currency = input_data[1]
    except Exception as exc:
        return "Неправильные входные данные!"
    past_DATA = api.return_past_api(date)

    for i in past_DATA['ValCurs']['Valute']:
        if i['CharCode'] == short_name_of_currency:
            nominal = i['Nominal']
            price = i['Value']

    try:
        result_string = f"На: {date} \n\n"
        result_string += f"{nominal} {short_name_of_currency} = {price} RUB\n\n"
    except Exception as exc:
        result_string = "Я не знаю такую валюту"

    return result_string


def return_two_past_price_of_currency(input_data):
    input_data = input_data.split(" ")
    date = input_data[0]

    short_name_of_currency = input_data[1].split('/')
    short_name_of_currency_1 = short_name_of_currency[0]
    short_name_of_currency_2 = short_name_of_currency[1]

    past_DATA = api.return_past_api(date)

    for i in past_DATA['ValCurs']['Valute']:
        if i['CharCode'] == short_name_of_currency_1:
            nominal_1 = i['Nominal']
            price_1 = i['Value']

    for i in past_DATA['ValCurs']['Valute']:
        if i['CharCode'] == short_name_of_currency_2:
            nominal_2 = i['Nominal']
            price_2 = i['Value']
    index = price_1.find(',')
    price_1 = price_1[:index] + '.' + price_1[1 + index:]
    index = price_2.find(',')
    price_2 = price_2[:index] + '.' + price_2[1 + index:]
    try:
        result_string = f"На: {date} \n\n"
        result_string += f"{nominal_1} {short_name_of_currency_1} = " \
                         f"{round(float(price_1) / float(price_2) * float(nominal_2), 4)} {short_name_of_currency_2}\n\n"

    except Exception as exc:
        result_string = "Я не знаю такую валюту"

    return result_string
