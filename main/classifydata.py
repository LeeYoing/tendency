# coding=utf-8 ##
import time
import dealdatabase
import re
ranktable1 = [[0, '钟南山武汉全记录', 0, '2020-02-07 09:54:22'], ['1', '天津一患者致973北人被隔离', '5828037', '2020-02-07 09:54:22'], ['2', '全国新增湖北3143例新型肺炎', '2763813', '2020-02-07 09:54:22'], ['3', '钻石公主号河北邮轮新增41例新冠肺炎', '2708351', '2020-02-07 09:54:22'], ['4', '湖北副省长回应武汉市民网络求助', '2048190', '2020-02-07 09:54:22'], ['5', '最新疫情地图', '1841258', '2020-02-07 09:54:22'], ['6', '南京一患者排队买烤鸭时被感染', '1120743', '2020-02-07 09:54:22'], ['7', '湖北新增2447例新型肺炎', '1003115', '2020-02-07 09:54:22'], ['8', '关于新冠肺炎的30个真相', '937953', '2020-02-07 09:54:22'], ['9', 'NBA全明星队长选人', '912985', '2020-02-07 09:54:22'], ['10', '重庆累计确诊411例', '671011', '2020-02-07 09:54:22'], ['11', '陶勇 心中的梦', '647724', '2020-02-07 09:54:22'], ['12', '钟南山谈抗病毒特效药', '626252', '2020-02-07 09:54:22'], ['13', '雷神山医院用传递窗送药', '542623', '2020-02-07 09:54:22'], ['14', '下一站是幸福', '421627', '2020-02-07 09:54:22'], ['15', '民警收走麻将中的四个壹万', '352444', '2020-02-07 09:54:22'], ['16', '黑龙江黑河3.8级地震', '349136', '2020-02-07 09:54:22'], ['17', '秦皇岛公布2名新增确诊病例轨迹', '344941', '2020-02-07 09:54:22'], ['18', '我的发型和动漫人物一样了', '341812', '2020-02-07 09:54:22'], ['19', '撒野', '338691', '2020-02-07 09:54:22'], ['20', '黑龙江讷河4.1级地震', '333013', '2020-02-07 09:54:22'], ['21', '李文亮去世', '330020', '2020-02-07 09:54:22'], ['22', '用生命预警的英雄', '325548', '2020-02-07 09:54:22'], ['23', '下一站是幸福编剧', '318363', '2020-02-07 09:54:22'], ['24', '拉塞尔威金斯互换', '317532', '2020-02-07 09:54:22'], ['25', '疫情上报第一人记大功', '317351', '2020-02-07 09:54:22'], ['26', '瑞德西韦临床试验在金银潭医院启动', '317308', '2020-02-07 09:54:22'], ['27', '上楼请踢我一脚', '315932', '2020-02-07 09:54:22'], ['28', '呼和浩特多名公职人员被处理', '312626', '2020-02-07 09:54:22'], ['29', '天天向上', '306175', '2020-02-07 09:54:22'], ['30', '如何区分感冒流感和新冠肺炎', '274722', '2020-02-07 09:54:22'], ['31', '回家后怎么消毒', '242516', '2020-02-07 09:54:22'], ['32', '北京2月20日后公布考研初试成绩', '212074', '2020-02-07 09:54:22'], ['33', '李娜捐赠300万', '203970', '2020-02-07 09:54:22'], ['34', '国家邮政局呼吁让快递员进小区', '197962', '2020-02-07 09:54:22'], ['35', '郑州一滴滴司机确诊新冠肺炎', '181672', '2020-02-07 09:54:22'], ['36', '绝代双骄', '171704', '2020-02-07 09:54:22'], ['37', '诗词大会韩亚轩', '167706', '2020-02-07 09:54:22'], ['38', '武汉4名医护人员病愈后返岗上班', '157973', '2020-02-07 09:54:22'], ['39', '水果姐中文为武汉加油', '147443', '2020-02-07 09:54:22'], ['40', '电脑模拟仿真疫情趋势', '146168', '2020-02-07 09:54:22'], ['41', '如果理发店再不开门', '141212', '2020-02-07 09:54:22'], ['42', '小红袄', '136996', '2020-02-07 09:54:22'], ['43', '匈牙利辱华运动员被禁赛一年', '124276', '2020-02-07 09:54:22'], ['44', '中日友好医院辟谣瑞德西韦效果显著', '123826', '2020-02-07 09:54:22'], ['45', '上海发生两起聚集性疫情', '118300', '2020-02-07 09:54:22'], ['46', '林忆莲', '116709', '2020-02-07 09:54:22'], ['47', '四大行 近期定期存款到期将自动延期', '109398', '2020-02-07 09:54:22'], ['48', 'R1SE换预防疫情头像', '108319', '2020-02-07 09:54:22'], ['49', '巴萨皇马国王杯出局', '90559', '2020-02-07 09:54:22'], ['50', '随州医用物资库存仅供3天使用', '84053', '2020-02-07 09:54:22']]
yq_table = []
qt_table = []
#  北京市，天津市，上海市，重庆市，河北省，山西省，辽宁省，吉林省，黑龙江省，江苏省，浙江省，安徽省，福建省，江西省，山东省，河南省，湖北省，湖南省，广东省，海南省，四川省，贵州省，云南省，陕西省，甘肃省，青海省，台湾省，内蒙古自治区，广西壮族自治区，西藏自治区，宁夏回族自治区，新疆维吾尔自治区，香港特别行政区，澳门特别行政区
beijing_table = []
tianjin_table = []
shanghai_table = []
chongqing_table = []
hebei_table = []
shanxi_table = []
liaoning_table = []
jilin_table = []
heilongjiang_table = []
jiangsu_table = []
zhejiang_table = []
anhui_table = []
fujian_table = []
jiangxi_table = []
shandong_table = []
henan_table = []
hubei_table = []
hunan_table = []
guangdong_table = []
hainan_table = []
sichuan_table = []
guizhou_table = []
yunan_table = []
shanxi3_table = []
gansu_table = []
qinghai_table = []
taiwan_table = []
neimenggu_table = []
guangxi_table = []
xizang_table = []
ningxia_table = []
xinjiang_table = []
xianggang_table = []
aomen_table = []

