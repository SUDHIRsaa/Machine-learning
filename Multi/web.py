#https://python.langchain.com/v0.2/docs/introduction/
# https://python.langchain.com/v0.2/docs/concepts/
# https://python.langchain.com/v0.2/docs/tutorials/

import threading
import requests
import time
from bs4 import BeautifulSoup
urls=[
   " https://python.langchain.com/v0.2/docs/concepts/",
    "https://python.langchain.com/v0.2/docs/tutorials/",
    "https://python.langchain.com/v0.2/docs/introduction/"
]

def fetch_url(urls):
    response=requests.get(urls)
    soup=BeautifulSoup(response.content, "html.parser")
    print(f'Fetching URL: {(len(soup.text))}')
    
threads=[]
for url in urls:
    t=threading.Thread(target=fetch_url, args=(url,))
    threads.append(t)
    t.start()
    
for t in threads:
    t.join()
    
print("Done")