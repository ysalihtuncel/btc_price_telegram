import requests

pair = 'BTCUSDT'
telegram_bot_token = ''
telegram_chat_id = ''


def telegram_bot_send_message(message):
    try:
        send_text = 'https://api.telegram.org/bot' \
                    + telegram_bot_token + '/sendMessage?chat_id=' + telegram_chat_id + \
                    '&parse_mode=Markdown&text=' + message

        response = requests.get(send_text)

        return response
    except:
        print("Something went wrong")


def get_binance_value(pair=pair):
    try:
        url = 'https://api.binance.com/api/v3/avgPrice?symbol={pair}'.format(pair=pair)

        response = requests.get(url=url)
        response = response.json()
        return response.get('price')
    except:
        print("Something went wrong")


telegram_bot_send_message(get_binance_value())
