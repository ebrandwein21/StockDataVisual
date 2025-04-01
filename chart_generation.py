import pygal



##Generate a graph and open in the user’s default browser.
## bar graph
def generate_chart(labels,values, chart_type, symbol):


    if chart_type == '1':
        bar_chart = pygal.Bar()
        bar_chart.title = f"stock data bar graph"
        bar_chart.x_labels = labels
        bar_chart.add("Values", values)
        bar_chart.render_in_browser()
    
    if chart_type == '2':
        line_chart = pygal.Line()
        line_chart.title = f"stock data line graph"
        line_chart.x_labels = labels
        line_chart.add("Values", values)
        line_chart.render_in_browser()



def test_chart():
    line_chart = pygal.Line()
    line_chart.title = 'Browser usage evolution (in %)'
    line_chart.x_labels = map(str, range(2002, 2013))
    line_chart.add('Firefox', [None, None,    0, 16.6,   25,   31, 36.4, 45.5, 46.3, 42.8, 37.1])
    line_chart.add('Chrome',  [None, None, None, None, None, None,    0,  3.9, 10.8, 23.8, 35.3])
    line_chart.add('IE',      [85.8, 84.6, 84.7, 74.5,   66, 58.6, 54.7, 44.8, 36.2, 26.6, 20.1])
    line_chart.add('Others',  [14.2, 15.4, 15.3,  8.9,    9, 10.4,  8.9,  5.8,  6.7,  6.8,  7.5])
    line_chart.render_in_browser()

