import json

import requests

completion_query = 'Den'

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:125.0) Gecko/20100101 Firefox/125.0"
}

response = requests.get(f'https://google.com/complete/search?client=chrome&q={completion_query}')  # proxies={https:' '20.186.205.122'}


for completion in json.loads(response.text)[1]:
    print(completion)
