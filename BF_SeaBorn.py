# Импорт необходимых библиотек
import requests
from bs4 import BeautifulSoup


#Парсинг HTML SeaBorn
url = "https://seaborn.pydata.org/examples/index.html"
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')
print(soup)      #print(soup.prettify())

# Нахождение всех заголовков 2 уровня
lst = soup.find_all('<p>')

for item in lst: 
    print(item)
    
def clean_item(my_item):
    position = my_item.find('<a')
    return my_item[4:position]
    
print(" ")

# Очистка(1)
for item in lst: 
    print(clean_item(str(item)))
    
lst = soup.find_all(class_ = 'std std-ref')

for item in lst: 
    print(item) 
    
def clean_item2(my_item):
    position = my_item.find('</')
    return my_item[26:position]  

# Очистка(2)    
for item in lst: 
    print(clean_item(str(item)))
    
