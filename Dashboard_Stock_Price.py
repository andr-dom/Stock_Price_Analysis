import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import os

# ── Rutas relativas (funcionan tanto local como en Streamlit Cloud) ──
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "individual_stocks_5yr")

company_files = {
    "AAPL": os.path.join(DATA_DIR, "AAPL_data.csv"),
    "AMZN": os.path.join(DATA_DIR, "AMZN_data.csv"),
    "GOOG": os.path.join(DATA_DIR, "GOOG_data.csv"),
    "MSFT": os.path.join(DATA_DIR, "MSFT_data.csv"),
}

all_data = pd.DataFrame()
for ticker, file in company_files.items():
    current_df = pd.read_csv(file)
    all_data = pd.concat([all_data, current_df], ignore_index=True)

all_data['date'] = pd.to_datetime(all_data['date'])

# ── Page config ──
st.set_page_config(page_title="Stock Market Case Study", layout="wide")
st.title("📈 Tech Stocks Analysis Dashboard")

# ── Sidebar ──
tech_list = all_data['Name'].unique()
st.sidebar.title("Choose a Company")
selected_company = st.sidebar.selectbox("Select a stock", tech_list)

company_df = all_data[all_data['Name'] == selected_company].copy()
company_df.sort_values('date', inplace=True)

# ── 1. Closing Price ──
st.subheader(f"1. Closing Price of {selected_company} Over Time")
fig1 = px.line(company_df, x="date", y="close",
               title=selected_company + " closing prices over time")
st.plotly_chart(fig1, use_container_width=True)

# ── 2. Moving Averages ──
st.subheader("2. Moving Averages (10, 20, 50 days)")
for ma in [10, 20, 50]:
    company_df['close_' + str(ma)] = company_df['close'].rolling(ma).mean()

fig2 = px.line(company_df, x="date", y=["close", "close_10", "close_20", "close_50"],
               title=selected_company + " moving averages")
st.plotly_chart(fig2, use_container_width=True)

# ── 3. Daily Returns ──
st.subheader(f"3. Daily Returns for {selected_company}")
company_df['Daily_return(in %)'] = company_df['close'].pct_change() * 100
fig3 = px.line(company_df, x="date", y="Daily_return(in %)",
               title="Daily Return (%)")
st.plotly_chart(fig3, use_container_width=True)

# ── 4. Resampled Closing Price ──
st.subheader("4. Resampled Closing Price (Monthly/Quarterly/Yearly)")
company_df.set_index('date', inplace=True)
resample_option = st.radio("Select Resample Frequency", ["Monthly", "Quarterly", "Yearly"])

freq_map = {"Monthly": "ME", "Quarterly": "QE", "Yearly": "YE"}
resampled = company_df['close'].resample(freq_map[resample_option]).mean()

fig4 = px.line(resampled, title=f"{selected_company} {resample_option} Average Closing Price")
st.plotly_chart(fig4, use_container_width=True)

# ── 5. Correlation Heatmap ──
st.subheader("5. Closing Price Correlation Between Companies")

closing_price = pd.DataFrame()
for ticker, file in company_files.items():
    df = pd.read_csv(file)
    closing_price[ticker] = df['close']

fig5, ax = plt.subplots()
sns.heatmap(closing_price.corr(), annot=True, cmap="coolwarm", ax=ax)
st.pyplot(fig5)

st.markdown("---")
st.markdown("***Note:*** This dashboard provides basic technical analysis of major tech stocks using Python and Streamlit.")
