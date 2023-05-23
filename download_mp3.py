import requests, random, os
from bs4 import BeautifulSoup
from urllib.request import urlopen


def download_mp3(link):

  url, sep, late  = link.partition('/video/')
  vidid, sep, late = late.partition('?')

  file_dir = os.path.dirname(os.path.realpath('__file__'))
  file_name = os.path.join(file_dir, f'Content/{vidid}.mp3')
  if os.path.exists(file_name):
    return vidid
  else:

    cookies = {
      '_gid': 'GA1.2.772426870.1684789050',
      '_gat_UA-3524196-6': '1',
      '_ga': 'GA1.2.1912642289.1684789050',
      '_ga_ZSF3D6YSLC': 'GS1.1.1684789049.1.1.1684789102.0.0.0',
    }

    headers = {
      'authority':
      'ssstik.io',
      'accept':
      '*/*',
      'accept-language':
      'en-US,en;q=0.9',
      'content-type':
      'application/x-www-form-urlencoded; charset=UTF-8',
      # 'cookie': '_gid=GA1.2.772426870.1684789050; _gat_UA-3524196-6=1; _ga=GA1.2.1912642289.1684789050; _ga_ZSF3D6YSLC=GS1.1.1684789049.1.1.1684789102.0.0.0',
      'dnt':
      '1',
      'hx-current-url':
      'https://ssstik.io/download-tiktok-mp3',
      'hx-request':
      'true',
      'hx-target':
      'target',
      'hx-trigger':
      '_gcaptcha_pt',
      'origin':
      'https://ssstik.io',
      'referer':
      'https://ssstik.io/download-tiktok-mp3',
      'sec-ch-ua':
      '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
      'sec-ch-ua-mobile':
      '?0',
      'sec-ch-ua-platform':
      '"Windows"',
      'sec-fetch-dest':
      'empty',
      'sec-fetch-mode':
      'cors',
      'sec-fetch-site':
      'same-origin',
      'user-agent':
      'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
    }

    params = {
      'url': 'dl',
    }

    data = {
      'id': link,
      'locale': 'en',
      'tt': 'Y2liano2',
    }

    response = requests.post('https://ssstik.io/abc',
                             params=params,
                             cookies=cookies,
                             headers=headers,
                             data=data)
    downloadLink = BeautifulSoup(response.text, "html.parser").a["href"]
    mp4File = urlopen(downloadLink)
    with open(f"Content/{vidid}.mp3", "wb") as output:
      while True:
        data = mp4File.read(4096)
        if data: output.write(data)
        else: break

  return vidid
