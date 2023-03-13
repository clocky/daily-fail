import requests
from bs4 import BeautifulSoup
DATA_FILE = "./data/headlines.txt"

response = requests.get(
    "https://www.dailymail.co.uk/news/headlines/index.html")
if response.ok:
    soup = BeautifulSoup(response.text, "html.parser")
    sidebar = soup.select("ul.link-bogr2 li span.pufftext strong")
    new_headlines = []
    for headline in sidebar:
        new_headlines.append(headline.get_text(strip=True))

    with open(DATA_FILE, "r") as file:
        existing_headlines = file.readlines()[-250:]
        existing_headlines = [line.strip() for line in existing_headlines]

    new_headlines = [s for s in new_headlines if s not in existing_headlines]

    with open(DATA_FILE, "a") as file:
        for s in new_headlines:
            file.write(s + "\n")
    print(f"Added {len(new_headlines)} new headlines...")

else:
    print("Error: ", response.status_code)
