# py -m pip install "beautifulsoup4"

import requests
from bs4 import BeautifulSoup

headers = {
    "Accept":"text/html",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0"
    # "Cookie":"ajs_user_id=8c1f1c77b71908986ea73a6d6946c41fcd814023; ajs_anonymous_id=171a52c6-e1c4-4011-8203-9f151bb89cef"
}
url = "http://g2cpqacover01.nextestate.com/coverageresult/history.html"

response = requests.get(url, headers=headers)

parsed_response = BeautifulSoup(response.text, "html.parser")
# print(parsed_response.prettify)

regressionSummarys = parsed_response.find_all("div", class_="dropdown-btn")
print(regressionSummarys)

for summary in regressionSummarys:
    text = summary.text
    summaryPercentages = summary.find_all("span", class_="summary percentage")
    percentage = summaryPercentages[0].text
    print(f"{text}: {percentage}")