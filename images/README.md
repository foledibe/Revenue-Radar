# Revenue Radar

An interactive Power BI dashboard analyzing retail sales data, with a Python-powered
data pipeline feeding in from Excel.

## 🔧 Tools Used

- **Python** (pandas, openpyxl) - generating and cleaning the dataset
- **Excel** - raw and cleaned data storage
- **Power BI** - interactive dashboard and DAX measures
- **Git/GitHub** - version control

## 📊 What the Dashboard Shows

- Total revenue and average order value
- Sales trends by month
- Revenue breakdown by region and product category
- Interactive filtering by region

## 📁 Project Structure

```
Revenue-Radar/
├── data/
│   ├── raw_sales_data.xlsx
│   └── clean_sales_data.xlsx
├── scripts/
│   ├── radar_signal.py
│   └── clean_data.py
├── dashboard/
│   └── revenue_radar.pbix
├── images/
│   └── dashboard_overview.png
└── README.md
```

## 🖼️ Preview

![Dashboard Overview](images/dashboard_overview.png)

## 🚀 How to Run This Yourself

1. Clone this repo
2. Run `python scripts/radar_signal.py` to generate the sample dataset
3. Run `python scripts/clean_data.py` to clean and enrich it
4. Open `dashboard/revenue_radar.pbix` in Power BI Desktop
