import pandas as pd
import random
from datetime import datetime, timedelta

random.seed(42)

regions = ["North", "South", "East", "West"]
products = {
    "Coffee Maker": ("Appliances", 45.99),
    "Blender": ("Appliances", 29.99),
    "Desk Lamp": ("Home Office", 19.99),
    "Notebook": ("Stationery", 3.49),
    "Headphones": ("Electronics", 59.99),
}

rows = []
start_date = datetime(2024, 1, 1)

for i in range(1, 251):
    date = start_date + timedelta(days=random.randint(0, 364))
    product = random.choice(list(products.keys()))
    category, price = products[product]
    units = random.randint(1, 12)
    rows.append({
        "OrderID": 1000 + i,
        "Date": date.strftime("%Y-%m-%d"),
        "Region": random.choice(regions),
        "Product": product,
        "Category": category,
        "UnitsSold": units,
        "UnitPrice": price,
        "Revenue": round(units * price, 2),
    })

df = pd.DataFrame(rows)
df.to_excel("data/raw_sales_data.xlsx", index=False)
print("Done! Saved data/raw_sales_data.xlsx")