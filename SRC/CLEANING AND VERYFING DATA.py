# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 20:53:09 2026

@author: hp
"""

import pandas as pd

df = pd.read_csv(r"C:\Users\hp\Desktop\MINI PROJECT\sales_data.csv")

# Fill missing values using mean
df["Quantity"] = df["Quantity"].fillna(df["Quantity"].mean())
df["Revenue"] = df["Revenue"].fillna(df["Revenue"].mean())

# Round the filled values
df["Quantity"] = df["Quantity"].round(0)
df["Revenue"] = df["Revenue"].round(0)

print(df)

print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

# Total Revenue
total_revenue = df["Revenue"].sum()

# Average Revenue
average_revenue = df["Revenue"].mean()

print("\nTotal Revenue:", total_revenue)
print("Average Revenue:", average_revenue)

product_revenue = df.groupby("Product")["Revenue"].sum()

print(product_revenue)

import matplotlib.pyplot as plt
plt.figure(figsize=(7,4))

product_revenue.plot(kind="bar")

plt.title("Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Revenue")

plt.xticks(rotation=45, ha="right")

plt.tight_layout()

plt.show()

import matplotlib.pyplot as plt

categories = {
    "Serums": 6,
    "Moisturizers": 2,
    "Sun Care": 2,
    "Essences": 2,
    "Cleansers": 1,
    "Acne Care": 1,
    "Lip Care": 1,
    "Beauty Devices": 1
}

plt.figure(figsize=(5,5))

plt.pie(categories.values(),
        labels=categories.keys(),
        autopct="%1.1f%%")

plt.title("Distribution of Skincare Product Categories")

plt.show()

df["Date"] = pd.to_datetime(df["Date"])

monthly_revenue = df.groupby(df["Date"].dt.month)["Revenue"].sum()

import matplotlib.pyplot as plt

plt.figure(figsize=(6,3))

plt.plot(monthly_revenue.index,
         monthly_revenue.values,
         marker="o")

plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")

plt.grid(True)

plt.tight_layout()

plt.show()