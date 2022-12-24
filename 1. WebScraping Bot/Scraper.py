# import requests
# from bs4 import BeautifulSoup

# response = requests.get(
#     url="https://en.wikipedia.org/wiki/Web_scraping",
# )
# soup = BeautifulSoup(response.content, 'html.parser')
# # print(response.status_code)

# title = soup.find(Class="mw-page-title-main")
# print(title.string)

import requests
from bs4 import BeautifulSoup

response = requests.get(
	url="https://en.wikipedia.org/wiki/Web_scraping",
)
soup = BeautifulSoup(response.content, 'html.parser')

title = soup.find(id="firstHeading")
print(title.string)