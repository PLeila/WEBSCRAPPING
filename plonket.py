import requests
from bs4 import BeautifulSoup
import csv

# URL pou paj la ou vle grate
url = "https://lenouvelliste.com/"

# Fè yon demann GET pou jwenn paj la
response = requests.get(url)

# Kreye yon objè BeautifulSoup avèk kontni paj la
soup = BeautifulSoup(response.content, "html.parser")

# Jwenn tout atik yo nan paj la
articles = soup.find_all("article")

# Kreye yon list pou kenbe done yo
data = []

# Fouye atravè chak atik
for article in articles:
    # Ekstrè done yo pou chak atik
    title = article.find("h2").text.strip()
    link = article.find("a")["href"]
    image = article.find("img")["src"]
    description = article.find("p").text.strip()

    # Ajoute done yo nan list la
    data.append([title, link, image, description])

# Kreye yon fichi CSV epi ekri done yo nan li
with open("lenouvelliste_data.csv", "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Tit", "Link", "Foto", "Deskripsyon"])
    writer.writerows(data)