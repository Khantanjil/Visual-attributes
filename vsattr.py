from bokeh.plotting import show
from bokeh.plotting import figure
from bokeh.plotting import output_file

plotting = figure(plot_width=500, plot_height=500, tools="pan, reset")
plotting.title.text = "Earthquakes"
plotting.title.text_color = "Orange"
plotting.title.text_font = "times"
plotting.title.text_font_style = "italic"
plotting.xaxis.minor_tick_line_color = "Yellow"
plotting.yaxis.minor_tick_line_color = None
plotting.xaxis.axis_label = "Times"
plotting.yaxis.axis_label = "Values"
plotting.circle(
    [1, 2, 3, 4, 5],
    [5, 6, 5, 5, 3],
    size=[i * 2 for i in [8, 12, 14, 15, 20]],
    color="red",
    alpha=0.5
)

output_file("scatter_plotting.html")
show(plotting)