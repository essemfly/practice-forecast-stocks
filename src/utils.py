def get_index_of_date(stock_prices_data, date):
    for i, d in enumerate(stock_prices_data["date"]):
        if d == date:
            return i
    return -1
