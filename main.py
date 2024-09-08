import os
import requests
import rss.minkabu_rss as minkabu_rss
import rss.jpx_rss as jpx_rss
import rss.yahoo_news_rss as yahoo_news_rss

def send_line_notify(message: str) -> None:
  endpoint = "https://notify-api.line.me/api/notify"
  headers = {"Authorization": f"Bearer {os.environ.get('LINE_NOTIFY_TOKEN')}"}
  data = {"message": message}
  requests.post(endpoint, headers=headers, data=data)

def main():
  send_line_notify(minkabu_rss.get_rss_minkabu_statement())
  send_line_notify(minkabu_rss.get_rss_minkabu_stock())
  send_line_notify(minkabu_rss.get_rss_minkabu_commodity_bond())
  send_line_notify(jpx_rss.get_rss_jpx_markets_news())
  send_line_notify(yahoo_news_rss.get_rss_yahoo_news_coindeskjapan())

if __name__ == "__main__":
  main()


