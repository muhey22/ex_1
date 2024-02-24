import lxml
import requests
from bs4 import BeautifulSoup

session = requests.session()
header = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"}

for j in range(1, 11):
    url = f"https://kups.club/?page={j}"

response = session.get(url, headers=header)
soup = BeautifulSoup(response.text,"lxml")
print(soup)

all_product = soup.find('div', class_="row mt-4")

products = all_product.find_all("div", class_="col-lg-4 col-md-4 col-sm-6 portfolio-item")

for elem in products:
    price = elem.find("p", class_="card-text").text
    price = price[price.find(":")+1:price.find("₽")]
    title = elem.find("h3", class_="card-title").text.strip()
    with open("сайт.txt", "a", encoding="utf-8") as file:
        file.write(f"{title}\n")
    print(price)