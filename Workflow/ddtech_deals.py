import os
import requests
from bs4 import BeautifulSoup
from prefect import task, Flow, context
from tabulate import tabulate
from datetime import datetime

context.config.logging.level = "ERROR"

@task
def scrape_ddtech_deals():
    url = "https://ddtech.mx/buscar/ddescuentos"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"
    } 
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        products = soup.find_all("div", class_="product")
        
        if products:
            product_data = []
            for product in products:
                product_name_elem = product.find("h3", class_="name")
                price_elem = product.find("span", class_="price")
                if product_name_elem and price_elem:
                    product_name = product_name_elem.get_text(strip=True)
                    product_name = product_name.split("/")[0].strip()
                    price = price_elem.get_text(strip=True)
                    product_data.append([product_name, price])
            return product_data
        else:
            return None
    else:
        return None

@task
def write_to_file(product_data):
    if product_data:
        file_path = "C:\\Users\\yo-22\\OneDrive\\Documentos\\Computacion-Tolerante-a-Fallas\\Workflow\\ddtech_deals_historial.txt"
        current_date = datetime.now().strftime("%Y-%m-%d")
        
        if os.path.exists(file_path):
            with open(file_path, "r", encoding="utf-8") as file:
                existing_content = file.read()
                if current_date in existing_content:
                    print("Ya se ha escrito un registro para hoy. No se escribirá otro.")
                    return
                else:
                    with open(file_path, "a", encoding="utf-8") as file:
                        file.write(f"\n\nOfertas en DDTech - {current_date}:\n")
                        file.write(tabulate(product_data, headers=["Nombre del producto", "Precio"], tablefmt="grid"))
                        print(f"Se ha agregado un nuevo registro para hoy ({current_date}).")
        else:
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(f"Ofertas en DDTech - {current_date}:\n")
                file.write(tabulate(product_data, headers=["Nombre del producto", "Precio"], tablefmt="grid"))
                print(f"Se ha creado un nuevo archivo para hoy ({current_date}).")
    else:
        print("No se encontraron ofertas en la página.")

@task
def read_and_print_file():
    file_path = "C:\\Users\\yo-22\\OneDrive\\Documentos\\Computacion-Tolerante-a-Fallas\\Workflow\\ddtech_deals_historial.txt"
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as file:
            print(file.read())
    else:
        print("El archivo no existe.")

if __name__ == "__main__":
    with Flow("scrape_ddtech_flow") as flow:
        data = scrape_ddtech_deals()
        write_to_file(data)
        read_and_print_file()

    flow.run()
