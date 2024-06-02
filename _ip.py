import requests
import socket
import http.client


def get_ip_by_hostname(url):
    try:
        return f'{url}\n IP: {socket.gethostbyname(url)}'
    except:
        return f'Какая то ошибка!'


def get_my_ip():
    conn = http.client.HTTPConnection("ifconfig.me")
    conn.request("GET", "/ip")
    return conn.getresponse().read()


def get_info_by_ip(ip='213.24.134.169'):
    try:
        responce = requests.get(url=f'http://ip-api.com/json/{ip}').json()

        data = {
            '[IP]': responce.get('query'),
            '[Int prov]': responce.get('isp'),
            '[Org]': responce.get('org'),
            '[Country]': responce.get('country'),
            '[Region Name]': responce.get('regionName'),
            '[City]': responce.get('city'),
            '[ZIP]': responce.get('zip'),
            '[Lat]': responce.get('lat'),
            '[Lon]': responce.get('lon')
        }

        str_res = ''
        for k,v in data.items():
            str_res += f'{k} >> {v}\n'

        return str_res
    except requests.exceptions.ConnectionError:
        return '[!] Что-то не то!'