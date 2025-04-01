import pygal


##Generate a graph and open in the user’s default browser.
## bar graph
def generate_chart(filtered_data, chart_type='1', symbol=''):
    
    dates = list(filtered_data.keys())
    values = [float(data['Prices']) for data in filtered_data.values()]
    
    if chart_type == '1':
        bar_chart = pygal.Bar()
        bar_chart.title = f"{symbol}stock data bar graph"
        bar_chart.x_labels = dates
        bar_chart.add("Price", values)
        bar_chart.render_in_browser()
    
    if chart_type == '2':
        line_chart = pygal.Line()
        line_chart.title = f"{symbol}stock data line graph"
        line_chart.x_labels = dates
        line_chart.add("Price", values)
        line_chart.render_in_browser()