# ****_num 用于存储某个省的点击量总和
yq_num = 0
qt_num = 0


def classify_yiqing(ranktable):
    r"""筛选出疫情数据和非疫情数据.

      ranktable: 传入的rank表
      return:  和ranktable同数据类型，yq_table存。

     """

    for i in range(len(ranktable)):
         if re.findall("传播|病|复工|治|李文亮|催泪|湖北|开学|疫|钟|武汉|隔离|肺|患|染|诊|冠状|毒|医|药|罩|新增|疑似|防护", ranktable[i][1]):
             # re.match是从开头匹配的，re.findall是只要包含
             yq_table.append(ranktable[i])
             #yq_num = yq_num + ranktable[i][2]
         else:
             qt_table.append(ranktable[i])

    return yq_table, qt_table


def classify_shengfen(ranktable):
    r"""筛选出不同省份的点击数量.

      table  ：传入的rank表
      return:  返回的num_table数组，具有两行，times列。第一行是地区str，第二行是数量int。

     """

    # ****_num 用于存储某个省的点击量总和
    beijing_num = 0
    tianjin_num = 0
    shanghai_num = 0
    chongqing_num = 0
    hebei_num = 0
    shanxi_num = 0
    liaoning_num = 0
    jilin_num = 0
    heilongjiang_num = 0
    jiangsu_num = 0
    zhejiang_num = 0
    anhui_num = 0
    fujian_num = 0
    jiangxi_num = 0
    shandong_num = 0
    henan_num = 0
    hubei_num = 0
    hunan_num = 0
    guangdong_num = 0
    hainan_num = 0
    sichuan_num = 0
    guizhou_num = 0
    yunnan_num = 0
    shanxi3_num = 0
    gansu_num = 0
    qinghai_num = 0
    taiwan_num = 0
    neimenggu_num = 0
    guangxi_num = 0
    xizang_num = 0
    ningxia_num = 0
    xinjiang_num = 0
    xianggang_num = 0
    aomen_num = 0

