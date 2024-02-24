import lxml
import requests
from bs4 import BeautifulSoup

session = requests.session()
header = {"user-agent": "big_grid row form-row row-cols-1 row-cols-sm-2 row-cols-xl-3 row-cols-xxl-4"}

for j in range(1, 11):
    url = f"https://onlyballs.com.ua/kupit-myachi-futbolnye={j}"

response = session.get(url, headers=header)
soup = BeautifulSoup(response.text,"lxml")
print(soup)

all_product = soup.find('div', class_="row mt-4")

products = all_product.find_all("div", class_="col-lg-4 col-md-4 col-sm-6 portfolio-item")

for elem in products:
    price = elem.find("p", class_="card-text").text
    price = price[price.find(":")+1:price.find("₽")]
    title = elem.find("h3", class_="card-title").text.strip()
    with open("ex.txt", "a", encoding="utf-8") as file:
        file.write(f"{title}\n")
    print(price)