import requests
import bs4
import pandas as pd

def scrape_articles(url):
    response = requests.get(url)
    soup = bs4.BeautifulSoup(response.content, 'html.parser')

    articles = soup.find_all('article')

    data = []
    for article in articles:
        title = article.find('h1').text
        link = article.find('a')['href']  # Fix: Use square brackets to access the 'href' attribute
        image = article.find('img')['src']
        description = article.find('p').text

        data.append({
            'title': title,
            'link': link,
            'image': image,
            'description': description
        })

    return data

data = scrape_articles('https://lenouvelliste.com/')
df = pd.DataFrame(data)
df.to_csv('articles.csv', index=False)  # Fix: Add index=False to avoid writing row indices to the CSV file
