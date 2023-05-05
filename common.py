import os
import requests
import pyhttpx
import boto3
from config import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_ENDPOINT, AWS_DEFAULT_REGION, AWS_BUCKET

HOST = "127.0.0.1"
PORT = 8234

headers = {
  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
  "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
  "Cookie": "__stripe_mid=81a97fdf-a7e9-4ab3-bf16-64e4d6da71b173c2e1; _ga=GA1.1.503658053.1681522399; bitmedia_fid=eyJmaWQiOiIxNzk0ODQzMGMwOGRkZTYyMTFkYTRjZDMyNTBkZDgyNiIsImZpZG5vdWEiOiIwMmJhOTM3ZDVjMzE4ZmYzOTU0ZDNlYmYzYTIxNDM1YiJ9; ASP.NET_SessionId=3wdtz4qqnsqngeoi0s2vwhor; __cflb=0H28vyb6xVveKGjdV3CFc257Dfrj7qvniLCWeB9BSo6; _ga_PQY6J2Q8EP=GS1.1.1683254911.9.0.1683254911.0.0.0; __cf_bm=l2AcNO_TaP21hoB.kOTvFxIBsK1KJEawMAXUbu7MC5M-1683254914-0-ATP130KdXERfgsmYSCW+TWhkbjfHWAVAo5+oRK0DIZR0R7beSrQ8ul5McGTrFDTeUndW94wUsPHRvtai7GCMVgsN622+4RFp0w1+P2hbD9v2"
}

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
      print('proxy:', proxy)
      response = requests.get(url, proxies={"http": "http://{}".format(proxy)}, headers=headers)
      # session = pyhttpx.HttpSession()
      # response = session.get(url=url, headers=headers, proxies={"http": "http://{}".format(proxy)})
      return response
    except Exception:
      retry_count -= 1
  delete_proxy(proxy)
  return None

def uploadFile(chain, filepath, filename):
  if filename is None:
    raise ValueError("Please enter a valid and complete file path")

  session = boto3.Session(
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=AWS_DEFAULT_REGION
  )
  s3 = session.client("s3")
  s3.upload_file(Filename=filepath, Key=f"{chain}/{filename}", Bucket=AWS_BUCKET)
  os.remove(filepath)

def downloadFile(chain, filename):
  session = boto3.Session(
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=AWS_DEFAULT_REGION
  )
  s3 = session.client("s3")
  s3.download_file(Bucket=AWS_BUCKET, Key=f"{chain}/{filename}", Filename='./html/icon/%s' % filename)

def get_icon_aws(chain, address, url):
  """
  https://winfishapp.s3.ap-southeast-1.amazonaws.com/bscscan/0xbb4CdB9CBd36B01bD1cBaEBF2De08d9173bc095c_logo.png
  """
  proxy = get_proxy().get("proxy")
  response = requests.get(url, proxies={"http": "http://{}".format(proxy)}, headers=headers, stream=True)
  suffix = os.path.splitext(url)[1].replace('.', '')
  filename = '%s_logo.%s' % (address, suffix)
  filepath = './html/icon/%s' % filename
  with open(filepath, "wb") as wf:
    wf.write(response.content)
  uploadFile(chain, filepath, filename)
  download_url = "https://%s.s3.ap-southeast-1.amazonaws.com/%s/%s" % (AWS_BUCKET, chain, filename)
  return download_url

if __name__ == "__main__":
  uploadFile()