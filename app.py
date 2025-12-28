import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from forecast import train_and_forecast

st.set_page_config(page_title="Demand Forecasting Dashboard", layout="wide")

st.title("📈 Demand Forecasting Dashboard")
st.write("Forecast future demand using **Facebook Prophet**")

# Sidebar
st.sidebar.header("Forecast Settings")

forecast_days = st.sidebar.slider(
    "Forecast Horizon (days)",
    min_value=30,
    max_value=180,
    value=90
)

changepoint_prior = st.sidebar.slider(
    "Trend Flexibility (Changepoint Prior)",
    min_value=0.01,
    max_value=0.5,
    value=0.05
)

yearly = st.sidebar.checkbox("Yearly Seasonality", True)
weekly = st.sidebar.checkbox("Weekly Seasonality", True)
daily = st.sidebar.checkbox("Daily Seasonality", False)

# Upload data
uploaded_file = st.file_uploader(
    "Upload Sales CSV (date, sales)",
    type=["csv"]
)

if uploaded_file:
    data = pd.read_csv(uploaded_file)
else:
    data = pd.read_csv("data/sales_data.csv")

st.subheader("📄 Historical Sales Data")
st.dataframe(data)

# Forecast
model, forecast = train_and_forecast(
    data,
    periods=forecast_days,
    yearly=yearly,
    weekly=weekly,
    daily=daily,
    changepoint_prior=changepoint_prior
)

# Plot forecast
st.subheader("🔮 Demand Forecast")

fig = go.Figure()

fig.add_trace(go.Scatter(
    x=forecast["ds"],
    y=forecast["yhat"],
    mode="lines",
    name="Forecast"
))

fig.add_trace(go.Scatter(
    x=forecast["ds"],
    y=forecast["yhat_upper"],
    mode="lines",
    name="Upper Bound",
    line=dict(width=0),
    showlegend=False
))

fig.add_trace(go.Scatter(
    x=forecast["ds"],
    y=forecast["yhat_lower"],
    mode="lines",
    fill="tonexty",
    name="Lower Bound",
    line=dict(width=0),
    fillcolor="rgba(0,100,80,0.2)"
))

fig.update_layout(
    xaxis_title="Date",
    yaxis_title="Sales",
    hovermode="x"
)

st.plotly_chart(fig, use_container_width=True)

# Components
st.subheader("📊 Trend & Seasonality Components")

components_fig = model.plot_components(forecast)
st.pyplot(components_fig)

# Download forecast
st.subheader("⬇️ Download Forecast")
csv = forecast.to_csv(index=False).encode("utf-8")
st.download_button(
    "Download Forecast CSV",
    csv,
    "forecast.csv",
    "text/csv"
)
