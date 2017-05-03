import ssl
from http.client import IncompleteRead
from urllib.request import Request, urlopen

url = 'https://52.49.91.111:8443/ghost'

total_bytes = 3445
current_bytes = 13
content = 'iVBORw0KGgoAA'
while current_bytes < total_bytes:
    req = Request(url)
    req.add_header('Range', f'bytes={current_bytes}-')
    resp = urlopen(req, context=ssl._create_unverified_context())
    try:
        resp = urlopen(req, context=ssl._create_unverified_context())
        new_bytes = resp.read()
    except IncompleteRead as e:
        new_bytes = e.partial
    new_content = str(new_bytes, 'utf-8')
    content += new_content
    current_bytes = len(content)
    print(f'{current_bytes/total_bytes*100:.1f}%')

print(content)
