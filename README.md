# Stock Price Analysis — Tech Stocks Case Study

An exploratory data analysis and interactive dashboard project focused on the stock market performance of major tech companies (AAPL, AMZN, GOOG, MSFT) over a 5-year period, built with Python and Streamlit.

---

## Table of Contents

- [Project Overview](#project-overview)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Analysis Workflow](#analysis-workflow)
- [Dashboard Features](#dashboard-features)
- [How to Run](#how-to-run)

---

## Project Overview

This project performs a comprehensive technical analysis of four major tech stocks using historical price data. It includes an exploratory data analysis (EDA) notebook and a fully interactive Streamlit dashboard for visual exploration.

**Companies analyzed:**
| Ticker | Company |
|--------|---------|
| AAPL | Apple Inc. |
| AMZN | Amazon.com Inc. |
| GOOG | Alphabet Inc. (Google) |
| MSFT | Microsoft Corporation |

---

## Tech Stack

| Tool | Purpose |
|------|---------|
| ![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white) | Core language |
| ![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat&logo=pandas&logoColor=white) | Data manipulation |
| ![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=streamlit&logoColor=white) | Interactive dashboard |
| ![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=flat&logo=plotly&logoColor=white) | Interactive charts |
| ![Seaborn](https://img.shields.io/badge/Seaborn-4C72B0?style=flat) | Correlation heatmap |
| ![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=flat) | Static plots |

---

## Project Structure

```
Stock_Price_Analysis/
│
├── Stock_price_analysis.ipynb          # EDA notebook
├── Dashboard_Stock_Price.py            # Streamlit dashboard
├── individual_stocks_5yr/              # Raw CSV data
│   ├── AAPL_data.csv
│   ├── AMZN_data.csv
│   ├── GOOG_data.csv
│   └── MSFT_data.csv
└── README.md
```

---

## Analysis Workflow

### 1. EDA Notebook (`Stock_price_analysis.ipynb`)
- Loaded and merged historical stock data for all 4 companies
- Explored price trends, volume, and return distributions
- Calculated moving averages and daily returns
- Analyzed correlations between stocks

### 2. Streamlit Dashboard (`Dashboard_Stock_Price.py`)
- Built an interactive multi-page dashboard for visual exploration
- Company selector via sidebar
- Dynamic resampling options (Monthly / Quarterly / Yearly)

---

## Dashboard Features

| # | Visualization | Description |
|---|--------------|-------------|
| 1 | **Closing Price Over Time** | Historical price trend for selected stock |
| 2 | **Moving Averages** | 10, 20, and 50-day rolling averages vs. close price |
| 3 | **Daily Returns (%)** | Day-over-day percentage change in closing price |
| 4 | **Resampled Closing Price** | Monthly, Quarterly, or Yearly average closing price |
| 5 | **Correlation Heatmap** | Cross-company closing price correlation (Seaborn) |
