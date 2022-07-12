from cgi import print_arguments
import requests
from bs4 import BeautifulSoup

url = 'https://www.drukwerkdeal.nl/nl/producten/promotie/flyers'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
    
} 

result = requests.get(url, headers=headers)

page = BeautifulSoup(result.content, 'html.parser')

locator = 'header.product-page-title h1.h1'

header = page.select_one(locator)

print(header)
