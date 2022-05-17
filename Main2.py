import os
import requests
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

WebURL = os.environ.get('site')
LoopCount = int(os.environ.get('times'))

for i in range(0,LoopCount):
    x = requests.get(WebURL)
    print(x.elapsed,x.url)
