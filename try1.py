# https://stackoverflow.com/questions/47928608/how-to-use-beautifulsoup-to-parse-google-search-results-in-python

import urllib
from bs4 import BeautifulSoup
import requests
import webbrowser
import json

headers = {
    'User-agent':
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582"
}

text = 'hello world'
text = urllib.parse.quote_plus(text)

url = 'https://google.com/search?q=' + text

print(url)

response = requests.get(url)


#with open('output.html', 'wb') as f:
#    f.write(response.content)
#webbrowser.open('output.html')

soup = BeautifulSoup(response.text, 'lxml')
#for g in soup.find_all(class_='g'):
#    print(g.text)
#    print('-----')

summary = []

for container in soup.findAll('div', class_='tF2Cxc'):
  heading = container.find('h3', class_='LC20lb DKV0Md').text
  article_summary = container.find('span', class_='aCOpRe').text

  summary.append({
      'Heading': heading,
      'Article Summary': article_summary,
  })

print(json.dumps(summary, indent=2, ensure_ascii=False))