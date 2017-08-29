#! python3
# downloadXkcd.py - Downloads every single XKCD comic

import requests, os, bs4
os.chdir('D:\\untitled')
url = 'http://xkcd.com'
os.makedirs('xkcd', exist_ok=True)
while not url.endswith('#'):
    print('Downloading page %s...' % url)
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, "lxml")
    comicElem = soup.select('#comic img')
    if comicElem == []:
        print('Could not find comic image!')
    else:
        comicUrl = 'http:' + comicElem[0].get('src')
        res =requests.get(comicUrl)
        res.raise_for_status()
        imageFile = open(os.path.join('xkcd',os.path.basename(comicUrl)),'wb')
        for chunk in res.iter_content(10000):
            imageFile.write(chunk)
        imageFile.close()
    prveLink = soup.select('a[rel="prev"]')[0]
    url = 'http://xkcd.com'+prveLink.get('href')
print('Done.')


