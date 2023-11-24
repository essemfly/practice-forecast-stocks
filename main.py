from src.data_loader import load_data_from_csv
from src.find_similar_tickers import find_similar_tickers

SAMPLE_DATA_PATH = "./data/sample_stock_prices.csv"
ANALYZE_DURATION = 90


def main():
    stock_prices_data = load_data_from_csv(SAMPLE_DATA_PATH)
    tickers = stock_prices_data.columns[1:]

    while True:
        ticker = input("Enter a stock ticker: ").strip()
        if ticker == "exit":
            print("bye")
            return
        if ticker not in tickers:
            print(f"You entered a invalid ticker: {ticker}")
            continue
        similar_tickers = find_similar_tickers(stock_prices_data, ticker, ANALYZE_DURATION)
        print(f"Similar tickers to {ticker}:", similar_tickers)


if __name__ == "__main__":
    main()