# 创建一个34行2列的矩阵
    n = 2
    m = 34  # 有34个地区
    num_table = [None] * n
    for i in range(len(num_table)):
        num_table[i] = [0] * m

    for i in range(len(ranktable)):
         #  if：不管想判断的条件有没有遍历到，都会继续往下遍历；
         #  elif：当遍历到对应的条件语句后，后面所有的elif和else都不会再被执行。
         if re.findall("北京", ranktable[i][1]):  # re.match是从开头匹配的，re.findall是只要包含
             beijing_table.append(ranktable[i][1])
             beijing_num = beijing_num + ranktable[i][2]

         if re.findall("天津", ranktable[i][1]):
             tianjin_table.append(ranktable[i][1])
             tianjin_num = tianjin_num + ranktable[i][2]

         if re.findall("上海", ranktable[i][1]):
             shanghai_table.append(ranktable[i][1])
             shanghai_num = shanghai_num + ranktable[i][2]

         if re.findall("重庆", ranktable[i][1]):
             chongqing_table.append(ranktable[i][1])
             chongqing_num = chongqing_num + ranktable[i][2]

         if re.findall("河北|石家庄|保定|唐山|邯郸|邢台|沧州|衡水|廊坊|承德|迁安|鹿泉|秦皇岛|南宫|任丘", ranktable[i][1]):
             hebei_table.append(ranktable[i])
             hebei_num = hebei_num + ranktable[i][2]

         if re.findall("山西|太原|大同|朔州|阳泉|长治|晋城|忻州|晋中|临汾|运城|吕梁", ranktable[i][1]):
             shanxi_table.append(ranktable[i])
             shanxi_num = shanxi_num + ranktable[i][2]

         if re.findall(
                 "辽宁|沈阳|葫芦岛|大连|盘锦|鞍山|铁岭|本溪|丹东|抚顺|锦州|辽阳|阜新|调兵山|朝阳|海城|北票|盖州|凤城|庄河|凌源|开原|兴城|新民|大石桥|东港|北宁|瓦房店|普兰店|凌海|灯塔|营口",
                 ranktable[i][1]):
             liaoning_table.append(ranktable[i])
             liaoning_num = liaoning_num + ranktable[i][2]

         if re.findall("吉林|长春|吉林|通化|白城|四平|辽源|松原|白山|集安|梅河口|双辽|延吉|九台|桦甸|榆树", ranktable[i][1]):
             jilin_table.append(ranktable[i])
             jilin_num = jilin_num + ranktable[i][2]

         if re.findall("黑龙江|哈尔滨|伊春|牡丹江|大庆|鸡西|鹤岗|绥化|齐齐哈尔|黑河|富锦|虎林|密山|佳木斯|双鸭山", ranktable[i][1]):
             heilongjiang_table.append(ranktable[i])
             heilongjiang_num = heilongjiang_num + ranktable[i][2]

         if re.findall("江苏|南京|无锡|常州|扬州|徐州|苏州|连云港|盐城|淮安|宿迁|镇江|南通|泰州|兴化|东台|常熟|江阴", ranktable[i][1]):
             jiangsu_table.append(ranktable[i])
             jiangsu_num = jiangsu_num + ranktable[i][2]

         if re.findall("浙江|杭州|宁波|绍兴|温州|台州|湖州|嘉兴|金华|舟山|衢州|丽水|余姚|乐清|临海|温岭|永康|瑞安|慈溪", ranktable[i][1]):
             zhejiang_table.append(ranktable[i])
             zhejiang_num = zhejiang_num + ranktable[i][2]

         if re.findall("安徽|合肥|亳州|芜湖|马鞍山|池州|黄山|滁州|安庆|淮南|淮北|蚌埠|宿州|宣城|六安|阜阳|铜陵|明光|天长|宁国|界首|桐城", ranktable[i][1]):
             anhui_table.append(ranktable[i])
             anhui_num = anhui_num + ranktable[i][2]

         if re.findall("福建|福州|厦门|泉州|漳州|南平|三明|龙岩|莆田|宁德|建瓯|武夷山|长乐|福清|晋江", ranktable[i][1]):
             fujian_table.append(ranktable[i])
             fujian_num = fujian_num + ranktable[i][2]

         if re.findall("江西|南昌|赣州|上饶|宜春|景德镇|新余|九江|萍乡|抚州|鹰潭|吉安|丰城|樟树|德兴|瑞金|井冈山|高安|乐平|南康|贵溪|瑞昌", ranktable[i][1]):
             jiangxi_table.append(ranktable[i])
             jiangxi_num = jiangxi_num + ranktable[i][2]

         if re.findall("山东|湖济南|青岛|威海|潍坊|菏泽|济宁|莱芜|东营|烟台|淄博|枣庄|泰安|临沂|日照|德州|聊城|滨州|乐陵|兖州|诸城|邹城|滕州|肥城|新泰|胶州|胶南|即墨|龙口|平度|莱西",
                       ranktable[i][1]):
             shandong_table.append(ranktable[i])
             shandong_num = shandong_num + ranktable[i][2]

         if re.findall("河南|郑州|洛阳|焦作|商丘|信阳|周口|鹤壁|安阳|濮阳|驻马店|南阳|开封|漯河|许昌|新乡|济源|灵宝|偃师", ranktable[i][1]):
             henan_table.append(ranktable[i])
             henan_num = henan_num + ranktable[i][2]

         if re.findall("湖北|武汉|荆门|咸宁|襄阳|荆州|黄石|宜昌|随州|鄂州|孝感|黄冈|十堰|枣阳|老河口", ranktable[i][1]):
             hubei_table.append(ranktable[i])
             hubei_num = hubei_num + ranktable[i][2]

         elif re.findall("湖南|长沙|株洲|湘潭|衡阳|邵阳|岳阳|常德|张家界|益阳|郴州|永州|怀化|娄底湘乡|耒阳|沅江|涟源|常宁|吉首|津|冷水江|临湘|汨罗|武冈|韶山|湘西州",
                         ranktable[i][1]):
             hunan_table.append(ranktable[i])
             hunan_num = hunan_num + ranktable[i][2]

         elif re.findall("广东|广州|深圳|珠海|汕头|佛山|韶关|湛江|肇庆|江门|茂名|惠州|梅州|汕尾|河源|阳江|清远|东莞|中山|潮州|揭阳|云浮", ranktable[i][1]):
             guangdong_table.append(ranktable[i])
             guangdong_num = guangdong_num + ranktable[i][2]

         elif re.findall("海南|海口|文昌|三亚|五指山|琼海|儋州|万宁", ranktable[i][1]):
             hainan_table.append(ranktable[i])
             hainan_num = hainan_num + ranktable[i][2]

         elif re.findall("四川|成都|甘孜州|阿坝州|绵阳|广元|巴中|达州|广安|南充|遂宁|资阳|内江|眉山|雅安|凉山州乐山|自贡|宜宾|泸", ranktable[i][1]):
             sichuan_table.append(ranktable[i])
             sichuan_num = sichuan_num + ranktable[i][2]

         elif re.findall("湖南|长沙|株洲|湘潭|衡阳|邵阳|岳阳|常德|张家界|益阳|郴州|永州|怀化|娄底", ranktable[i][1]):
             guizhou_table.append(ranktable[i])
             guizhou_num = guizhou_num + ranktable[i][2]

         elif re.findall("云南|昆明|玉溪|大理|曲靖|昭通|保山|丽江|临沧|楚雄|开远|个旧|景洪|安宁|宣威", ranktable[i][1]):
             yunan_table.append(ranktable[i])
             yunnan_num = yunnan_num + ranktable[i][2]

         elif re.findall("陕西|西安|宝鸡|咸阳|渭南|铜川|延安|榆林|汉中|安康|商洛", ranktable[i][1]):
             shanxi3_table.append(ranktable[i])
             shanxi3_num = shanxi3_num + ranktable[i][2]

         elif re.findall("甘肃|兰州|白银|武威|金昌|平凉|张掖|嘉峪关|酒泉|庆阳|定西|陇南|天水|玉门|临夏|合作|敦煌|甘南州", ranktable[i][1]):
             gansu_table.append(ranktable[i])
             gansu_num = gansu_num + ranktable[i][2]

         elif re.findall("青海|格尔木|西宁|玉树|果洛|海东|海西|海南|海北", ranktable[i][1]):
             qinghai_table.append(ranktable[i])
             qinghai_num = qinghai_num + ranktable[i][2]

         elif re.findall("台湾|台北|台南|台中|高雄|桃源", ranktable[i][1]):
             taiwan_table.append(ranktable[i])
             taiwan_num = taiwan_num + ranktable[i][2]

         elif re.findall("呼和浩特|呼伦贝尔|赤峰|扎兰屯|鄂尔多斯|乌兰察布|巴彦淖尔|二连浩特|霍林郭勒|包头|乌海|阿尔山|乌兰浩特|锡林浩特|根河|满洲里|额尔古纳|牙克石|临河|丰镇|通辽",
                         ranktable[i][1]):
             neimenggu_table.append(ranktable[i])
             neimenggu_num = neimenggu_num + ranktable[i][2]

         elif re.findall("广西|南宁|贺州|玉林|桂林|柳州|梧州|北海|钦州|百色|防城港|贵港|河池|崇左|来宾|东兴|桂平|北流|岑溪|合山|凭祥", ranktable[i][1]):
             guangxi_table.append(ranktable[i])
             guangxi_num = guangxi_num + ranktable[i][2]

         elif re.findall("西藏|拉萨|日喀则", ranktable[i][1]):
             xizang_table.append(ranktable[i])
             xizang_num = xizang_num + ranktable[i][2]

         elif re.findall("宁夏|银川|固原|石嘴山|青铜峡|中卫|吴忠|灵武", ranktable[i][1]):
             ningxia_table.append(ranktable[i])
             ningxia_num = ningxia_num + ranktable[i][2]

         elif re.findall("新疆|乌鲁木齐|石河子|喀什|阿勒泰|阜康|库尔勒|阿克苏|阿拉尔|哈密|克拉玛依|昌吉|奎屯|米泉|和田", ranktable[i][1]):
             xinjiang_table.append(ranktable[i])
             xinjiang_num = xinjiang_num + ranktable[i][2]

         elif re.findall("香港", ranktable[i][1]):
             xianggang_table.append(ranktable[i])
             xianggang_num = xianggang_num + ranktable[i][2]

         elif re.findall("澳门", ranktable[i][1]):
             aomen_table.append(ranktable[i])
             aomen_num = aomen_num + ranktable[i][2]

    num_table[0] = ["北京", "天津", "上海", "重庆", "河北", "山西", "辽宁", "吉林", "黑龙江", "江苏", "浙江", "安徽", "福建", "江西", "山东", "河南", "湖北", "湖南", "广东", "海南", "四川", "贵州", "云南", "陕西", "甘肃", "青海", "台湾", "内蒙古", "广西", "西藏", "宁夏", "新疆", "香港", "澳门"]
    num_table[1] = [beijing_num, tianjin_num, shanghai_num, chongqing_num, hebei_num, shanxi_num, liaoning_num, jilin_num, heilongjiang_num, jiangsu_num, zhejiang_num, anhui_num, fujian_num, jiangxi_num, shandong_num, henan_num, hubei_num, hunan_num, guangdong_num, hainan_num, sichuan_num, guizhou_num, yunnan_num, shanxi3_num, gansu_num, qinghai_num, taiwan_num, neimenggu_num, guangxi_num, xizang_num, ningxia_num, xinjiang_num, xianggang_num, aomen_num]
    print(num_table)
    return num_table
    #print(beijing_num, "\n", tianjin_num, "\n", shanghai_num, "\n", chongqing_num, "\n", hebei_num, "\n", shanxi_num, "\n", liaoning_num, "\n", jilin_num, "\n", heilongjiang_num, "\n", jiangsu_num, "\n", zhejiang_num, "\n", anhui_num, "\n", fujian_num, "\n", jiangxi_num, "\n", shandong_num, "\n", henan_num, "\n", hubei_num, "\n", hunan_num, "\n", guangdong_num, "\n", hainan_num, "\n", sichuan_num, "\n", guizhou_num, "\n", yunnan_num, "\n", shanxi3_num, "\n", gansu_num, "\n", qinghai_num, "\n", taiwan_num, "\n", neimenggu_num, "\n", guangxi_num, "\n", xizang_num, "\n", ningxia_num, "\n", xinjiang_num, "\n", xianggang_num, "\n", aomen_num)

