# Импорт необходимых библиотек
import requests
from bs4 import BeautifulSoup

#Парсинг HTML SeaBorn
url = "https://seaborn.pydata.org/examples/index.html"
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')
print(soup)      #print(soup.prettify())

# Нахождение всех тэгов абзацев 
lst = soup.find_all('p')

for item in lst: 
    print(item)
    
def clean_item(my_item):
    position = my_item.find('</')
    return my_item[4:position]
    
print(" ")

# Очистка(1)
for item in lst: 
    print(clean_item(str(item)))
