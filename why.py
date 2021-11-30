$ pip install httplib2
from json import dumps

from httplib2 import Http


def main():
    """Hangouts Chat incoming webhook help."""
    url = 'https://chat.googleapis.com/v1/spaces/AAAAY2dqo2Y/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=SqeMfMoOM8m09sdegvpYYQtQg-qjhJUv_KzIPNo4eKc%3D'
    bot_message = {
        'text' : 'poo poo'}

    message_headers = {'Content-Type': 'application/json; charset=UTF-8'}

    http_obj = Http()

    response = http_obj.request(
        uri=url,
        method='POST',
        headers=message_headers,
        body=dumps(bot_message),
    )

    print(response)

if __name__ == '__main__':
    main()
$ python3 help.py
    
