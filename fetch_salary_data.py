import requests
from os import makedirs
from os.path import basename, join
DATA_DIR = 'tempdata'
makedirs(DATA_DIR, exist_ok=True)
SOURCE_DATA_URLS = [
    'http://transparentcalifornia.com/export/2014-university-system.csv',
    'http://transparentcalifornia.com/export/2014-community-colleges.csv'
]

for url in SOURCE_DATA_URLS:
    print("Downloading", url)
    resp = requests.get(url)
    data_file_path = join(DATA_DIR, basename(url))

    with open(data_file_path, 'w') as f:
        f.write(resp.text)
        print("Wrote", len(resp.text), "to", data_file_path)
