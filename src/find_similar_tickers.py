from src.analyzer import cosine_similarity


def find_similar_tickers(stock_prices_data, ticker_referece, analyze_duration, limit=5):
    # get last 90days of ticker data
    stock_prices_data[ticker_referece][-analyze_duration:],

    tickers = stock_prices_data.columns[1:]
    all_tickers_score = []
    for ticker in tickers:
        if ticker == ticker_referece:
            continue

        highest_similar_score = 0
        start_date = stock_prices_data["date"][0]
        end_date = stock_prices_data["date"][analyze_duration]
        for i in range(len(stock_prices_data[ticker]) - analyze_duration):
            similarity = cosine_similarity(
                stock_prices_data[ticker_referece][i : i + analyze_duration],
                stock_prices_data[ticker][i : i + analyze_duration],
            )
            if similarity > highest_similar_score:
                start_date = stock_prices_data["date"][i]
                end_date = stock_prices_data["date"][i + analyze_duration]
                highest_similar_score = max(highest_similar_score, similarity)

        all_tickers_score.append((ticker, start_date, end_date, highest_similar_score))

    all_tickers_score.sort(key=lambda x: x[3], reverse=True)
    for i, ticker in enumerate(all_tickers_score[:limit]):
        all_tickers_score[i] = (i + 1, ticker[0], ticker[1], ticker[2], ticker[3])

    return all_tickers_score[:limit]
