from pyecharts.charts import *
from pyecharts import options as opts


def pie_with_multi_titles():
    pie = Pie(init_opts=opts.InitOpts(theme='light',
                                      width='1000px',
                                      height='800px'))
    pie.add("",
            [list(z) for z in zip(["合作", "非合作"], [24, 38])],
            # 指定饼图中心位置
            center=["22%", "10%"],
            # 将饼图尺寸相应缩小，不然饼图会重叠
            radius=[60, 80]).set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c} ({d}%)"))

    pie.add("",
            [list(z) for z in zip(["合作", "非合作"], [18, 38])],
            # 指定饼图中心位置
            center=["57%", "10%"],
            # 将饼图尺寸相应缩小，不然饼图会重叠
            radius=[60, 80]).set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c} ({d}%)"))

    pie.add("",
            [list(z) for z in zip(["合作", "非合作"], [13, 31])],
            # 指定饼图中心位置
            center=["22%", "40%"],
            # 将饼图尺寸相应缩小，不然饼图会重叠
            radius=[60, 80]).set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c} ({d}%)"))

    pie.add("",
            [list(z) for z in zip(["合作", "非合作"], [29, 53])],
            # 指定饼图中心位置
            center=["57%", "40%"],
            # 将饼图尺寸相应缩小，不然饼图会重叠
            radius=[60, 80]).set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c} ({d}%)"))

    pie.add("",
            [list(z) for z in zip(["合作", "非合作"], [84, 160])],
            # 指定饼图中心位置
            center=["22%", "70%"],
            # 将饼图尺寸相应缩小，不然饼图会重叠
            radius=[60, 80]).set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c} ({d}%)"))

    pie.set_global_opts(title_opts=[dict(text='2019年', top='9%', left='18.5%'),
                                    dict(text='2020年', top='9%', left='54%'),
                                    dict(text='2021年', top='38.5%', left='18.5%'),
                                    dict(text='2022年', top='38.5%', left='54%'),
                                    dict(text='累计', top='68.5%', left='20%'),],
                        legend_opts=opts.LegendOpts(is_show=False)  # 设置图例是否显示
                        )
    return pie


if __name__ == '__main__':
    chart = pie_with_multi_titles()
    chart.render(path='pie_with_multi_titles.html')
