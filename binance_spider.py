import common
from lxml import etree

def binanceSpider(address='0xbb4CdB9CBd36B01bD1cBaEBF2De08d9173bc095c'):
  url = 'https://bscscan.com/token/%s#balances' % address
  data = {}
  response = common.get_response(url)
  if response.status_code != 200:
    return data
  # with open('./html/binance.html', 'w', encoding='utf-8') as wf:
  #   wf.write(response.text)
  selecter = etree.HTML(response.text)  
  iconXpath = selecter.xpath('//*[@id="content"]/div[1]/div/div[1]/h1/img')
  if len(iconXpath) == 1:
    iconElement = iconXpath[0] 
    iconSrc = iconElement.attrib.get('src')
    data['iconSrc'] = iconSrc

  overviewXpath = selecter.xpath('//*[@id="ContentPlaceHolder1_divSummary"]/div[1]/div[1]/div/div[1]/h2/span/b')
  if len(overviewXpath) == 1:
    overviewElement = overviewXpath[0]
    overviewText = overviewElement.text
    data['overviewText'] = overviewText

  supplyXpath = selecter.xpath('//*[@id="ContentPlaceHolder1_divSummary"]/div[1]/div[1]/div/div[2]/div[2]/div[2]/span[1]')
  if len(supplyXpath) == 1:
    supplyElement = supplyXpath[0] 
    supplyText = supplyElement.text
    data['supplyText'] = supplyText 

  holdersXpath = selecter.xpath('//*[@id="ContentPlaceHolder1_tr_tokenHolders"]/div/div[2]/div/div')
  if len(holdersXpath) == 1:
    holdersElement = holdersXpath[0] 
    holdersText = holdersElement.text
    data['holdersText'] = holdersText.strip()
  
  decimalsXpath = selecter.xpath('//*[@id="ContentPlaceHolder1_trDecimals"]/div/div[2]')
  if len(decimalsXpath) == 1:
    decimalsElement = decimalsXpath[0] 
    decimalsText = decimalsElement.text
    data['decimalsText'] = decimalsText.strip()
  
  officialXpath = selecter.xpath('//*[@id="ContentPlaceHolder1_tr_officialsite_1"]/div/div[2]/a')
  if len(officialXpath) == 1:
    officialElement = officialXpath[0] 
    officialText = officialElement.attrib.get('href')
    data['officialText'] = officialText

  socialXpath = selecter.xpath('//*[@id="ContentPlaceHolder1_divSummary"]/div[1]/div[2]/div/div[2]/div[4]/div/div[2]/ul/li')
  if len(socialXpath) >= 0:
    for index in range(len(socialXpath)):
      socialSonXpath = selecter.xpath('//*[@id="ContentPlaceHolder1_divSummary"]/div[1]/div[2]/div/div[2]/div[4]/div/div[2]/ul/li[%s]/a' % (index+1))
      if len(socialSonXpath) == 1:
        socialSonElement = socialSonXpath[0]
        content = socialSonElement.attrib.get('data-original-title')
        value = content.split(': ')
        data[value[0]] = value[1].strip()
  return data
  
if __name__ == '__main__':
  print(binanceSpider())