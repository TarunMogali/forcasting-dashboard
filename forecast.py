import pandas as pd
from prophet import Prophet

def train_and_forecast(
    data,
    periods=90,
    yearly=True,
    weekly=True,
    daily=False,
    changepoint_prior=0.05
):
    # Clean column names
    data.columns = data.columns.str.strip().str.lower()

    # Ensure required columns exist
    if "date" not in data.columns or "sales" not in data.columns:
        raise ValueError("CSV must contain 'date' and 'sales' columns")

    # Rename for Prophet
    df = data.rename(columns={"date": "ds", "sales": "y"})

    # Convert date column to datetime
    df["ds"] = pd.to_datetime(df["ds"])

    model = Prophet(
        yearly_seasonality=yearly,
        weekly_seasonality=weekly,
        daily_seasonality=daily,
        changepoint_prior_scale=changepoint_prior
    )

    model.fit(df)

    future = model.make_future_dataframe(periods=periods)
    forecast = model.predict(future)

    return model, forecast
