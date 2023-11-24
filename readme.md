# Similar Stocks

## Installation
To get started, install the required packages:

> pip install -r requirements.txt

Start the application

> python main.py

## Example Usage

'''
Enter a stock ticker: A000390
Similar tickers to A000390: [
(1, 'A000850', '2016-06-21', '2016-11-01', 0.9998597495307318),
(2, 'A001460', '2017-09-04', '2018-01-19', 0.9998423548323742),
(3, 'A001720', '2016-06-22', '2016-11-02', 0.9998410764022848),
(4, 'A001130', '2017-08-31', '2018-01-17', 0.9998346156897776),
(5, 'A001530', '2016-06-14', '2016-10-25', 0.9998210524366685)
]
'''

## Code Explanation
- The CLI interface allows users to input a stock ticker and receive results.
- `data_loader.py` is used to fetch data from the existing `sample_stock_prices.csv`.
- Initially, cosine similarity is used for calculating similarity. It observes the correlation between two vectors, normalized for computation.
- For each stock, data from 2015-01-02 to 2019-12-30 is segmented into 90-day periods, and similarity is calculated for all cases.
  - Currently, a brute force approach is used for these calculations. As the number of cases and stocks increase, the time to compute and produce results will also increase. There's a need to explore and test different methods for more efficient processing.
  - Presently, calculations are performed for all cases, but sampling over intervals can be an alternative approach.
- The implementation is class-based with OOP, enhancing maintainability and ease of adding new features. It involves:
  - Loading data
  - Attaching a model
  - Receiving input stock values and generating output
