from urllib.request import urlopen
from bs4 import BeautifulSoup

response = urlopen("https://stepik.org/media/attachments/lesson/209723/4.html")
html = response.read().decode("utf-8")
soup = BeautifulSoup(html, 'html.parser')
sum = 0
for td in soup.find_all('td'):
    sum += int(td.get_text())
print(sum)
