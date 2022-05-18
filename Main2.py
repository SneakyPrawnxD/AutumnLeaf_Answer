import os
import requests

from functools import total_ordering
from datetime import timedelta
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

WebURL = os.environ.get('site')
LoopCount = int(os.environ.get('times'))
Totaltime = timedelta(0,0,0)

for i in range(0,LoopCount):
    x = requests.get(WebURL)
    callTime = x.elapsed
    Totaltime = Totaltime + callTime
    
    print('Request time: ' + str(x.elapsed),'| Web URL: ' + str(x.url))
print('Total time: ' + str(Totaltime))