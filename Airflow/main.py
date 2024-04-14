from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
import requests
from bs4 import BeautifulSoup

def extract_discounts():
    url = "https://ddtech.mx/"
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        products = soup.find_all("div", class_="product")

        if products:
            product_data = []
            for product in products:
                product_name_elem = product.find("h3", class_="name")
                price_elem = product.find("span", class_="price")
                if product_name_elem and price_elem:
                    product_name = product_name_elem.get_text(strip=True).split("/")[0].strip()
                    price = price_elem.get_text(strip=True)
                    product_data.append([product_name, price])
            return product_data
        else:
            return None
    else:
        return None

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 4, 14),
    'retries': 1,
}

with DAG('extract_discounts_dag', 
         default_args=default_args,
         schedule_interval='@daily',
         catchup=False) as dag:

    extract_and_process = PythonOperator(
        task_id='extract_and_process',
        python_callable=extract_discounts,
    )

extract_and_process
