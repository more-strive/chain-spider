import uvicorn
from fastapi import FastAPI, Depends

app = FastAPI()

@app.get("/binance")
def binance():
  return {"hello": 'binance'}

@app.get("/etherscan")
def etherscan():
  return {"hello": 'etherscan'}

if __name__ == '__main__':
    uvicorn.run(app='main:app', host="192.168.1.103", port=8000, reload=True)