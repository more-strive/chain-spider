import requests

def get_proxy():
  return requests.get("http://localhost:5000/get/").json()

def delete_proxy(proxy):
  requests.get("http://localhost:5000/delete/?proxy={}".format(proxy))

def get_response(url):
  # url = 'https://bscscan.com/token/0xbb4CdB9CBd36B01bD1cBaEBF2De08d9173bc095c#balances'
  proxy = get_proxy().get("proxy")
  
  retry_count = 5
  # with open('./html/binance.html', 'w', encoding='utf-8') as wf:
  #   wf.write(response.text)
  while retry_count > 0:
    try:
      response = requests.get(url, proxies={"http": "http://{}".format(proxy)}, headers=headers)
      return response
    except Exception:
      retry_count -= 1
  delete_proxy(proxy)
  return None

headers = {
  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
}