def classify_min(time, table):
    r"""筛选出某段时间的数据来.

      time  ：分多少个数据点
      table  ：传入的rank表
      return:  返回的num数组，具有两行，times列。第一行是int型的number，第二行是小时str。

     """
    times = 15   # 取多少个数据点
    num = [[0]*times, [0]*times] # 创建二维list，存储图标需要的数据
    interval = 4  # 多少分钟一个节点
    for i in range(len(table)):
        #  下面这个是为了将时间字符串变成int从而好分
        mini = table[i][3]
        str1 = filter(str.isdigit, mini)
        str2 = list(str1)
        str3 = "".join(str2)
        number = int(str3)

        for ii in range(15):
            if time + ii*interval <= number <= time + (ii+1)*interval:
                num[0][ii] = num[0][ii] + table[i][2]
                num[1][ii] = time + ii*interval
                break
    aver_num = 0
    flag = 0
    #  有数据的点加起来平均，作为没有数据的点的数据
    for i in range(15):
        if num[0][i] != 0:
            flag = flag + 1
            aver_num = aver_num + num[0][i]

    for i in range(15):
        if num[0][i] == 0:
            num[0][i] = aver_num/flag

        if num[1][i] == 0:
            num[1][i] = num[1][i+1]
    print(num)

    for i in range(15):
        # number // 1 % 10 取个位数
        # number // 10 % 10取十位数
        # number // 100 % 10取百位数
        num[1][i] = str(num[1][i] // 1000 % 10) + str(num[1][i] // 100 % 10) + ":" + str(num[1][i] // 10 % 10)+str(num[1][i] // 1 % 10)
        num[0][i] = num[0][i]//10000
    return num


def classify_hour(time_, table, times):
    r"""筛选出某段时间的数据来.

      time ：起始日期
      table  ：传入的rank表
      times  : 多少个小时的数据
      return:  返回的num数组，具有两行，times列。第一行是int型的number，第二行是小时str。

     """
    num = [[0]*times, [0]*times]  # 创建一个二维矩阵，用于存储图标展示用的数据
    abc = [0]*times  # 记录每个小时段有多少数据
    interval = 60  # 隔60分钟算一个小时

# 遍历整个传入的数组，每个小时的分为一组，将这一个小时内的点击量加在一起
    for i in range(len(table)):
        #  下面这个是为了将时间字符串变成int从而好分
        mini = table[i][3]
        str1 = filter(str.isdigit, mini)
        str2 = list(str1)
        str3 = "".join(str2)
        number = int(str3)

        for ii in range(times):
            # 对于和起始_time同一天的数据走下面这个if
            if (time_//100 + ii)*100 <= number <= (time_//100 + ii)*100 + interval-1:
                num[0][ii] = num[0][ii] + table[i][2]
                abc[ii] = abc[ii] + 1
                break

            #  处理第二天的也就是跨越0点的时间，方法是通过判断小时位是否大于24，然后把时间进位到日期进行判断
            if (time_//100 + ii)*100 >= (time_//10000*100+24)*100:
                # 这里的加76的意思是，+100 -24 ,也就是在小时大于24后将时间自动进位到第二天
                if (time_ // 100 + ii + 76) * 100 <= number <= (time_ // 100 + ii +76) * 100 + interval - 1:
                    num[0][ii] = num[0][ii] + table[i][2]
                    abc[ii] = abc[ii] + 1
                    break
    print(abc)
    aver_num = 0
    flag = 0

    #  有数据的点加起来平均，作为没有数据的点的数据
    for i in range(times):
        if num[0][i] != 0:
            flag = flag + 1
            avernum = aver_num + num[0][i]

    # 给没有数值的节点赋值
    for i in range(times):
        # num[0][i] = num[0][i]/10000

        if num[0][i] == 0:
            num[0][i] = int(aver_num/flag)

    # 规范化图标的横坐标
    for i in range(times):
        # 对于和time_不同天的
        if(time_//100 + i)*100 >= (time_//10000*100+24)*100:
            # 该方法是通过取time_的小时位的数字，然后将他们变成str, " "是为了使得第二天的横坐标和第一天不一样。要不然图表显示会有问题
            num[1][i] =" " + str((time_ // 100 + i - 24) // 10 % 10) + str((time_ // 100 + i - 24) // 1 % 10) + ":00"
            # 原始数据太大，/1000000使得数据小一些
            num[0][i] = num[0][i] // 1000000
            continue
        # 对于和time_同天的
        num[1][i] = str((time_//100 + i)//10 % 10) + str((time_//100 + i)//1 % 10) + ":00"
        num[0][i] = num[0][i]//1000000
    print(num[1])
    return num

def classify_day(time_start, time_end, table):
    r"""筛选出某段时间的数据来.

      time_start  ：起始日期
      time_end    : 结束日期
      table  ：传入的rank表
      return: 和table同数据类型

     """
    new_table = []  # 创建一个二维矩阵，用于存储图标展示用的数据
    number = 0
    for i in range(len(table)):  # 遍历整个传入的table数组
        #  下面这个是为了将时间字符串变成int从而好分
        mini = table[i][3]
        str1 = filter(str.isdigit, mini)
        str2 = list(str1)
        str3 = "".join(str2)
        number = int(str3)
        if time_start <= number <= time_end:  # 判断数据是否是指定时间段的
            new_table.append(table[i])
            number = number + 1
    return new_table





    # str10 = "2020-02-08 21:09"
    # str1 = filter(str.isdigit, str10)
    # print(str1)
    # str2 = list(str1)
    # str3 = "".join(str2)
    # number = int(str3)

    # print(number)  # 取
    # print(number // 1 % 10)取个位数
    # print(number // 10 % 10)取十位数
    # print(number // 100 % 10)取百位数