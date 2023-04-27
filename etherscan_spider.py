import common
from lxml import etree

def etherscanSpider(address='0x7d1afa7b718fb893db30a3abc0cfc608aacfebb0'):
  url = 'https://etherscan.io/token/%s#balances' % address
  data = {}
  response = common.get_response(url)
  if response.status_code != 200:
    return data
  selecter = etree.HTML(response.text)
  iconXpath = selecter.xpath('//*[@id="content"]/section[1]/div/div[1]/img')
  if len(iconXpath) == 1:
    iconElement = iconXpath[0] 
    iconSrc = iconElement.attrib.get('src')
    data['iconSrc'] = iconSrc

  overviewXpath = selecter.xpath('//*[@id="ContentPlaceHolder1_divSummary"]/div[1]/div[1]/span')
  if len(overviewXpath) == 1:
    overviewElement = overviewXpath[0]
    overviewText = overviewElement.text
    data['overviewText'] = overviewText

  supplyXpath = selecter.xpath('//*[@id="ContentPlaceHolder1_divSummary"]/div[2]/div[1]/div/div/div[1]/div/span')
  if len(supplyXpath) == 1:
    supplyElement = supplyXpath[0] 
    supplyText = supplyElement.text
    data['supplyText'] = supplyText

  holdersXpath = selecter.xpath('//*[@id="ContentPlaceHolder1_tr_tokenHolders"]/div/div')
  if len(holdersXpath) == 1:
    holdersElement = holdersXpath[0] 
    holdersText = holdersElement.text
    data['holdersText'] = holdersText

  socialXpath = selecter.xpath('//*[@id="ContentPlaceHolder1_divLinks"]/ul/li')
  if len(socialXpath) >= 0:
    for index in range(len(socialXpath)):
      socialSonXpath = selecter.xpath('//*[@id="ContentPlaceHolder1_divLinks"]/ul/li[%s]/a' % (index+1))
      if len(socialSonXpath) == 1:
        socialSonElement = socialSonXpath[0]
        content = socialSonElement.attrib.get('href')
        data[index] = content
  return data
  
if __name__ == '__main__':
  etherscanSpider()
