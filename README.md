# Demand Forecasting Dashboard

A web-based application for forecasting demand using Facebook Prophet, built with Streamlit.

## Description

This project provides an interactive dashboard to forecast future sales or demand based on historical data. It uses the Prophet library for time series forecasting and offers visualizations of forecasts, trends, and seasonality components.

## Features

- Upload custom CSV data or use the provided sample data
- Adjustable forecast horizon (30-180 days)
- Configurable seasonality (yearly, weekly, daily)
- Trend flexibility settings
- Interactive plots with upper and lower bounds
- Download forecast results as CSV
- Trend and seasonality component analysis

## Installation

1. Clone or download this repository.

2. Navigate to the project directory:
   ```
   cd new_project
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run the Streamlit app:
   ```
   streamlit run app.py
   ```

2. Open your web browser and go to the URL displayed (usually `http://localhost:8501`).

3. Upload your sales data CSV file (must contain 'date' and 'sales' columns) or use the default sample data.

4. Adjust forecast settings in the sidebar:
   - Forecast horizon
   - Seasonality options
   - Trend flexibility

5. View the forecast plot, historical data, and components.

6. Download the forecast results if needed.

## Data Format

The CSV file must contain at least two columns:
- `date`: Date in a recognizable format (e.g., YYYY-MM-DD)
- `sales`: Numerical sales or demand values

Example:
```
date,sales
2023-01-01,100
2023-01-02,120
...
```

## Dependencies

- streamlit
- pandas
- prophet
- plotly
- matplotlib

## License

This project is open-source. Feel free to use and modify as needed.
