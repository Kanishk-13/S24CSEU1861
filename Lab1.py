import requests

url = "https://github.com/Kanishk-13?tab=repositories"
html = requests.get(url).text

from bs4 import BeautifulSoup

soup = BeautifulSoup(html, "html.parser")

for repo in soup.select("a[itemprop='name codeRepository']"):
    print(repo.text.strip())