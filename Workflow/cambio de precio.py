from prefect import task, Flow
import requests
from bs4 import BeautifulSoup
import time

@task
def get_price():
    url = 'https://ddtech.mx/producto/computadora-pride-msi-pro-white-amd-ryzen-7-7700x-rtx-4070-32gb-ram-1tb-m-2-enf-liquido-240mm-650w-80-bronze?id=14827'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    price = soup.find('span', {'class': 'price'}).text
    return price

@task
def check_price_change(current_price, old_price=31999.00):
    if current_price != old_price:
        print(f'El precio ha cambiado a {current_price}')

with Flow('Monitor Price') as flow:
    current_price = get_price()
    check_price_change(current_price)

while True:
    flow.run()
    time.sleep(3600)
