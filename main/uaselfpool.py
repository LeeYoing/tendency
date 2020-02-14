import requests
import random
import time
####chrome
header1={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"}
header2={"User-Agent":"Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.133 Safari/534.16"}
header3={"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11"}
header4={"User-Agent":"Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.133 Safari/534.16"}
####opera
header5={"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 OPR/26.0.1656.60"}
header6={"User-Agent":"Opera/8.0 (Windows NT 5.1; U; en)"}
header7={"User-Agent":"Mozilla/5.0 (Windows NT 5.1; U; en; rv:1.8.1) Gecko/20061208 Firefox/2.0.0 Opera 9.50"}
header8={"User-Agent":"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; en) Opera 9.50"}
####Firefox
header9={"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0"}
header10={"User-Agent":"Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10"}

uapool=[header1,header2,header3,header4,header5,header6,header7,header8,header9,header10]

def randomuser(uapool):
    for n in range(50):
      HeaderNum=random.randint(1,10)
      TimeNum=random.uniform(1,3)
      requests.headers=uapool[HeaderNum-1]
      response=requests.get("http://www.sina.com.cn", headers=uapool[HeaderNum-1])
      #response.encoding= 'utf-8'###可以上实际网页的html来看编码方式
      print("Header"+str(HeaderNum-1),uapool[HeaderNum-1])
      #print(response.text)
      print(response.status_code)
      #print(response.headers)
      time.sleep(TimeNum)
      print("\n等待"+str(TimeNum)+"秒，开始下一次爬取")

def random_ua():
  HeaderNum = random.randint(1, 10)
  ua = uapool[HeaderNum-1]
  return ua

#randomuser(uapool)