import os
import requests
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

WebURL = os.environ.get('site')
LoopCount = int(os.environ.get('times'))
Totaltime = 0

for i in range(0,LoopCount):
    x = requests.get(WebURL)
    callTime = x.elapsed
    Totaltime = callTime + callTime
    print(x.elapsed,x.url)
print('Total time:' + str(Totaltime))
