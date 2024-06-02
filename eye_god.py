import requests
import json


def get_phone(phone):
    try:
        url = "https://dimondevosint.p.rapidapi.com/main?phone=" + phone
        headers = {
            "X-RapidAPI-Key": "a91007ff89mshea39aae715c870bp192b9cjsn8faa45e0903a",
            "X-RapidAPI-Host": "dimondevosint.p.rapidapi.com"
        }

        response = requests.request("GET", url, headers=headers)
        print(response.text)

        data = json.loads(response.text)

        res = f"""👨 ФИО: {data['name']}
                🏳️ Страна: {data['country']}
                📱 Оператор: {data['operator']}
                📓 Объявления: {data['obyavleniya']}"""

        return res
    except:
        return "Упс, есть ошибка("