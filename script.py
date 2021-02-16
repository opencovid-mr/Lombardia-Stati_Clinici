import requests

from datetime import datetime

url='https://hub.dati.lombardia.it/resource/7jw9-ygfv.csv'

filename='data/'+datetime.today().strftime('%Y-%m-%d')+'.csv'

req = requests.get(url)
csv_file = open(filename, 'wb')

csv_file.write(req.content)
csv_file.close()
