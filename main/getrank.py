import requests
import uaselfpool
import bs4
import time
import dealdatabase


def getHTMLtext(url):
    r"""获取数据

     :param url: URL for the new :class:`Request` object.
     :param \*\*kwargs: Optional arguments that ``request`` takes.
     :return: :class:`Response <Response>` object
     :rtype: requests.Response
     """

    try:
        ua = uaselfpool.random_ua()
        r = requests.get(url, headers=ua)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        #print(r.encoding)
        # with open("weibo.html", "wb") as f:
        #   f.write(r.text.encode("utf-8"))
        # f.close()
        return r.text
    except:
        print("获取异常")
        return ""

def dealHTMLtext(html, i):
    flag = 1  # 用该flag是根据html内容设置的，因为第一个tr置顶数据不太一样
    ranktable = []
    # nowtime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    nowtime = time.strftime('%Y-%m-%d %H:%M', time.localtime(time.time()))  # 获取当前时间
    # 打开bs4解析器
    try:
        soup = bs4.BeautifulSoup(html,'html.parser')
    except:
        print("bs4解析出现错误")

    # 在下载回来的html中查找目标内容
    try:
        for tr in soup.find("tbody").children:
              if isinstance(tr, bs4.element.Tag):
                    if flag == 1:  # 针对第一个置顶的数据
                        rank = 0
                        content = tr.find("a").string
                        num = 00000
                        flag = 0
                        ranktable.append([rank, content, num, nowtime])
                    else:  # 处理有点击量的数据
                        try:
                            rank = tr.find('td', attrs={'class':'td-01 ranktop'}).string  # 排名
                            content = tr.find('a').string  # 话题内容
                            #print(type(rank), type(content))
                            num = tr.find("span").string  # 点击量
                            ranktable.append([rank, content, num, nowtime])
                        except:
                            print('一组数据异常')

        print("第", i+1, "次爬取录入完成！爬取结果：\n ", ranktable)
        text = "第" + str(i+1) + "次爬取"
        with open("htmltext/" + text + ".txt", "a", encoding="utf-8") as f:
            # 参数a代表如果文件存在，就在文件最后面追加写，不存在就创建文件，ab的话是以二进制打开，其他都一样
            f.write(str(text)+"\n"+str(ranktable)+"\n")
        f.close()
        return ranktable
    except:
        print("第", i+1, "次爬取解析HTML失败！跳过\n")
        return ranktable


if __name__=="__main__":
    url = "https://s.weibo.com/top/summary?Refer=top_hot&topnav=1&wvr=6"
    interval = 60  # 爬取间隔多少秒
    times = 10000  # 爬取多少次

    for i in range(times):
       html = getHTMLtext(url)

       ranktable = dealHTMLtext(html, i)

       dealdatabase.save_data(ranktable)

       time.sleep(interval)

    # return
    # restoredata()

