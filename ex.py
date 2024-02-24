import lxml
import requests
from bs4 import BeautifulSoup

session = requests.session()
header = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"}

for j in range(1, 11):
    url = f"https://onlyballs.com.ua/kupit-myachi-futbolnye={j}"

    response = session.get(url, headers=header)
    soup = BeautifulSoup(response.text,"lxml")
    print(soup)

    product-name = soup.find('div', class_="big_grid row form-row row-cols-1 row-cols-sm-2 row-cols-xl-3 row-cols-xxl-4")

    products = product-name.find_all("div", class_="product-name")

    for elem in products:
        price = elem.find("p", class_="card-text").text
        price = price[price.find(":")+1:price.find("₽")]
        title = elem.find("h3", class_="card-title").text.strip()
        with open("ex.txt", "a", encoding="utf-8") as file:
            file.write(f"{title}\n")
        print(price)
