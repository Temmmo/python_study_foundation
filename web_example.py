import requests, os
os.chdir('D:\\untitled')
res = requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt')
res.raise_for_status()
playFile = open('RAndJuli','wb')
for chunk in res.iter_content(100000):
    playFile.write(chunk)
playFile.close()

res1= requests.get('http://inventwithpython.com/page_that_does_not_exist')
try:
    res1.raise_for_status()
except Exception as exc:
    print('%s'% (exc))

