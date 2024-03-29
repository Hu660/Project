# from bs4 import BeautifulSoup
#
# with open("./test.html") as fin:
#     html_doc = fin.read()
# soup = BeautifulSoup(html_doc, "html.parser")
#
# links = soup.find_all("a")
# for link in links:
#     print(link.name,link["href"], link.getText())
# img = soup.find_all("img")
# print(img["src"])
from bs4 import BeautifulSoup

with open("./test.html") as fin:
    html_doc = fin.read()

soup = BeautifulSoup(html_doc, "html.parser")

links = soup.find_all("a")
for link in links:
    print(link.name, link["href"], link.getText())

imgs = soup.find_all("img")
for img in imgs:
    print(img["src"])