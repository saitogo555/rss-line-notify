import feedparser
from utils import convert_date_str

MAX_COUNT = 20

def _get_msg_from_jpx_rss(rss_url: str, site_url: str, title: str) -> str:
  list = {}
  feed = feedparser.parse(rss_url)
  message = f"JPX {title}\n"
  message += "\n"
  message += f"一覧ページ: {site_url}\n"
  message += "\n"
  message += "■ニュース一覧\n"

  for entry in feed.entries[:MAX_COUNT]:
    title = entry["title"]
    date = convert_date_str(entry["published"])
    if (date not in list):
      list[date] = []
    list[date].append(title)

  for date in list.keys():
    message += f"{date}\n"
    for title in list[date]:
      message += f"・{title}\n"
    message += "\n"

  return message


# JPX マーケットニュース
def get_rss_jpx_markets_news():
  rss_url = "https://www.jpx.co.jp/rss/markets_news.xml"
  site_url = "https://x.gd/5DHCw"
  title = "マーケットニュース"
  return _get_msg_from_jpx_rss(rss_url, site_url, title)
  