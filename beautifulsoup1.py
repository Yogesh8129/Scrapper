from bs4 import BeautifulSoup
import requests

# result = request.get("www.google.com")
# content = result.text
# soup = BeautifulSoup(content,"lxml")
# soup.find('tag', class_="class_name")
# #or
# soup.find("specific_id")
# soup.find('article', class_="main_article")
root = 'https://subslikescript.com'
website = f'{root}/movies'
result = requests.get(website)
content = result.text
soup = BeautifulSoup(content, 'lxml')
# print(soup.prettify())

box = soup.find('article', class_='main-article')

links = []
for link in box.find_all('a', href=True):
    links.append(link['href'])

print(links)

for link in links:
    website = f'{root}/{link}'
    result = requests.get(website)
    content = result.text
    soup = BeautifulSoup(content, 'lxml')

    box = soup.find('article', class_='main-article')

    title = box.find('h1').get_text()
    transcript = box.find('div', class_='full-script').get_text(strip=True, separator=' ')

    with open(f'{title}.docx', 'w', encoding='utf-8') as file:
        file.write(transcript)
