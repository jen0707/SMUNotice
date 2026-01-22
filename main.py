# %%
import bs4
import requests
import pandas as pd

# %%
url = "https://www.smu.ac.kr/kor/life/notice.do?srCampus=smu"
html = requests.get(url).text
soup = bs4.BeautifulSoup(html, 'html.parser')

# %%
css_selector = 'div.board-name-thumb.board-wrap li td a'

for tag in soup.select(css_selector):
    print(tag.get_text(strip=True))

# %%
css_selector = 'div.board-name-thumb.board-wrap td:nth-child(2) a'

labels = []

for tag in soup.select(css_selector):
    labels.append(tag.get_text(strip=True))

print(labels)


# %%
css_selector = 'div.board-name-thumb.board-wrap td:nth-child(3) a'

titles = []

for tag in soup.select(css_selector):
    titles.append(tag.get_text(strip=True))

print(titles)

# %%
css_selector = 'div.board-name-thumb.board-wrap li.board-thumb-content-date'

dates = []

for tag in soup.select(css_selector):
    date_raw = tag.get_text(strip=True)
    date = date_raw.replace('작성일', '')
    dates.append(date)

print(dates)

# %%
df = pd.DataFrame({
    "date": dates
})

df["date"] = pd.to_datetime(df["date"])

# %%
base_url = "https://www.smu.ac.kr/kor/life/notice.do"
css_selector = 'div.board-name-thumb.board-wrap td:nth-child(3) a'

links = []

for tag in soup.select(css_selector):
    href = tag.get('href')
    full_url = base_url + href
    links.append(full_url)

print(links)

# %%
data = list(zip(labels,titles,dates,links))
data = pd.DataFrame(data=data,columns=['labels','titles','date','links'])



