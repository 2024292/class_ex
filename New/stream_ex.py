import streamlit as st
import pandas as pd
import plotly.express as px

# 设置页面标题
st.set_page_config(page_title="Irish Agriculture Dashboard", layout="wide")

# 页面标题
st.title("🇮🇪 Irish Agriculture Dashboard for Farmers")

# --- 数据加载 ---
@st.cache_data
def load_data():
    # 示例数据，可以替换为实际数据文件路径
    export_data = pd.DataFrame({
        "Year": [2018, 2019, 2020, 2021, 2022],
        "Category": ["Beef", "Beef", "Dairy", "Dairy", "Beef"],
        "Export_Value (€)": [1500, 1600, 2000, 2100, 1800],
        "Quantity (Tonnes)": [500, 550, 700, 750, 600]
    })
    
    area_yield_data = pd.DataFrame({
        "Year": [2018, 2019, 2020, 2021, 2022],
        "Region": ["West", "East", "South", "North", "Midlands"],
        "Area (Hectares)": [1000, 1200, 1100, 1300, 1250],
        "Production (Tonnes)": [400, 500, 450, 600, 550]
    })
    
    sentiment_data = pd.DataFrame({
        "Source": ["Twitter", "News", "Reddit", "Forum", "News"],
        "Sentiment": ["Positive", "Negative", "Neutral", "Positive", "Negative"],
        "Count": [120, 80, 50, 150, 90]
    })

    return export_data, area_yield_data, sentiment_data

export_data, area_yield_data, sentiment_data = load_data()

# --- 导航栏 ---
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Export Analysis", "Land & Production", "Sentiment Analysis"])

# --- 出口数据可视化 ---
if page == "Export Analysis":
    st.header("📊 Agricultural Export Analysis")
    
    # 显示数据表格
    st.dataframe(export_data)

    # 按年份和类别筛选
    year = st.selectbox("Select Year", export_data["Year"].unique())
    filtered_data = export_data[export_data["Year"] == year]
    
    # 柱状图
    fig = px.bar(filtered_data, x="Category", y="Export_Value (€)", 
                 title=f"Export Value by Category in {year}", color="Category")
    st.plotly_chart(fig, use_container_width=True)

# --- 耕地面积和产量可视化 ---
elif page == "Land & Production":
    st.header("🌾 Land Area and Production Trends")
    
    # 显示数据表格
    st.dataframe(area_yield_data)

    # 折线图
    fig = px.line(area_yield_data, x="Year", y=["Area (Hectares)", "Production (Tonnes)"], 
                  title="Land Area and Production Over the Years", markers=True)
    st.plotly_chart(fig, use_container_width=True)

# --- 情感分析结果可视化 ---
elif page == "Sentiment Analysis":
    st.header("💬 Sentiment Analysis on Livestock Products")
    
    # 显示数据表格
    st.dataframe(sentiment_data)

    # 饼图
    fig = px.pie(sentiment_data, names="Sentiment", values="Count", 
                 title="Sentiment Distribution on Livestock Products")
    st.plotly_chart(fig, use_container_width=True)

# --- 底部信息 ---
st.sidebar.info("Developed by [Your Name]. Powered by Streamlit.")