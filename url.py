import requests
from bs4 import BeautifulSoup

url = 'https://www.bbc.com/news/world'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

headlines = soup.find_all('h2', attrs={"class":'sc-4fedabc7-3 zTZri'})

# Display the headlines
for headline in headlines:
    print(headline.text.strip())  # .strip() to remove any leading/trailing whitespace

