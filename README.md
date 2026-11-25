# Solar Sales Analysis - Interactive KPI Dashboard

## Live Demo
**Deployed App (Streamlit Cloud):** https://solar-sales-analysis-djv9q9f4g8x5bvx5h9i8zpy.streamlit.app/
**GitHub Repo:** https://github.com/husnainshahbaz979-786/solar-sales-analysis

This deployed app runs the same code as `src/app.py` in this repo.

## Demo Video
Watch Demo: https://youtu.be/kc6RDm5_QtA

## What it does
- Generates 500 fake solar sales records
- Cleans the data (duplicates, missing values)
- Analyzes total sales by Region, Product, and Sales Rep
- Interactive dashboard with sidebar filters, date range, region filter and Plotly charts
- Shows Total Revenue, Total Sales, Total Records

## How to run - Streamlit Dashboard
pip install -r requirements.txt
streamlit run src/app.py
Then open: http://localhost:8501

## How to run - Old Analysis Scripts
pip install -r requirements.txt
python src/load_data.py
python src/analyze_data.py
