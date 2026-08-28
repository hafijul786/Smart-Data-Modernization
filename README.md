# 📊 Smart Data Modernization

> An end-to-end Enterprise Analytics and Business Intelligence platform that transforms raw business data into meaningful insights, customer intelligence, predictive analytics, anomaly detection, and smarter business decisions.

---

## 🚀 Project Overview

**Smart Data Modernization** is a data-driven analytics platform built using **Python, Pandas, Scikit-Learn, and Streamlit**.

The project processes business sales data and provides multiple analytics and machine learning modules through an interactive dashboard.

The platform helps businesses understand:

- Sales performance
- Profitability
- Customer behavior
- Customer segmentation
- Customer risk
- Sales predictions
- Future sales forecasting
- Business anomalies
- Data quality
- Business insights

The complete application is designed as a centralized **Enterprise Analytics Platform**.

---

## 🎯 Project Objectives

The main objectives of this project are:

1. Modernize traditional business data analysis.
2. Convert raw business data into actionable insights.
3. Analyze sales and profit performance.
4. Understand customer behavior.
5. Segment customers using RFM analysis.
6. Predict customer risk.
7. Apply machine learning for sales prediction.
8. Forecast future sales.
9. Detect unusual business transactions.
10. Monitor data quality and dataset health.
11. Provide an interactive executive dashboard.

---

# 🛠️ Technology Stack

### Programming Language

- Python 3.x

### Data Analysis

- Pandas
- NumPy

### Machine Learning

- Scikit-Learn
- Random Forest
- Customer Segmentation
- Customer Risk Prediction
- Anomaly Detection
- Sales Prediction

### Visualization

- Streamlit
- Streamlit Charts

### Development Tools

- VS Code
- Git
- GitHub

### Deployment

- Streamlit Community Cloud

---

# 📌 Main Features

## 1. 📊 Executive Dashboard

The Executive Dashboard provides a high-level overview of business performance.

### KPIs

- Total Sales
- Total Profit
- Total Quantity
- Total Orders
- Profit Margin

### Visualizations

- Yearly Sales Performance
- Category Sales & Profit
- Regional Profit
- Top 10 Customers by Profit

---

## 2. 📈 Sales Analytics

The Sales Analytics module provides detailed analysis of business sales.

### Features

- Monthly Sales Trend
- 3-Month Moving Average
- Category Analysis
- Region Analysis
- Shipping Mode Performance
- Loss-Making Sub-Categories

### Metrics

- Total Sales
- Total Profit
- Total Quantity
- Total Orders
- Profit Margin
- Average Shipping Days

---

## 3. 👥 Customer Intelligence

The Customer Intelligence module focuses on customer behavior and customer segmentation.

### RFM Analysis

RFM stands for:

- **Recency** – How recently a customer purchased
- **Frequency** – How frequently a customer purchased
- **Monetary** – How much the customer spent

### Customer Segments

The platform can display customer segments such as:

- Champions
- At Risk
- Other available segments

### Customer Risk Prediction

Customers are classified into:

- 🔴 High Risk
- 🟡 Medium Risk
- 🟢 Low Risk

### Customer Clustering

Customer clustering groups customers based on their behavioral characteristics.

---

## 4. 🤖 Machine Learning Analytics

The ML Analytics module provides predictive analytics.

### Sales Prediction

The project uses a machine learning model to predict sales.

**Model:**

Random Forest Regressor

### Model Evaluation

The dashboard displays:

- MAE
- RMSE
- R² Score

Current model results:

- MAE: `85.38`
- RMSE: `251.88`
- R² Score: `0.7219`

### Sales Forecasting

The platform also provides future sales forecasts using the generated forecasting dataset.

---

## 5. 🚨 Anomaly Detection

The Anomaly Detection module identifies unusual business transactions.

It analyzes areas such as:

- Discount anomalies
- Shipping cost anomalies
- Transaction anomalies
- Anomaly scores

### Dashboard Metrics

- Total Anomalous Records
- Discount Anomalies
- Shipping Anomalies

High-priority anomalies can also be displayed based on anomaly score.

---

## 6. 💡 Business Intelligence

The Business Intelligence module automatically generates useful business insights.

### Examples

- Highest-profit category
- Highest-profit region
- Highest-sales shipping mode
- Loss-making sub-categories
- Discount vs Profit analysis

This helps convert analytical results into business-level decisions.

---

## 7. ⚙️ Data Quality

The Data Quality module monitors the health of the dataset.

### Metrics

- Total Records
- Total Columns
- Missing Values
- Duplicate Rows
- Data Completeness
- Quality Score

### Column-Level Validation

For every column, the dashboard provides:

- Column Name
- Data Type
- Missing Values
- Unique Values

A dataset preview is also available.

---

# 🔎 Global Filters

The application provides global filters through the Streamlit sidebar.

Available filters include:

### Year

Filter the dashboard based on selected years.

### Category

Filter the business data based on product categories.

### Region

Filter data based on geographical regions.

These filters affect the main analytics dashboard dynamically.

---

# 📂 Project Structure

```text
Smart-Data-Modernization/
│
├── app.py
│
├── data/
│   ├── cleaned_superstore.csv
│   ├── rfm_customer_segments.csv
│   ├── customer_risk_predictions.csv
│   ├── customer_clusters.csv
│   ├── sales_predictions.csv
│   ├── sales_forecast.csv
│   └── anomalies.csv
│
├── notebooks/
│   └── analysis notebooks (if available)
│
├── scripts/
│   ├── customer_risk.py
│   ├── customer_clustering.py
│   ├── sales_prediction.py
│   ├── sales_forecasting.py
│   └── anomaly_detection.py
│
├── requirements.txt
│
├── README.md
│
└── .gitignore


## Clone the Repository

Open your terminal or command prompt and run:
(git clone https://github.com/YOUR_USERNAME/Smart-Data-Modernization.git)

Move into the project directory:
(cd Smart-Data-Modernization)

▶️ 7. Run the Streamlit Application

Start the application using:

streamlit run app.py

After running the command, Streamlit will provide a local URL similar to:

http://localhost:8501

Open the URL in your browser.