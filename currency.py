import requests
import json

# http://api.nbp.pl/#kursyWalut

currency = "USD"

url_scheme = 'http://api.nbp.pl/api/exchangerates/rates/A/{code}/?format=json'
url = url_scheme.format(code=currency)

resp = requests.get(url)

data = json.loads(resp.content.decode('ISO-8859-1'))
print(data['rates'][0]['mid'])
