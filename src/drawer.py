import matplotlib.pyplot as plt
from src.utils import get_index_of_date


def plot_multiple_tickers(df, ticker, analyze_duration, similar_tickers):
    plt.figure(figsize=(12, 6))

    base_ticker_df = df[ticker][-analyze_duration:]

    plt.plot(base_ticker_df, label=ticker, linewidth=2.5)

    for similar_ticker in similar_tickers:
        ticker_name = similar_ticker[1]
        start_date = similar_ticker[2]
        end_date = similar_ticker[3]
        start_date_index = get_index_of_date(df, start_date)
        end_date_index = get_index_of_date(df, end_date)
        plt.plot(df[ticker_name][start_date_index:end_date_index], label=similar_ticker)

    plt.title(f"Comparison of {ticker} with Similar Tickers")
    plt.xlabel("Date")
    plt.ylabel("Value")
    plt.legend()

    plt.show()
