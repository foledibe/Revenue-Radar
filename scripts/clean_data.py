import pandas as pd

# Load the raw data
df = pd.read_excel("data/raw_sales_data.xlsx")

# Drop exact duplicate rows, if any
df = df.drop_duplicates()

# Make sure Date is a real date type, not just text
df["Date"] = pd.to_datetime(df["Date"])

# Add a "Month" column — useful for Power BI charts later
df["Month"] = df["Date"].dt.strftime("%B")

# Add a "Quarter" column too
df["Quarter"] = "Q" + df["Date"].dt.quarter.astype(str)

# Double check Revenue math is consistent
df["Revenue"] = (df["UnitsSold"] * df["UnitPrice"]).round(2)

# Save the cleaned version — THIS is the file Power BI will use
df.to_excel("data/clean_sales_data.xlsx", index=False)
print("Cleaned data saved to data/clean_sales_data.xlsx")