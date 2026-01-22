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

#%%
data.to_csv("smu_notice.csv", index=False, encoding="utf-8-sig")

#%%
from feedgen. feed import FeedGenerator
fg = FeedGenerator()
fg.title("상명대학교 공지사항 (SMU Notice)")
fg.link(href="https://www.smu.ac.kr/kor/life/notice.do?srCampus=smu", rel="alternate")
fg.description("상명대학교 공지사항을 자동 수집해 RSS로 제공합니다.")

for _, row in data.iterrows():
    fe = fg.add_entry()
    fe.title(str(row["titles"]))
    fe.link(href=str(row["links"]))
    fe.description(str(row["labels"]))
    fe.pubDate(pd.to_datetime(row["date"]).to_pydatetime())

fg.rss_file("rss.xml")




