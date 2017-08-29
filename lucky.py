#! python3
import requests, sys, webbrowser, bs4
print('baiduing...')
res =requests.get('https://www.sogou.com/web?query='+' '.join(sys.argv[1:]))
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text,'lxml')
linkElems = soup.select('.vrTitle a')
numOpen =min(5,len(linkElems))
for i in range(numOpen):
   webbrowser.open(linkElems[i].get('href'))

