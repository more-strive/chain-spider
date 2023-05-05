import uvicorn
import bscscan_spider
import etherscan_spider
from fastapi import FastAPI

app = FastAPI()

@app.get("/api/chain/data")
async def main(chain: str, address: str):
  data = None
  if chain == 'bscscan':
    data = bscscan_spider.bscscanSpider(address)
  elif chain == 'etherscan':
    data = etherscan_spider.etherscanSpider(address)
  return {"chain": chain, 'address': address, 'data': data}



if __name__ == '__main__':
    uvicorn.run(app='main:app', host="192.168.1.103", port=8000, reload=True)