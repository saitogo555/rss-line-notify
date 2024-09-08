import feedparser
from utils import convert_date_str

MAX_COUNT = 20

def _get_msg_from_yahoo_news_rss(rss_url: str, site_url: str, title: str, suffix: str = None) -> str:
  list = {}
  feed = feedparser.parse(rss_url)
  message = f"Yahooニュース - {title}\n"
  message += "\n"
  message += f"一覧ページ: {site_url}\n"
  message += "\n"
  message += "■ニュース一覧\n"

  for entry in feed.entries[:MAX_COUNT]:
    title = entry["title"]
    if suffix is not None:
      title = title.replace(suffix, "")
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

def _get_msg_from_coindeskjapan_rss(rss_url: str, site_url: str, title: str) -> str:
  suffix = "(CoinDesk JAPAN)"
  return _get_msg_from_yahoo_news_rss(rss_url, site_url, title, suffix)

# CoinDesk JAPAN
def get_rss_yahoo_news_coindeskjapan():
  rss_url = "https://news.yahoo.co.jp/rss/media/coindesk/all.xml"
  site_url = "https://x.gd/ALpJp"
  title = "CoinDesk JAPAN"
  return _get_msg_from_coindeskjapan_rss(rss_url, site_url, title)
  