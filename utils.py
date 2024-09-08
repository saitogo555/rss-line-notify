from dateutil import parser

def convert_date_str(date: str) -> str:
  try:
    parsed_date = parser.parse(date)
    return parsed_date.strftime("%m-%d")
  except (ValueError, TypeError):
    print(f"未対応の日付形式です: {date}")
    return "日付不明"