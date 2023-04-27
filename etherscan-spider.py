import common
from lxml import etree

def etherscanSpider():
  url = 'https://etherscan.io/token/0x7d1afa7b718fb893db30a3abc0cfc608aacfebb0#balances'
  # headers = {
  #   "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
  # }
  # response = requests.get(url, headers=headers)

  # with open('./html/etherscan.html', 'w', encoding='utf-8') as wf:
  #   wf.write(response.text)
  response = common.get_response(url)
  print('response:', response)
  if not response:
    return
  selecter = etree.HTML(response.text)
  iconXpath = selecter.xpath('//*[@id="content"]/section[1]/div/div[1]/img')
  if len(iconXpath) == 1:
    iconElement = iconXpath[0] 
    iconSrc = iconElement.attrib.get('src')
    print('iconSrc:', iconSrc)

  overviewXpath = selecter.xpath('//*[@id="ContentPlaceHolder1_divSummary"]/div[1]/div[1]/span')
  if len(overviewXpath) == 1:
    overviewElement = overviewXpath[0]
    overviewText = overviewElement.text
    print("overviewText:", overviewText)

  supplyXpath = selecter.xpath('//*[@id="ContentPlaceHolder1_divSummary"]/div[2]/div[1]/div/div/div[1]/div/span')
  if len(supplyXpath) == 1:
    supplyElement = supplyXpath[0] 
    supplyText = supplyElement.text
    print("supplyText:", supplyText) 

  holdersXpath = selecter.xpath('//*[@id="ContentPlaceHolder1_tr_tokenHolders"]/div/div')
  if len(holdersXpath) == 1:
    holdersElement = holdersXpath[0] 
    holdersText = holdersElement.text
    print("holdersText:", holdersText.strip()) 

  socialXpath = selecter.xpath('//*[@id="ContentPlaceHolder1_divLinks"]/ul/li')
  if len(socialXpath) >= 0:
    for index in range(len(socialXpath)):
      socialSonXpath = selecter.xpath('//*[@id="ContentPlaceHolder1_divLinks"]/ul/li[%s]/a' % (index+1))
      if len(socialSonXpath) == 1:
        socialSonElement = socialSonXpath[0]
        content = socialSonElement.attrib.get('href')
        print('content:', content)
    
  
if __name__ == '__main__':
  etherscanSpider()
