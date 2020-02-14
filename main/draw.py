import dealdatabase
import classifydata
import pyecharts.options as opts
from pyecharts.faker import Faker
from pyecharts.charts import Line
from pyecharts.charts import Page, WordCloud
from pyecharts.globals import SymbolType


# 画折线图，下面这种方法是链式调用
def line_base(yq_result, qt_result) -> Line:
    c = (
        Line()
        .add_xaxis(yq_result[1])  # 需要数据类型是字符串才可以正常显示
        .add_yaxis("疫情相关", yq_result[0], is_smooth=True)  # 需要数组里面的元素是tuple
        .add_yaxis("其他", qt_result[0], is_smooth=True)     # 同上
        .set_global_opts(title_opts=opts.TitleOpts(title="热点分析"))  # 设置标题名
        #.set_global_opts(toolbox_opts=opts.ToolBoxFeatureOpts(save_as_image={"show": True, "title": "save", "type": "png"}))
        # .set_series_opts(label_opts=opts.LabelOpts(color="red"))  # 设置标签颜色
    )
    return c


# 画词云图
def wordcloud_base(words) -> WordCloud:
    c = (
        WordCloud()
        .add("", words, word_size_range=[20, 80])  # words的格式为[("Sam S Club", 10000),("Macys", 6181)]， 后面的参数代表字的大小范围
        .set_global_opts(title_opts=opts.TitleOpts(title="疫情词云"))
    )
    return c


# 用数据画折线图
def draw_line(date, times):  # data代表起始日期，int型，如202002101000；times代表画几个节点
    result = dealdatabase.search_data("select * from hotrank")
    yq_table, qt_table = classifydata.classify_yiqing(result)
    print(qt_table)
    yq_result = classifydata.classify_hour(date, yq_table, times)
    qt_result = classifydata.classify_hour(date, qt_table, times)
    line_base(yq_result, qt_result).render("tendency.html")


# 用数据画词云图
def draw_words(time_start, time_end):
    word_table = []  # 用于画图的数据
    result = dealdatabase.search_data("select * from hotrank")
    classify_result = classifydata.classify_day(time_start, time_end, result)
    num_table = classifydata.classify_shengfen(classify_result)
    for i in range(len(num_table[0])):
            if num_table[1][i] != 0:  # 只有有热点的省份才显示出来
                word_table.append(tuple([num_table[0][i], num_table[1][i]]))
    print(word_table)
    wordcloud_base(word_table).render("couldwords.html")




