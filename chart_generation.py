import pygal


##Generate a graph and open in the user’s default browser.
## bar graph
def generate_chart(labels, values, chart_type='1'):
    
    if chart_type == '1':
        bar_chart = pygal.Bar()
        bar_chart.title = "stock data bar graph"
        bar_chart.x_labels = labels
        bar_chart.add("Values", values)
        bar_chart.render()
    
    if chart_type == '2':
        line_chart = pygal.Line()
        line_chart.title = "stock data line graph"
        line_chart.x_labels = labels
        line_chart.add("Values", values)
        line_chart.render()






