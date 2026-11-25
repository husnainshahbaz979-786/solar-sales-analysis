import streamlit as st
import pandas as pd
import plotly.express as px
import os

st.set_page_config(page_title="SunGrid Solar Sales", layout="wide")

st.title("SunGrid Solar Sales Dashboard")
st.markdown("Key metrics from EDA - based on cleaned_preview.csv")

@st.cache_data
def load_data():
    # CSV ka rasta dhoondna - chahe kahan bhi ho
    possible_paths = [
        "data/cleaned_preview.csv",
        "cleaned_preview.csv",
        "../data/cleaned_preview.csv",
        "../cleaned_preview.csv",
        "src/cleaned_preview.csv"
    ]
    file_path = None
    for p in possible_paths:
        if os.path.exists(p):
            file_path = p
            break
    
    if file_path is None:
        st.error("cleaned_preview.csv nahi mili! Check karo file kahan hai.")
        st.stop()

    df = pd.read_csv(file_path)
    df['DATE_TIME'] = pd.to_datetime(df['DATE_TIME'])
    # Mapping as used in Task 2
    df['Sales'] = df['DC_POWER']
    df['Revenue'] = df['AC_POWER']
    # Region from SOURCE_KEY (dataset me region column nahi hai)
    df['Region'] = df['SOURCE_KEY'].astype(str).str[:4]
    return df

df = load_data()

# --- Sidebar: 3 Widgets ---
st.sidebar.header("Filters")
min_date = df['DATE_TIME'].min().date()
max_date = df['DATE_TIME'].max().date()

date_range = st.sidebar.date_input("Select Date Range", [min_date, max_date], min_value=min_date, max_value=max_date)
regions = st.sidebar.multiselect("Select Region", sorted(df['Region'].unique()), default=sorted(df['Region'].unique()))
top_n = st.sidebar.slider("Top Products to Show", 3, 10, 5)

# Filter data
start_date, end_date = pd.to_datetime(date_range[0]), pd.to_datetime(date_range[1])
filtered = df[(df['DATE_TIME'].dt.date >= start_date.date()) & (df['DATE_TIME'].dt.date <= end_date.date())]
filtered = filtered[filtered['Region'].isin(regions)]

# --- KPI Cards: 4 Visual Components ---
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Revenue", f"{filtered['Revenue'].sum():,.0f}")
col2.metric("Total Sales (DC_POWER)", f"{filtered['Sales'].sum():,.0f}")
col3.metric("Avg Installation Size", f"{filtered['Sales'].mean():,.2f}")
col4.metric("Total Records", f"{len(filtered):,}")

# --- Charts ---
# 1. Top Products Bar Chart
top_products = filtered.groupby('Region')['Revenue'].sum().sort_values(ascending=False).head(top_n).reset_index()
fig1 = px.bar(top_products, x='Region', y='Revenue', title='Top Products by Revenue (by Region)')
st.plotly_chart(fig1, use_container_width=True)

# 2. Monthly Sales Line Chart
filtered['Month'] = filtered['DATE_TIME'].dt.to_period('M').astype(str)
monthly = filtered.groupby('Month')['Sales'].sum().reset_index()
fig2 = px.line(monthly, x='Month', y='Sales', title='Monthly Sales Trend')
st.plotly_chart(fig2, use_container_width=True)