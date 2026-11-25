# Fintech Projects

These are three small Python notebooks I worked through to compare simple ways of building a stock portfolio from the Nifty 50 list. I kept each idea in its own notebook so I can follow the steps and change the assumptions.

## Projects

1. **Equal weight portfolio** - starts with the larger companies by market value, then works out how many shares could be bought when the investment amount is split evenly.
2. **Value investing** - compares P/E and P/B ratios across the list and uses those comparisons to create a basic value score.
3. **Dividend investing** - looks at dividend yield, dividend rate, payout ratio and historical yield, then combines the measures into a weighted score.

These are learning exercises, not investment recommendations. The results depend on data from Yahoo Finance and can change over time.

## Files

- `1-Equal_Weights.ipynb`
- `2-Value_Investing.ipynb`
- `3-Dividend_Investing.ipynb`
- `dataset/ind_nifty50list.csv` - company symbols used by the notebooks

## Run the notebooks

Open this folder as a project in PyCharm or Jupyter, install the packages below, and run a notebook from top to bottom. The notebooks read the CSV from the `dataset` folder relative to this directory.

    python -m pip install pandas numpy yfinance jupyter

The Yahoo Finance steps need an internet connection. Some values can be missing, and market data can change between runs. Each notebook asks for an investment amount before calculating share quantities.
