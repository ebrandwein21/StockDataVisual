#import from other files
from userinput import (
    get_chart_type,
    get_stock_symbol,
    get_function,
    get_start_date,
    get_end_date,

)

from api_handling import fetch_stock_data
from chart_generation import generate_chart



def filter_data_by_date(data, start_date, end_date):
    """
    Filter the stock data based on the provided date range.
    """

    time_series_key = next((key for key in data if "Time series" in key), None)
    if not time_series_key:
        print("Invalid data format")
        return{}
    
    time_series_data = data[time_series_key]
    filtered ={
        date: values for date, values in time_series_data.items()
        if start_date <= date <= end_date
    }

    return filtered



def main():

    print("Stock Data Visualizer")
    print("---------------------")

    symbol = get_stock_symbol()
    chart_type = get_chart_type()
    function = get_function()
    start_date = get_start_date()
    end_date = get_end_date(start_date)

    data = fetch_stock_data(symbol, function)

    if data is None:
        print("Failed to fetch stock data. Please try again later.")
        return
    
    filtered_data = filter_data_by_date(data, start_date, end_date)


    if not filtered_data:
        print("No stock data avalible. Try a different date.")
        return
    
    generate_chart(filtered_data, chart_type, symbol)


if __name__ == "__main__":
    main()