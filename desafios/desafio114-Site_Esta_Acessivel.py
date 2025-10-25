import requests
from requests.exceptions import HTTPError

url = "https://www.pudim.com.br/"
try:
    resp = requests.get(url)
    resp.raise_for_status()
except Exception:
    print(f'O site Pudim não está acessível no momento.')
else:
    print('Consegui acessar o site Pudim com sucesso!')

