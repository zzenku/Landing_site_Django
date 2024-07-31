import requests
from .models import TeleSettings

token = '7325613304:AAGOO-xh9oxPn_hvGP4wkKpPm7qugHWxGuQ'
chat_id = '-4276887254'
text = 'TestMessage'


def sendTelegram(tg_name, tg_phone):
    if TeleSettings.objects.get(pk=1):
        settings = TeleSettings.objects.get(pk=1)
        token = str(settings.tg_token)
        chat_id = str(settings.tg_chat)
        text = str(settings.tg_message)
        api = 'https://api.telegram.org/bot'
        method = api + token + '/sendMessage'

        if text.find('{') and text.find('}') and text.rfind('{') and text.rfind(
                '}'):
            part_1 = text[0:text.find('{')]
            part_2 = text[text.find('}') + 1:text.rfind('{')]
            part_3 = text[text.rfind('}'): -1]

            text_slice = part_1 + tg_name + part_2 + tg_phone + part_3
        else:
            text_slice = text

        try:
            req = requests.post(method, data={
                'chat_id': chat_id,
                'text': text_slice
            })
        except:
            pass

        finally:
            if req.status_code == 500:
                print('Ошибка 500')
            elif req.status_code != 200:
                print('Ошибка отправки!')
            else:
                print('Сообщение отправлено')
    else:
        pass
