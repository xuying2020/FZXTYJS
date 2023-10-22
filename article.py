from pyecharts import options as opts
from pyecharts.charts import Bar, Grid, Line

x_data = ['2019年','2020年','2021年','2022年']
bar = (
    Bar()
    .add_xaxis(x_data)
    .add_yaxis(
        "SCI一区",
        [2,5,5,13],
        yaxis_index=0,
        #color="#d14a61",
    )
    .add_yaxis(
        "SCI二区",
        [26,14,17,22],
        yaxis_index=0,
        #color="#0B9604",
    )
    .add_yaxis(
        "SCI三区",
        [9,12,12,19],
        yaxis_index=0,
        #color="#A1E3F4",
    )
    .add_yaxis(
        "SCI四区",
        [15,11,6,12],
        yaxis_index=0,
        #color="#6723B1",
    )
    .add_yaxis(
        "非SCI",
        [10,14,4,16],
        yaxis_index=0,
       # color="#E87DB0",
    )
    .extend_axis(
        yaxis=opts.AxisOpts(
            name="分区篇数",
            type_="value",
            min_=0,
            max_=30,
            position="left",
            axisline_opts=opts.AxisLineOpts(
                #linestyle_opts=opts.LineStyleOpts(color="#03070D")
            ),
            axislabel_opts=opts.LabelOpts(formatter="{value} 篇"),
        )
    )
    .extend_axis(
        yaxis=opts.AxisOpts(
            type_="value",
            name="每年总篇数",
            min_=0,
            max_=100,
            position="right",
            axisline_opts=opts.AxisLineOpts(
               # linestyle_opts=opts.LineStyleOpts(color="#675bba")
            ),
            axislabel_opts=opts.LabelOpts(formatter="{value} 篇"),
            splitline_opts=opts.SplitLineOpts(
                is_show=True, linestyle_opts=opts.LineStyleOpts(opacity=1)
            ),
        )
    )
    .set_global_opts(
        yaxis_opts=opts.AxisOpts(
            name="分区篇数",
            min_=0,
            max_=30,
            position="left",
            offset=80,
            axisline_opts=opts.AxisLineOpts(
                #linestyle_opts=opts.LineStyleOpts(color="#03070D")
            ),
            axislabel_opts=opts.LabelOpts(formatter="{value} 篇"),
        ),
        title_opts=opts.TitleOpts(title="复杂系统研究所论文情况"),
        tooltip_opts=opts.TooltipOpts(trigger="axis", axis_pointer_type="cross"),
    )
)

line = (
    Line()
    .add_xaxis(x_data)
    .add_yaxis(
        "总篇数",
        [62,56,44,82],
        yaxis_index=2,
        #color="#850730",
        label_opts=opts.LabelOpts(is_show=False),
    )
)

bar.overlap(line)
grid = Grid()
grid.add(bar, opts.GridOpts(pos_left="5%", pos_right="20%"), is_control_axis_index=True)
grid.render("grid_multi_yaxis.html")
