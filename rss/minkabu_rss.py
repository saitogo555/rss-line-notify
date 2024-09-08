import feedparser
from utils import convert_date_str

MAX_COUNT = 20

def _get_msg_from_minkabu_rss(rss_url: str, site_url: str, title: str) -> str:
  list = {}
  feed = feedparser.parse(rss_url)
  message = f"みんかぶ FX/為替 {title}\n"
  message += "\n"
  message += f"一覧ページ: {site_url}\n"
  message += "\n"
  message += "■ニュース一覧\n"

  for entry in feed.entries[:MAX_COUNT]:
    title = entry["title"]
    date = convert_date_str(entry["date"])
    if (date not in list):
      list[date] = []
    list[date].append(title)

  for date in list.keys():
    message += f"{date}\n"
    for title in list[date]:
      message += f"・{title}\n"
    message += "\n"

  return message


# みんかぶ FX/為替 要人発言
def get_rss_minkabu_statement():
  rss_url = "https://assets.wor.jp/rss/rdf/minkabufx/statement.rdf"
  site_url = "https://x.gd/2eBFC"
  title = "要人発言"
  return _get_msg_from_minkabu_rss(rss_url, site_url, title)

# みんかぶ FX/為替 株式
def get_rss_minkabu_stock():
  rss_url = "https://assets.wor.jp/rss/rdf/minkabufx/stock.rdf"
  site_url = "https://x.gd/5Uabp"
  title = "株式"
  return _get_msg_from_minkabu_rss(rss_url, site_url, title)

# みんかぶ FX/為替 商品/債券
def get_rss_minkabu_commodity_bond():
  rss_url = "https://assets.wor.jp/rss/rdf/minkabufx/commodity.rdf"
  site_url = "https://x.gd/fAqCa"
  title = "商品/債券"
  return _get_msg_from_minkabu_rss(rss_url, site_url, title)
