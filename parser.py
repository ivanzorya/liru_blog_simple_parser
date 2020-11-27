from bs4 import BeautifulSoup
import urllib.request

result = []

for i in range(1, 55):

    req = urllib.request.urlopen(
        f'https://www.liveinternet.ru/users/zimnii/page{i}.shtml'
    )
    html = req.read()
    soup = BeautifulSoup(html, 'html.parser')
    posts = soup.find_all('div', class_='CONBL blo-fastcom_base')
    page = []
    for item in posts:
        title = item.find('h1', class_='ZAG').get_text(strip=True)
        date = item.find('span', class_='GL_TXTSM').get_text(strip=True)
        desc = item.find('div', class_='GL_MAR10T').get_text(strip=True)
        page.append({
            'title': title,
            'date': date,
            'desc': desc
        })
    page.reverse()
    result += page

f = open('posts.txt', 'w', encoding='utf-8')
i = 1
for item in result:
    f.write(
        f'Запись {i}.\n\nЗаголовок: {item["title"]}.\n\n'
        f'Дата:{item["date"]}.\n\n{item["desc"]}\n\n'
        f'_______________________\n\n'
    )
    i += 1
f.close()


if __name__ == '__main__':
    main()
